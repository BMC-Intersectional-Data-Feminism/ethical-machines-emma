import urban_planning 

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def student_algorithm(option1, option2):
    high_priority_pedestrian = ['Child', 'Elderly person', 'Person using wheelchair or crutches']
    low_priority_morals = ['Speeding', 'Wrong lane']
    avoid_entities = ['Autonomous delivery robot', 'Street-cleaning robot', 'Large wild animal such as a deer']

    def score(option):
        entity, moral = option
        score = 0

        if entity.startswith('Pedestrian'):
            score += 3
            if any(priority in moral for priority in high_priority_pedestrian):
                score += 2
        if moral in low_priority_morals:
            score -= 2
        if entity in avoid_entities:
            score -= 3
        if 'Following speed limit' in moral:
            score += 1

        return score

    score1 = score(option1)
    score2 = score(option2)

    if score1 > score2:
        return option1, option2
    else:
        return option2, option1

    print('Write your own algorithm here!')

# Function to run the simulation using a given algorithm
# Run the activity
# urban_planning.run_activity()

# Run the activity using the example algorithm
#print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = always_pick_non_vehicle)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")
