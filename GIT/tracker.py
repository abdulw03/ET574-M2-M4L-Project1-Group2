import data
from collections import Counter
import csv

CSV_FILE = '../issue_tracker.csv'

def add_workout():
    workout_type = input("Enter workout type (e.g., Running, Yoga, Weights): ").strip().title()
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

    # Save to CSV file
    try:
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([workout_type, duration])
    except Exception as e:
        print(f"Error saving to file: {e}")
def view_all_workouts():
    if not data.workout_types:
        print("No workouts logged yet.")
        return
    print("\n=== All Workouts ===")
    for i, (wtype, duration) in enumerate(zip(data.workout_types, data.durations), start=1):
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
    print(f"Average duration: {avg_duration:.2f} minutes")
    print(f"Most frequent workout: {most_common_type}")

# Simple menu loop to run the tracker interactively
def load_workouts():
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    data.workout_types.append(row[0])
                    try:
                        data.durations.append(int(row[1]))
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading file: {e}")

if __name__ == "__main__":
    load_workouts()
    while True:
        print("\n1. Add workout")
        print("2. View all workouts")
        print("3. View summary")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_workout()
        elif choice == "2":
            view_all_workouts()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
