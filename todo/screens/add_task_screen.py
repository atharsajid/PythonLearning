from shared_imports import *

class AddTaskScreen(BaseView):
    def __init__(self):
        super().__init__(Vertical(
            Label("Enter Your Task"),
            Input(id="input"),
            Button("Create", id="create")
        ))
    
    def on_button_pressed(self, event: Button.Pressed):
        text = self.query_one("#input", Input).value
        if text:
            try:
                ToDoRepository.create_todo(text)
                self.notify("Task Created Successfully", severity = "information")
                self.app.pop_screen()
            except Exception as e:
                self.notify(str(e), severity="error")
                print(str(e))
            