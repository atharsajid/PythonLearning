from shared_imports import *

class ListViewScreen(BaseView):
    def __init__(self):
        super().__init__(DataTable())

    def _on_mount(self, event):
        super()._on_mount(event)
        table = self.query_one(DataTable)
        table.cursor_type = "none"
        
        try:
            todo_list = ToDoRepository.fetch_all_tasks()
            table.add_columns(("ID", "id"), ("Tasks", "task"), ("Completed", "isComplete"), ("Updated At"))
            for index, task in enumerate(todo_list, start=1):
                table.add_row(f"{index}", task["title"], task["isComplete"], task["updatedAt"])
        except Exception as e:
            self.notify(str(e),severity="error")
        
    