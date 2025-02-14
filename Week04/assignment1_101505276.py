# Author: Kevin George Buhain
# Assignment: #1

gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # float
highest_reps = 25 # integer
membership_active = True # boolean


# Dictionary with tuples having int values for 
workout_stats = {
    "Kevin":(30, 60, 40),
    "Jaira": (34, 50, 23),
    "Rozeluxe": (15,20,25),
    "Alex": (60,60,60)
} 

workout_total = {} # workout total dictionary
workout_list = [] # nested list

for key, values in workout_stats.items():
    temp = [] # temporary list
    total = 0 # integer for total minutes of exercise
    for value in values:
        temp.append(value)
        total = total + value
    new_key = key + "_Total"
    workout_list.append(temp) # appened each values of exercise to of each friend
    workout_total[new_key] = total # append the total exercise time for each friend to the dictionary

# Slice the workout_list to extract and print specific workout minutes
# Yoga and running for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running Minutes for all friends:", yoga_running)

# Weightlifting minutes for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for the last two friends:", weightlifting_last_two)

# check for friends with more than 120minutes of workout
for name, values in workout_stats.items():
    if sum(values) >= 120:
        print(f"Great job staying active, {name}!")
        
# Allow the user to input a friend's name
friend_name = input("Please enter a friend's name: ")
if friend_name in workout_stats:
    workouts = workout_stats[friend_name]
    total_minutes = workout_total[f"{friend_name}_Total"]
    print(f"{friend_name}'s workout minutes: {workouts}")
    print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

temp_string_highest = "" # string holder for max workout of friend
temp_string_lowest = "" # string holder for min workout of friend
high = 0 # highest minutes
low = 0 # lowest minutes

# find the friend with the highest and lowest workout minutes
for key, value in workout_total.items():
    if temp_string_highest == "" and temp_string_lowest == "":
        # set initial values in the first iteration of the loop
        high = value
        low = value
        temp_string_highest = f"Friend with the highest workout is {key.replace('_Total', '')}: {value} minutes"
        temp_string_lowest = f"Friend with the lowest workout is{key.replace('_Total', '')}: {value} minutes"
    elif high < value:
        # validate highest value for each iteration
        high = value
        temp_string_highest = f"Friend with the highest workout is {key.replace('_Total', '')}: {value} minutes"
    elif low > value:
        # validate lowest value for each iteration
        low = value
        temp_string_lowest = f"Friend with the lowest workout is{key.replace('_Total', '')}: {value} minutes"

# print the highest and lowest friends and their minutes
print(temp_string_highest)
print(temp_string_lowest)