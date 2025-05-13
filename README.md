# Traffic Light Control with SUMO and Reinforcement Learning 🚦

This project is an implementation of a Traffic Light Control system using SUMO (Simulation of Urban MObility) and a Reinforcement Learning (RL) agent. The system allows for the control of traffic lights in an intersection and uses SUMO's TraCI API for real-time control.

---

## Features
- **Traffic Light Control:** Manages traffic lights at a multi-lane intersection.
- **Reinforcement Learning (RL):** A basic random agent is used as a baseline.
- **SUMO Integration:** Uses SUMO-GUI for visualization.
- **Dynamic Route Control:** Routes can be easily defined in the configuration files.
- **Error Handling:** Robust error handling for connection and route issues.

---

## Project Structure
``` plaintext
Traffic-RL-Project/
├── environment/ # SUMO Configuration Files
│ ├── config.sumocfg # Main SUMO configuration file
│ ├── intersection.net.xml # Network file (intersection layout)
│ ├── tls.add.xml # Traffic light settings
│ └── traffic.rou.xml # Vehicle routes
│
├── agents/
│ └── basic_agent.py # Basic random agent controlling the traffic light
│
├── gym_traffic/
│ └── traffic_env.py # Custom Gym-compatible environment (RL)
│
└── scripts/
└── run_sumo.py # Debugging script for running SUMO
```

---

## Requirements
- **Python 3.8+**
- **SUMO (Simulation of Urban MObility)**
- **Gymnasium (for RL integration)**

### Python Packages:
```bash
pip install gymnasium traci numpy
```
### Running the Simulation:
```bash
python agents/basic_agent.py
python scripts/run_sumo.py
```
