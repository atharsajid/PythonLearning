from textual.app import App, ComposeResult
from textual.screen import Screen
from screens.main_menu_screens import MainMenu


class ToDoApp(App):
    CSS_PATH = "style.tcss"

    def on_mount(self):
        self.push_screen(MainMenu())


if __name__ == "__main__":
    ToDoApp().run()