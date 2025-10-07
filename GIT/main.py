from tracker import add_workout, view_workouts, view_summary

def main():
    while True:
        print("\n=== Workout Tracker ===")
        print("1. Add Workout")
        print("2. View All Workouts")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_workout()
        elif choice == '2':
            view_workouts()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()