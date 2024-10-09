# Traffic Management System using SUMO and Reinforcement Learning

## Introduction
This project demonstrates a Traffic Management System using SUMO (Simulation of Urban MObility) integrated with Reinforcement Learning (RL) environments. The system is designed to optimize traffic flow and reduce congestion at intersections using advanced RL techniques.
## Goals
- Design and implement an adaptive traffic signal control system.
- Create a simulated traffic environment for testing.
- Train a reinforcement learning (RL) model to optimize traffic flow.
- Reduce congestion at intersections through real-time decision-making.
- Leverage RL algorithms for dynamic and efficient traffic control.
- Utilize SUMO (Simulation of Urban MObility) as the simulation environment.
## Contributors
<table>
<tr>
    <td align="center" width="200">
      <pre><a href="https://github.com/dklkushal07" target="_blank"><img src="https://avatars.githubusercontent.com/u/68638711?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Kushal Dhakal</sub></a></pre>
    </td>
        <td align="center" width="200">
      <pre><a href="https://github.com/nishamghimire5" target="_blank "><img src="https://avatars.githubusercontent.com/u/77533996?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Nisham Ghimire</sub></a></pre>
    </td>
        <td align="center" width="200">
      <pre><a href="https://github.com/Shubham-karn" target="_blank" ><img src="https://avatars.githubusercontent.com/u/147227439?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Shubham Karn</sub></a></pre>
    </td>
        <td align="center" width="200">
      <pre><a href="https://github.com/dklgarima" target="_blank"><img src="https://avatars.githubusercontent.com/u/66936719?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Garima Dhakal</sub></a></pre>
    </td>
</tr>
</table>

## Project Architecture
The project is divided into the following components:

### 1. SUMO Environment Setup
- **Traffic Simulation**: While SUMO itself is not an AI component, it provides a simulated environment used for training AI models. The traffic scenarios created serve as datasets for reinforcement learning.

### 2. RL Model Design
- **Objective Definition**: Defining the objectives (e.g., minimizing waiting time or congestion) is essential for the RL model. This determines what the model should aim to optimize.
- **Algorithm Selection**: Choosing the appropriate reinforcement learning algorithm (such as PPO, DQN, etc.) involves understanding various AI techniques that affect learning efficiency and model performance.
- **Architecture Design**: Designing the architecture of the RL model (e.g., neural networks) plays a crucial role in how the model processes input and makes decisions.

### 3. Integration with Gymnasium
- **Gym Environment Development**: Developing a Gym environment tailored for SUMO applies AI principles to simulate the traffic system dynamics and allow the RL model to learn effectively.
- **Model Integration**: Implementing the RL model within the Gym framework enables interaction and training between the learning algorithm and the simulation.

### 4. Model Training
- **Reinforcement Learning Training**: The RL model learns from the traffic simulation data provided by SUMO, iteratively adjusting parameters based on feedback from the environment.
- **Performance Optimization**: Fine-tuning the model to enhance decision-making capabilities through techniques such as hyperparameter tuning or training improvements.
<br />
<img src="https://github.com/user-attachments/assets/dc44fd51-00bc-4226-8976-f96c4d0b42d1" alt="Architecture Diagram" width="340"/>

<br />

<img src="https://github.com/user-attachments/assets/22570682-a7f8-4775-b7fb-e9adffb5561c" alt="Architecture Drawio" width="500"/>






# Status
## Known Issue
## High Level Next Steps
- **Implement Advanced RL Techniques**: Explore and integrate state-of-the-art algorithms (e.g., PPO, TRPO, A3C) for improved performance.
- **Optimize Hyperparameters**: Conduct systematic tuning and experiment with various neural network architectures.
- **Expand Traffic Scenarios**: Introduce diverse scenarios with varying traffic densities and road configurations.
- **Real-Time Data Integration**: Investigate methods to incorporate real-time traffic data and sensor inputs.
- **Develop Visualization Tools**: Create dashboards to monitor traffic flow and model performance.
- **Conduct User Testing**: Engage with stakeholders for feedback on usability and effectiveness.

