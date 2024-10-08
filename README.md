# Traffic Management System using SUMO and Reinforcement Learning

## Introduction
This project demonstrates a Traffic Management System using SUMO (Simulation of Urban MObility) integrated with Reinforcement Learning (RL) environments. The system is designed to optimize traffic flow and reduce congestion at intersections using advanced RL techniques.
## Goals
Our goal is to design and implement an adaptive traffic signal control system by creating a simulated traffic environment and training a reinforcement learning (RL) model. The goal is to optimize traffic flow and reduce congestion at intersections, leveraging the capabilities of RL algorithms for real-time decision-making within a simulation environment like SUMO (Simulation of Urban MObility).
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
The project has been divided into following componenets: 
<br>
1. SUMO Environment Setup
Traffic Simulation: While SUMO itself is not an AI component, it provides a simulated environment that can be used to train AI models. The traffic scenarios created can serve as a dataset for reinforcement learning.
2. RL Model Design
Objective Definition: Defining the objectives (like minimizing waiting time or congestion) is crucial for the reinforcement learning model. This is where AI concepts are applied to determine what the model should aim to optimize.
Algorithm Selection: Choosing a reinforcement learning algorithm (like PPO, DQN, etc.) involves understanding various AI techniques that affect learning efficiency and model performance.
Architecture Design: Designing the architecture for the RL model (e.g., neural networks) is a key AI component that determines how the model processes input and makes decisions.
3. Integration with OpenAI Gym
Gym Environment Development: Creating a Gym environment tailored for SUMO involves applying AI principles to ensure that the environment correctly simulates the dynamics of the traffic system and allows the RL model to learn effectively.
Model Integration: Implementing the RL model within the Gym framework is an AI-related task that connects the learning algorithm with the simulation, enabling interaction and training.
4. Model Training
Reinforcement Learning Training: This is a core AI component where the RL model learns from the traffic simulation data provided by SUMO. It involves iteratively adjusting the model's parameters based on feedback from the environment.
Performance Optimization: Fine-tuning the model to improve its decision-making capabilities is another AI component, utilizing techniques like hyperparameter tuning or training enhancements.

<img src="https://github.com/user-attachments/assets/dc44fd51-00bc-4226-8976-f96c4d0b42d1" alt="Architecture Diagram" width="340"/>

<br />

<img src="https://github.com/user-attachments/assets/22570682-a7f8-4775-b7fb-e9adffb5561c" alt="Architecture Drawio" width="500"/>






# Status
## Known Issue
## High Level Next Steps


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
## Code Structure
## Artifacts Location

# Results
## Metrics Used
## Evaluation Results
