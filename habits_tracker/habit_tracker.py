import json
import flet as ft
import habit_tracker_actions as actions

def main(page: ft.Page):
    page.title = "Habit Tracker"

    # shows the existing habits
    actions.view_habits()

    habits_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=ft.padding.all(10),
        controls=[
            ft.ListTile(
                title=ft.Text(habit),
                trailing=ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.DONE,
                            on_click=lambda e: actions.mark_habit_done(habit),
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e: actions.delete_habit(habit),
                        ),
                    ]
                ),
            )
            for habit in actions.habits
        ],
    )

    page.add(habits_list)

ft.app(target=main)
