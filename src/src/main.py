import flet as ft


def main(page: ft.Page):
    # icons browser.
    # https://gallery.flet.dev/icons-browser/

    # Theme mode. DARK Mode is enabled.
    # page.theme_mode = ft.ThemeMode.LIGHT
    page.theme_mode = ft.ThemeMode.DARK

    # we set the initial window height and width.
    page.window.height = 720
    page.window.width = 1280

    # we set the padding of all global controls in the page.
    page.padding = 10

    # we fetch the fonts for Application UI and Code editor.
    page.fonts = {
        "JetBrainsMono": "/fonts/JetBrainsMono-Regular.ttf",
        "QuicksandBold": "/fonts/Quicksand-Bold.ttf",
        "QuicksandMedium": "/fonts/Quicksand-Medium.ttf"
    }

    # we set the main font of the application, in Light and Dark mode.
    page.theme = ft.Theme(font_family="QuicksandMedium")
    page.dark_theme = ft.Theme(font_family="QuicksandMedium")

    # we define the text style for the code editor.
    # we use the Jetbrains mono font for the code editor.
    code_editor_font = ft.TextStyle(font_family="JetBrainsMono")

    # We write the code editor events from here.
    # We perform some tasks when some text is entered into the editor.
    def on_prompt_submit(e):
        pass

    # we define the chat list view reference here.
    chat_list = ft.Ref[ft.ListView]
    user_prompt_input = ft.Ref[ft.TextField()]

    # we define the code editor in the main file since the fonts assigned to the
    # control cannot be assigned in a different file, where the editor is created and
    # imported here.
    code_editor = ft.TextField(
        value=""" print("AI is fine") """,
        text_size=20,
        text_style=code_editor_font,
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
        expand=2
    )

    # we edit the python file name using this text field.
    code_filename = ft.TextField(
        value="filename.py",
        text_size=15,
        height=30,
        hint_text="myapp1.py"
    )

    # this Column contains the code editor text input and the file name text input.
    # the ratio size remains the same as the code editor text input.
    code_editor_file_name_row = ft.Column(
        controls=[code_filename, code_editor],
        expand=2
    )

    # we initialize the chat view here.
    editor_chat_view = ft.Column(
        [
            # we define the header text of this part of the view.
            ft.Text(
                value="Chat with Gemini",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            # we define the container where all the chat interaction will be shown.
            ft.Container(
                content=ft.ListView(
                    ref=chat_list,
                    spacing=10,
                    auto_scroll=True
                ),
                expand=True,
                bgcolor=ft.Colors.GREY_500,
                border_radius=10
            ),

            # we define the input and the send button for the user to use.
            ft.Row(
                [
                    ft.TextField(
                        ref=user_prompt_input,
                        multiline=True,
                        max_lines=3,
                        border_color=ft.Colors.LIGHT_BLUE_100,
                        hint_text="Your prompt",
                        on_submit=on_prompt_submit,
                        expand=True
                    ),
                    ft.IconButton(
                        icon=ft.Icons.SEND,
                        on_click=on_prompt_submit,
                        tooltip="Ask Gemini"
                    )
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        expand=1,
        alignment=ft.MainAxisAlignment.START
    )

    # We initialize the entire Lide IDE Interface, using the left and the right columns.
    # The left column contains the Gemini chat view, where the user communicates with Gemini using a
    # list view.
    #
    # The right column contains the file name editor, the code editor.
    lide_editor_view = ft.Row(
        [
            editor_chat_view,
            ft.VerticalDivider(width=2),
            code_editor_file_name_row
        ],
        expand=True,
        spacing=10,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH
    )

    # This is the Home page view of Lide AI.
    lide_homepage = [
        ft.Text("Welcome to Lide AI IDE", size=30),
        ft.Text("Lide AI is available", size=30),
        ft.Icon(ft.Icons.MARK_CHAT_READ_ROUNDED, size=50, color=ft.Colors.RED_50),
        ft.VerticalDivider(width=5)
    ]

    # We define the final column that contains the lide ai homepage controls.
    lide_ai_view = ft.Column(
        lide_homepage,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    # We define the UI controls for the lide ai settings page.
    settings_controls = [
        ft.Text("App Settings", size=30),
        ft.Switch(label="Notifications"),
        ft.Switch(label="Flash mode"),
        ft.Switch(label="Save chats"),
        ft.Switch(label="Use Local Liquid Models")
    ]

    # We define the final column that contains the lide ai settings page controls.
    settings_view = ft.Column(
        settings_controls,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # we define the indexes of all views, similar to navigation Destinations in flet.
    app_views = {
        0: lide_ai_view,
        1: lide_editor_view,
        2: settings_view,
    }

    # We set the current page content to the 0th view.
    page_content = ft.Column(controls=[app_views[0]], expand=True)

    # we set the title of the page.
    page.title = "NavigationBar Example"

    # we define how the navigation changes when the destination buttons are clicked.
    def view_navigation_change(e) -> None:
        # we need the current index of the navigation bar
        current_index = e.control.selected_index

        # we clear all the current controls.
        page_content.controls.clear()

        # we set new controls, from the app_views {}
        page_content.controls.append(app_views[current_index])

        # once the controls are appended to the page, we call the update method
        # to refresh the view with the new controls.
        page.update()

    # We define the navigation bar and the destinations.
    # We need 3 destinations, one for chat, editor and settings.
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CHAT, label="Lide AI"),
            ft.NavigationBarDestination(icon=ft.Icons.CODE, label="IDE"),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS_SHARP,
                selected_icon=ft.Icons.SETTINGS_SHARP,
                label="Settings",
            ),
        ],
        on_change=view_navigation_change,
        selected_index=0,
    )

    # add the page_content to the main page.
    page.add(page_content)


ft.app(
    main,
    assets_dir="assets"
)
