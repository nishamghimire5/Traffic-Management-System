import os
import time
import traci
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback, EvalCallback
from sumo_env import SumoEnv  # Import the custom environment

# Enable TensorBoard for logging training progress
tensorboard_log_dir = "./tensorboard_logs/"

# Define the paths for SUMO binary and config file
SUMO_BINARY = "sumo"  # Use "sumo-gui" for graphical interface
SUMO_CONFIG_FILE = "sumo_files/osm.sumocfg"  # Path to your SUMO config file

# Initialize the SUMO environment
env = SumoEnv(sumo_binary=SUMO_BINARY, sumo_cfg_file=SUMO_CONFIG_FILE, use_gui=False)

# Define the PPO model with adjusted parameters
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=0.0003,  # Adjust as needed
    n_steps=2048,  # Number of steps to run for each environment per update
    batch_size=128,  # Number of samples in each minibatch
    n_epochs=10,  # Number of epochs when optimizing the surrogate loss
    gamma=0.99,  # Discount factor
    gae_lambda=0.95,  # Factor for trade-off of bias vs variance for Generalized Advantage Estimator
    clip_range=0.2,  # Clipping parameter for PPO
    clip_range_vf=None,  # Clipping parameter for the value function (set to None to disable)
    ent_coef=0.01,  # Entropy coefficient for exploration
    vf_coef=0.5,  # Value function coefficient
    max_grad_norm=0.5,  # Max gradient norm for gradient clipping
    use_sde=False,  # Whether to use generalized State Dependent Exploration
    sde_sample_freq=-1,  # Sample a new noise matrix every n steps when using SDE
    target_kl=0.03,  # Target KL divergence threshold for early stopping
    tensorboard_log=tensorboard_log_dir,
    verbose=1
)

# Create a callback for saving checkpoints every 10000 steps
checkpoint_dir = "./checkpoints/"
os.makedirs(checkpoint_dir, exist_ok=True)
checkpoint_callback = CheckpointCallback(
    save_freq=100000,
    save_path=checkpoint_dir,
    name_prefix="ppo_sumo_model",
    save_replay_buffer=True,
    save_vecnormalize=True,
)

# Create an evaluation callback to evaluate the model periodically
eval_callback = EvalCallback(env, best_model_save_path="./logs/best_model/",
                             log_path="./logs/results/", eval_freq=5000)

# Start training the model
print("Starting training...")
start_time = time.time()

# Train the model for a certain number of timesteps with logging and checkpointing enabled
model.learn(
    total_timesteps=1000000,
    callback=[checkpoint_callback, eval_callback],
    tb_log_name="PPO_Sumo_Training"
)

# Calculate and print the total training time
end_time = time.time()
print(f"Training finished in {end_time - start_time:.2f} seconds")

# Save the final trained model
final_model_path = os.path.join(checkpoint_dir, "ppo_sumo_final_model")
model.save(final_model_path)
print(f"Final model saved to {final_model_path}")

# Close the SUMO environment to properly end the simulation
env.close()