from shared_imports import *

class UpdateTaskScreen(BaseView):
    def __init__(self):
        super().__init__(Vertical(
            Label("Select Your Task"),
            
            Input(id="input"),
            Button("Update", id="update")
        ))
    
    def on_button_pressed(self, event: Button.Pressed):
        text = self.query_one("#input", Input).value
        if text:
            pass

        self.app.pop_screen()