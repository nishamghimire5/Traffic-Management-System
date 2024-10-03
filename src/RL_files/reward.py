import traci

def get_traffic_light_data(tl_id):
    """
    Collect data for lanes controlled by a traffic light.

    Args:
        tl_id (str): Traffic light ID.
    
    Returns:
        lane_data (dict): Dictionary containing vehicle count, total waiting time, etc.
    """
    lanes = traci.trafficlight.getControlledLanes(tl_id)
    lane_data = {
        'vehicle_count': 0,
        'total_waiting_time': 0
    }

    for lane in lanes:
        # Vehicle count on the lane
        vehicle_count = traci.lane.getLastStepVehicleNumber(lane)
        lane_data['vehicle_count'] += vehicle_count
        
        # Total waiting time for all vehicles
        lane_data['total_waiting_time'] += traci.lane.getWaitingTime(lane)

    return lane_data

def compute_reward(waiting_weight=-0.1, throughput_weight=1.0, congestion_weight=-0.2, 
                   max_expected_waiting_time=150, max_vehicle_count=50):
    traffic_light_ids = traci.trafficlight.getIDList()
    
    total_waiting_time = 0
    total_vehicle_count = 0
    total_congestion_penalty = 0
    
    for tl_id in traffic_light_ids:
        data = get_traffic_light_data(tl_id)
        
        total_waiting_time += data['total_waiting_time']
        total_vehicle_count += data['vehicle_count']
        
        congestion_threshold = 20
        # Adjust congestion penalty more smoothly
        if data['vehicle_count'] > congestion_threshold:
            total_congestion_penalty += (data['vehicle_count'] - congestion_threshold)

    # Normalize the collected data
    normalized_waiting_time = total_waiting_time / max_expected_waiting_time if max_expected_waiting_time > 0 else total_waiting_time
    normalized_vehicle_count = total_vehicle_count / max_vehicle_count if max_vehicle_count > 0 else total_vehicle_count

    # Dynamic waiting weight adjustment
    if total_waiting_time > 0.8 * max_expected_waiting_time:
        waiting_weight *= 2  # Penalize more for high waiting times

    waiting_time_penalty = waiting_weight * normalized_waiting_time
    throughput_reward = throughput_weight * normalized_vehicle_count
    congestion_penalty = congestion_weight * total_congestion_penalty
    
    # Final reward computation
    reward = waiting_time_penalty + throughput_reward + congestion_penalty
    
    return reward
