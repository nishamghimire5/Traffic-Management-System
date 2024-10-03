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

# Define the PPO model and enable TensorBoard logging
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=tensorboard_log_dir)

# Create a callback for saving checkpoints during training
checkpoint_callback = CheckpointCallback(save_freq=10000, save_path="./models/", name_prefix="ppo_sumo")

# Create an evaluation callback to evaluate the model periodically
eval_callback = EvalCallback(env, best_model_save_path="./logs/best_model/",
                             log_path="./logs/results/", eval_freq=5000)

# Start training the model
print("Starting training...")
start_time = time.time()

# Train the model for a certain number of timesteps with logging enabled
model.learn(total_timesteps=100000, callback=[checkpoint_callback, eval_callback], tb_log_name="PPO_Sumo_Training")

# Calculate and print the total training time
end_time = time.time()
print(f"Training finished in {end_time - start_time:.2f} seconds")

# Save the trained model
model.save("ppo_sumo_final_model")

# Close the SUMO environment to properly end the simulation
env.close()
