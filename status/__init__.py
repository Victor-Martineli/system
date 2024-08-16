import flet as ft

def main(page: ft.Page):
    page.title = "Status"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    status_card = ft.Card(
        content=ft.Column(
            [
                ft.Text("STATUS", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=24)),
                ft.Divider(),
                ft.Row(
                    [
                        ft.Text("NAME: SUNG JIN-WOO", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.Container(
                            width=100,
                            content=ft.Text("LEVEL: 39", style=ft.TextStyle(weight=ft.FontWeight.BOLD), text_align=ft.TextAlign.RIGHT),
                        ),
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("JOB: NONE", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.Container(
                            width=100,
                            content=ft.Text("FATIGUE: 0", style=ft.TextStyle(weight=ft.FontWeight.BOLD), text_align=ft.TextAlign.RIGHT),
                        ),
                    ]
                ),
                ft.Text("TITLE: WOLF SLAYER", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.Row(
                    [
                        ft.Text("HP: 7229", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.ProgressBar(value=0.9, color=ft.colors.RED, width=200),
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("MP: 638", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.ProgressBar(value=0.6, color=ft.colors.BLUE, width=200),
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    [
                        ft.Text("STRENGTH: 97", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        
                        ft.Container(
                            width=100,
                            content=ft.Text("VITALITY: 59", style=ft.TextStyle(weight=ft.FontWeight.BOLD), text_align=ft.TextAlign.RIGHT),
                        ),
                        
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("AGILITY: 97", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.Container(
                            width=100,
                            content=ft.Text("INTELLIGENCE: 51", style=ft.TextStyle(weight=ft.FontWeight.BOLD), text_align=ft.TextAlign.RIGHT),
                        ),
                        
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("SENSE: 81", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    [
                        ft.Text("PHYSICAL DAMAGE REDUCTION: 20%", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.ElevatedButton(
                            on_click=lambda e: print("Activating"),
                            text=ft.Text("ACTIVATING", style=ft.TextStyle(color=ft.colors.GREEN)),
                        ),
                    ]
                ),
                ft.Divider(),
                ft.Text("REMAINING POINTS: 0", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ]
        ),
    )

    page.add(status_card)

ft.app(target=main)
