import os
import sys
import random  # For random actions

# Step 1: Set SUMO_HOME and Import TraCI
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

import traci

# Step 2: Define SUMO Configuration (Adjust Path)
sumo_binary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"
sumo_config = r"C:\Users\Kartikeya A Yadav\Desktop\Traffic-RL-Project\environment\config.sumocfg"

# Step 3: Start SUMO with Traci
traci.start([sumo_binary, "-c", sumo_config])
print("Simulation started.")

# Step 4: Define Variables
vehicle_speed = 0
total_speed = 0
step_count = 0

# Define Traffic Light ID (Update to your correct traffic light ID)
traffic_light_id = "110239609"  # Replace with your correct ID
num_phases = 4  # Number of possible light phases

# Step 5: Run Simulation (Basic Random Agent)
while traci.simulation.getMinExpectedNumber() > 0:
    # Randomly select an action (0 to 3)
    action = random.randint(0, num_phases - 1)

    # Apply the action (set traffic light phase)
    traci.trafficlight.setPhase(traffic_light_id, action)

    # Advance simulation by one step
    traci.simulationStep()
    print(f"Step: {step_count}, Action: {action}")

    # Monitor Vehicles
    vehicle_ids = traci.vehicle.getIDList()
    if len(vehicle_ids) > 0:
        print(f"Active Vehicles: {vehicle_ids}")
        for vehicle in vehicle_ids:
            vehicle_speed = traci.vehicle.getSpeed(vehicle)
            total_speed += vehicle_speed
            print(f"Vehicle {vehicle} Speed: {vehicle_speed} m/s")

    step_count += 1

# Step 6: Close Simulation
traci.close()
print("Simulation finished.")
