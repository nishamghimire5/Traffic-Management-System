import os
import time
import traci
from stable_baselines3 import PPO
from sumo_env import SumoEnv  # Import the custom environment

# Define the paths for SUMO binary and config file
SUMO_BINARY = "sumo"  # Use "sumo-gui" for graphical interface
SUMO_CONFIG_FILE = "sumo_files/osm.sumocfg"  # Path to your SUMO config file

# Initialize the SUMO environment
env = SumoEnv(sumo_binary=SUMO_BINARY, sumo_cfg_file=SUMO_CONFIG_FILE, use_gui=False)

# Path to the saved model
model_path = "./checkpoints/ppo_sumo_final_model.zip"

# Load the trained model
model = PPO.load(model_path)

def predict():
    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        total_reward += reward


    print(f"Total reward: {total_reward}")

    # Close the SUMO environment to properly end the simulation
    env.close()

# Run the prediction function
predict()