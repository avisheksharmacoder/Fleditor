import flet as ft


# We define the UI Controls for the code editor UI stack.
editor_ui = [
    ft.TextField(
        value="Your code editor",
        text_size=20,
        multiline=True,
        max_lines=1000,
        min_lines=20,
        hint_text="""
        print("Lide IDE")
        """,
        border_color=ft.Colors.TRANSPARENT,
        content_padding=ft.padding.all(5),
        autofocus=True,
        filled=False,
        expand=True
    ),
]

