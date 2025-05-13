import os
import gym
import traci
import numpy as np
from gym import spaces


class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()
        self.sumo_binary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"  # Use "sumo" for headless training
        self.sumo_config = os.path.abspath(r"C:\Users\Kartikeya A Yadav\Desktop\Traffic-RL-Project\environment\config.sumocfg")

        # Define action and observation spaces
        self.action_space = spaces.Discrete(4)  # Four possible phases for the light
        self.observation_space = spaces.Box(low=0, high=1000, shape=(4,), dtype=np.float32)
        self.reset()

    def reset(self):
        traci.start([self.sumo_binary, "-c", self.sumo_config])
        self.steps = 0
        return self._get_state()

    def _get_state(self):
        queue_lengths = [
            traci.lane.getLastStepVehicleNumber("12185366#3_0"),  # North-South (34th)
            traci.lane.getLastStepVehicleNumber("12185366#4_0"),  # North-South (34th)
            traci.lane.getLastStepVehicleNumber("194358838#0_0"),  # West-East (Spring Garden)
            traci.lane.getLastStepVehicleNumber("387422143#0_0")  # West-East (Spring Garden)
        ]
        return np.array(queue_lengths, dtype=np.float32)

    def step(self, action):
        # Set traffic light phase based on action
        traci.trafficlight.setPhase("110239609", action)
        traci.simulationStep()
        print("Simulation stepped.")

        # Calculate reward as negative of total queue length (minimize congestion)
        state = self._get_state()
        print(f"Current State: {state}")
        reward = -np.sum(state)  # Minimize queue length
        self.steps += 1
        done = self.steps >= 3600  # 1-hour simulation
        print(f"Step: {self.steps}, Reward: {reward}")

        return state, reward, done, {}

    def render(self, mode="human"):
        pass  # Optional for debugging

    def close(self):
        traci.close()
