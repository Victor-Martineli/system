import datetime
import json

habits = {}

def add_habit(habit):
    """adds a new habit to the tracker."""
    if habit not in habits:
        habits[habit] = []
        json.dump(habits, open("habits.json", "w"))
        print(f"Habit '{habit}' added!")

    else:
        print(f"Habit '{habit}' already exists.")

def mark_habit_done(habit):
    """ records that a habit was complet today."""
    if habit in habits:
        today = datetime.date.today().strftime("%Y-%m-%d")  
        habits[habit].append(today)
        print(f" congratulations \nHabit '{habit}' was completed today.")
    else:
        print(f"Habit '{habit}' not found.")

def view_habits():
    """ Displays all habits and their completion history."""
    if habits:
        for habit, dates in habits.items():
            print(f"Habit: {habit}")
            print(f"  Completed on: {dates}")
    else:
        print("No habits added yet.")

def view_habit_progress(habit):
    """Shows the progress of a specific habit."""
    if habit in habits:
        dates = habits[habit]
        print(f"Habit: {habit}")
        print(f"  Completed on: {dates}")
    else:
        print(f"Habit '{habit}' not found.")

