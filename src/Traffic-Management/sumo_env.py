import os
import gym
import numpy as np
import traci
from gym import spaces
from RL_files.action import apply_action
from RL_files.reward import compute_reward
from RL_files.state import get_state

class SumoEnv(gym.Env):
    def __init__(self, sumo_binary, sumo_cfg_file, use_gui=False):
        super(SumoEnv, self).__init__()

        # SUMO configuration
        self.sumo_binary = sumo_binary
        self.sumo_cfg_file = sumo_cfg_file
        self.use_gui = use_gui

        # Connection to SUMO
        self.sumo_cmd = self._get_sumo_cmd()
        traci.start(self.sumo_cmd)

        # Define observation and action spaces
        self.action_space = spaces.MultiDiscrete([3] * self.get_num_traffic_lights())
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.get_state_shape(),), dtype=np.float32)

    def _get_sumo_cmd(self):
        # SUMO command to start the simulation
        sumo_cmd = [self.sumo_binary, "-c", self.sumo_cfg_file]
        if self.use_gui:
            sumo_cmd.append("--start")
        return sumo_cmd

    def get_num_traffic_lights(self):
        return len(traci.trafficlight.getIDList())

    def get_state_shape(self):
        """
        Calculates the shape of the state space based on the number of traffic lights,
        vehicle densities, and waiting times at lanes controlled by traffic lights.
        
        Returns:
            int: The total size of the state vector.
        """
        # Get the list of traffic light IDs
        traffic_light_ids = traci.trafficlight.getIDList()
        
        # Initialize variables for counting the state components
        num_traffic_lights = len(traffic_light_ids)
        num_lanes = 0
        
        # Iterate over each traffic light to count the number of controlled lanes
        for tl_id in traffic_light_ids:
            lanes = traci.trafficlight.getControlledLanes(tl_id)
            num_lanes += len(lanes)  # Accumulate the number of lanes

        # State size: traffic light phases + vehicle densities + waiting times
        state_size = num_traffic_lights + num_lanes * 2  # One for density, one for waiting time per lane

        return state_size

    def reset(self):
        # Close any existing SUMO simulation
        if traci.getConnection():
            traci.close()
        
        # Start a new SUMO simulation
        traci.start(self.sumo_cmd)
        state = get_state()

        # Ensure the state shape matches the observation space
        state = np.reshape(state, self.observation_space.shape)
        return state

    def step(self, action):
        # Apply the action to each traffic light
        traffic_light_ids = traci.trafficlight.getIDList()
        for tl_id, tl_action in zip(traffic_light_ids, action):
            apply_action(tl_id, tl_action)
        
        # Run one step of the simulation
        traci.simulationStep()

        # Get the new state and reward
        state = get_state()
        reward = compute_reward()

        # Ensure the state shape matches the observation space
        state = np.reshape(state, self.observation_space.shape)

        # Check if the simulation is finished
        done = traci.simulation.getMinExpectedNumber() == 0

        return state, reward, done, {}

    def close(self):
        # Close the SUMO simulation
        if traci.getConnection():
            traci.close()