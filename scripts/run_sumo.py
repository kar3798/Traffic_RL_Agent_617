import traci

sumo_binary = "sumo-gui"  # or "sumo" for faster headless mode
sumo_config = "environment/config.sumocfg"

traci.start([sumo_binary, "-c", sumo_config])

for step in range(3600):
    traci.simulationStep()

traci.close()
