import json
import flet as ft
import habit_tracker_actions as actions

def main(page: ft.Page):
    page.title = "Habit Tracker"

    # Create the ListView outside the main function to keep it in memory
    habits_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=ft.padding.all(10),
    )
    page.add(habits_list)

    # Add habit input and button
    habit_input = ft.TextField(label="New Habit", expand=True)
    add_habit_button = ft.ElevatedButton(
        text="Add Habit",
        on_click=lambda e: add_habit_and_update_list(habit_input.value, habits_list, page),
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[habit_input, add_habit_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        ),
    )

    # Initial update to display existing habits
    update_habits_list(habits_list, page)

    page.update()

def add_habit_and_update_list(habit, habits_list, page):
    """Adds a habit and updates the ListView."""
    actions.add_habit(habit)
    update_habits_list(habits_list, page)

def update_habits_list(habits_list, page):
    """Updates the ListView with the current habits."""
    habits_list.controls = [
        ft.ListTile(
            title=ft.Text(h),
            trailing=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.DONE,
                        on_click=lambda e: mark_habit_done_and_update(h, habits_list, page),
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=lambda e: delete_habit_and_update(h, habits_list, page),
                    ),
                ]
            ),
        )
        for h in actions.habits
    ]
    page.update()

def mark_habit_done_and_update(habit, habits_list, page):
    """Marks a habit as done and updates the ListView."""
    actions.mark_habit_done(habit)
    update_habits_list(habits_list, page)

def delete_habit_and_update(habit, habits_list, page):
    """Deletes a habit and updates the ListView."""
    actions.delete_habit(habit)
    update_habits_list(habits_list, page)

ft.app(target=main)
