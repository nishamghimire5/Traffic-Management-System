import traci

# Constants for actions
ACTION_STAY = 0
ACTION_NEXT = 1
ACTION_PREVIOUS = 2

def apply_action(tl_id, action):
    """
    Applies the action to the traffic light (tl_id).
    
    Args:
        tl_id (str): Traffic light ID.
        action (int): Action to apply. 
                      0 - Stay in the current phase
                      1 - Move to the next phase
                      2 - Move to the previous phase
                      Any other integer - Set to a specific phase.
    """
    # Get current phase and number of phases
    current_phase = traci.trafficlight.getPhase(tl_id)
    num_phases = len(traci.trafficlight.getCompleteRedYellowGreenDefinition(tl_id)[0].phases)
    
    # Validate the action input
    if action == ACTION_STAY:
        # Stay in the current phase
        traci.trafficlight.setPhase(tl_id, current_phase)
    elif action == ACTION_NEXT:
        # Move to the next phase
        next_phase = (current_phase + 1) % num_phases
        traci.trafficlight.setPhase(tl_id, next_phase)
    elif action == ACTION_PREVIOUS:
        # Move to the previous phase
        prev_phase = (current_phase - 1) % num_phases
        traci.trafficlight.setPhase(tl_id, prev_phase)
    elif 0 <= action < num_phases:
        # Set to a specific phase
        traci.trafficlight.setPhase(tl_id, action)
    else:
        raise ValueError(f"Invalid action: {action}. Must be one of {list(range(num_phases))} or {ACTION_STAY}, {ACTION_NEXT}, {ACTION_PREVIOUS}.")

