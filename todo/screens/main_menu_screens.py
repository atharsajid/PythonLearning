from shared_imports import *
from screens.list_view_screens import ListViewScreen
from screens.add_task_screen import AddTaskScreen


class MainMenu(Screen):
    BINDINGS = [("q", "quit", "Quit"),]
    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(
            "View Task Lists.",
            "Add a new Task.",
            "Update a Task.",
            "Delete a Task.",
            "Quit App")
        yield Footer()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
            match event.option_index:
                case 0:
                    self.app.push_screen(ListViewScreen())
                
                case 1:
                    self.app.push_screen(AddTaskScreen())
                
                case 2:
                    self.app.push_screen(ListViewScreen())
                
                case 3:
                    self.app.push_screen(ListViewScreen())
                case 4:
                    self.app.exit()
                
            

    def action_quit(self):
        self.app.exit()

