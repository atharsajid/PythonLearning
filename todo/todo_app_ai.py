from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import (
    Header,
    Footer,
    ListView,
    ListItem,
    Label,
    Input,
    Button,
    DataTable
)
from textual.containers import Vertical


class TodoStore:
    todos = [
        "Learn Textual",
        "Build Todo App",
    ]


# ==========================
# Main Menu
# ==========================

class MainMenu(Screen):

    def compose(self) -> ComposeResult:
        yield Header()

        yield ListView(
            ListItem(Label("View Tasks")),
            ListItem(Label("Add Task")),
            ListItem(Label("Update Task")),
            ListItem(Label("Delete Task")),
            ListItem(Label("Exit")),
            id="menu",
        )

        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected):

        match event.list_view.index:

            case 0:
                self.app.push_screen(TaskListScreen())

            case 1:
                self.app.push_screen(AddTaskScreen())

            case 2:
                self.app.push_screen(UpdateTaskScreen())

            case 3:
                self.app.push_screen(DeleteTaskScreen())

            case 4:
                self.app.exit()


# ==========================
# View Tasks
# ==========================

class TaskListScreen(Screen):

    BINDINGS = [
        ("escape", "back", "Back"),
    ]

    def compose(self) -> ComposeResult:

        yield Header()
        yield DataTable()

        # tasks = ListView()

        # for task in TodoStore.todos:
        #     tasks.append(ListItem(Label(task)))

        # yield tasks

        yield Footer()

    def action_back(self):
        self.app.pop_screen()

    def _on_mount(self, event):
        super()._on_mount(event)
        table = self.query_one(DataTable)
        table.cursor_type = "none"
        table.add_columns(("ID", "id"), ("Tasks", "task"))
        table.add_rows(enumerate(TodoStore.todos, start = 1))


# ==========================
# Add Task
# ==========================

class AddTaskScreen(Screen):

    BINDINGS = [
        ("escape", "back", "Back"),
    ]

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Enter Task")
            yield Input(id="task_input")
            yield Button("Save", id="save")

    def on_button_pressed(self, event: Button.Pressed):

        text = self.query_one("#task_input", Input).value

        if text:
            TodoStore.todos.append(text)

        self.app.pop_screen()

    def action_back(self):
        self.app.pop_screen()


# ==========================
# Update Task
# ==========================

class UpdateTaskScreen(Screen):

    BINDINGS = [
        ("escape", "back", "Back"),
    ]

    selected_index = None

    def compose(self):

        yield Label("Select task to update")
        self.list_view = ListView(
            *[
                ListItem(Label(task))
                for task in TodoStore.todos
            ]
        )

        yield self.list_view
        
        yield Input(
            placeholder="New title",
            id="new_title",
        )

        yield Button("Update")



    def on_button_pressed(self, event):

        if self.list_view.index is None:
            return

        new_title = self.query_one(
            "#new_title",
            Input,
        ).value

        TodoStore.todos[self.list_view.index] = new_title

        self.app.pop_screen()

    def action_back(self):
        self.app.pop_screen()



# ==========================
# Delete Task
# ==========================

class DeleteTaskScreen(Screen):

    BINDINGS = [
        ("escape", "back", "Back"),
    ]

    def compose(self):

        self.list_view = ListView()

        for task in TodoStore.todos:
            self.list_view.append(
                ListItem(Label(task))
            )

        yield Label("Select task to delete")
        yield self.list_view
        yield Button("Delete")

    def on_button_pressed(self, event):

        if self.list_view.index is None:
            return

        TodoStore.todos.pop(
            self.list_view.index
        )

        self.app.pop_screen()

    def action_back(self):
        self.app.pop_screen()


# ==========================
# App
# ==========================

class TodoApp(App):

    CSS = """
    Screen {
        align: center middle;
    }

    ListView {
        width: 60;
        height: 15;
        border: round cyan;
    }

    Input {
        width: 60;
    }

    Button {
        width: 20;
        margin-top: 1;
    }
    """

    def on_mount(self):
        self.push_screen(MainMenu())


if __name__ == "__main__":
    TodoApp().run()