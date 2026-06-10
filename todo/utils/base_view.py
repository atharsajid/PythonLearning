from shared_imports import *

class BaseView(Screen):
    BINDINGS = [
        ('escape', 'back', "Back")
    ]


    def __init__(self, *widgets, is_main_view = False):
        super().__init__()
        self.widgets = widgets
        self.is_main_view = is_main_view

    def compose(self)-> ComposeResult:
        yield Header()
        with Vertical(id="content"):
            for widget in self.widgets:
                yield widget
        yield Footer()
    
    def action_back(self):
        if self.is_main_view == False:
            self.app.pop_screen()   
