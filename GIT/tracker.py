import data
from collections import Counter
def add_workout():
workout_type = input("Enter workout type (e.g., Running, Yoga,
Weights): ").strip().title()
try:
duration = int(input("Enter duration (in minutes): "))
if duration <= 0:
print("Duration must be positive.")
return
except ValueError:
print("Invalid input. Duration must be a number.")
return
data.workout_types.append(workout_type)
data.durations.append(duration)
print(f"Added: {workout_type} - {duration} minutes")
def view_all_workouts():
if not data.workout_types:
print("No workouts logged yet.")
return
print("\n=== All Workouts ===")
for i, (wtype, duration) in enumerate(zip(data.workout_types,
data.durations), start=1):
print(f"{i}. {wtype} - {duration} minutes")
def view_summary():
if not data.workout_types:
print("No workouts to summarize.")
return
total_time = sum(data.durations)
num_workouts = len(data.durations)
avg_duration = total_time / num_workouts
most_common_type = Counter(data.workout_types).most_common(1)[0][0]
print("\n=== Workout Summary ===")
print(f"Total workouts: {num_workouts}")
print(f"Total time spent: {total_time} minutes")
print(f"Average duration: {avg_duration:.2f} minutes")print(f"Most frequent workout: {most_common_type}")
