import numpy as np
import traci

def get_state():
    """
    Retrieves the state of the environment, including traffic light phases,
    vehicle density at intersections, waiting times, and average speeds.
    
    Returns:
        state (np.array): A flattened array representing the state.
    """
    # Initialize lists to store state variables
    traffic_light_phases = []
    vehicle_densities = []
    waiting_times = []
    average_speeds = []

    # Get the list of traffic lights in the simulation
    traffic_light_ids = traci.trafficlight.getIDList()

    # Variable to track total lanes controlled by all traffic lights
    total_lanes = 0

    for tl_id in traffic_light_ids:
        # Traffic light phase
        current_phase = traci.trafficlight.getPhase(tl_id)
        traffic_light_phases.append(current_phase)

        # Vehicle density and average speed at lanes controlled by the traffic light
        lanes = traci.trafficlight.getControlledLanes(tl_id)
        total_lanes += len(lanes)
        vehicle_density = 0
        waiting_time = 0
        total_speed = 0
        
        for lane in lanes:
            # Number of vehicles on the lane
            vehicle_count = traci.lane.getLastStepVehicleNumber(lane)
            vehicle_density += vehicle_count
            
            # Total waiting time on the lane
            waiting_time += traci.lane.getWaitingTime(lane)
            
            # Calculate average speed
            total_speed += traci.lane.getLastStepMeanSpeed(lane) * vehicle_count  # Weighted by number of vehicles

        vehicle_densities.append(vehicle_density)
        waiting_times.append(waiting_time)
        average_speeds.append(total_speed / max(1, vehicle_density))  # Prevent division by zero

    # Convert lists to arrays and normalize them
    traffic_light_phases = np.array(traffic_light_phases)
    vehicle_densities = np.array(vehicle_densities)
    waiting_times = np.array(waiting_times)
    average_speeds = np.array(average_speeds)

    # Normalize the values
    traffic_light_phases = traffic_light_phases / np.max(traffic_light_phases) if np.max(traffic_light_phases) > 0 else traffic_light_phases
    vehicle_densities = vehicle_densities / np.max(vehicle_densities) if np.max(vehicle_densities) > 0 else vehicle_densities
    waiting_times = waiting_times / np.max(waiting_times) if np.max(waiting_times) > 0 else waiting_times
    average_speeds = average_speeds / np.max(average_speeds) if np.max(average_speeds) > 0 else average_speeds

    # Concatenate all state variables into a single state vector
    state = np.concatenate([traffic_light_phases, vehicle_densities, waiting_times, average_speeds])

    # Dynamically compute expected size based on traffic lights and lanes
    num_traffic_lights = len(traffic_light_ids)
    expected_size = num_traffic_lights + total_lanes * 3  # Phases + (density, waiting time, speed for each lane)

    # Ensure the state has the correct size
    if state.size < expected_size:
        state = np.pad(state, (0, expected_size - state.size), 'constant')
    elif state.size > expected_size:
        state = state[:expected_size]

    return state