# Usage
## Installation and Setup Instructions

1. **Install the Latest Software:**
   - Ensure you have the latest version of Python, SUMO, and SUMO Gym installed on your system.

2. **Clone the Repository:**
   - Use Git to clone the repository to your local machine.

3. **Navigate to the Project Directory:**
   - Open your terminal (or command prompt) and navigate to the following directory:
     ```bash
     traffic-management-system\src
     ```

4. **Create a New Conda Environment (if you have Anaconda installed):**
   - Run the following command to create a new environment named `fellowship_env`:
     ```bash
     conda create --name fellowship_env python
     ```

5. **Activate the Conda Environment:**
   - After creating the environment, activate it with the command:
     ```bash
     conda activate fellowship_env
     ```

6. **Install Required Packages:**
   - Install the necessary dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

7. **Train the Model:**
   - Finally, start the training process by executing:
     ```bash
     python train.py
     ```
   - **Note:** The training process may take 1 to 2 days to complete, depending on your system's performance.


## Usage Instructions


# Data Source
The primary data source used for training and evaluation is the simulated traffic data generated by SUMO.
## Traffic Management System Code Structure

```bash
traffic-management-system/
├── docs/                        # Documentation files
├── notebook/                    # Jupyter notebooks
├── src/                         # Source code
│   ├── RL_files/                # Reinforcement learning related files
│   │   ├── action.py            # Action definitions
│   │   ├── reward.py            # Reward definitions
│   │   └── state.py             # State definitions
│   ├── checkpoints/             # Model checkpoints
│   │   ├── ppo_sumo_final_model.zip
│   │   ├── ppo_sumo_model_1000000_steps.zip
│   │   ├── ppo_sumo_model_100000_steps.zip
│   │   ├── ppo_sumo_model_200000_steps.zip
│   │   ├── ppo_sumo_model_300000_steps.zip
│   │   ├── ppo_sumo_model_400000_steps.zip
│   │   ├── ppo_sumo_model_500000_steps.zip
│   │   ├── ppo_sumo_model_600000_steps.zip
│   │   ├── ppo_sumo_model_700000_steps.zip
│   │   ├── ppo_sumo_model_800000_steps.zip
│   │   ├── ppo_sumo_model_900000_steps.zip
│   ├── logs/                    # Logs directory
│   │   ├── best_model/          # Best model logs
│   │   │   └── best_model.zip
│   │   ├── results/             # Evaluation results
│   │   │   ├── ep_lengths.csv
│   │   │   ├── evaluations.npz
│   │   │   └── results.csv
│   ├── sumo_files/              # SUMO simulation files
│   │   ├── Other_files/         # Additional SUMO files
│   │   │   ├── osm.poly.xml
│   │   │   ├── osm.view.xml
│   │   │   ├── osm_bbox.osm.xml
│   │   │   ├── osm_ptlines.xml
│   │   │   ├── osm_stops.add.xml
│   │   │   ├── stopinfos.xml
│   │   │   ├── trips.trips.xml
│   │   │   └── vehroutes.xml
│   │   ├── Junction.png
│   │   ├── osm.bus.trips.xml
│   │   ├── osm.motorcycle.trips.xml
│   │   ├── osm.net.xml
│   │   ├── osm.passenger.trips.xml
│   │   ├── osm.sumocfg
│   │   ├── osm.truck.trips.xml
│   │   └── osm_pt.rou.xml
│   ├── tensorboard_logs/        # TensorBoard logs
│   │   └── PPO_Sumo_Training_1/
│   │       └── events.out.tfevents.1728016919.Legion.9004.0
│   ├── __init__.py
│   ├── inspect_evaluations.py   # Script to inspect evaluations
│   ├── predict.py               # Prediction script
│   ├── predict_result.txt       # Prediction results
│   ├── sumo_env.py              # SUMO environment script
│   └── train.py                 # Training script
├── tests/                       # Test files
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile
├── README.md
├── pyproject.toml
└── requirements.in
```
## Artifacts Location

# Results
## Metrics Used
## Evaluation Results
