import requests

base_url = "https://api.freeapi.app/api/v1/"

class ToDoRepository():
    def fetch_all_tasks(query=""):
        url = f'{base_url}todos{f"?query={query}" if query else ""}'
        response = requests.get(url, )
        data = response.json()
        if data["success"] and "data" in data:
            return data["data"]
        else:
            raise Exception("Unable to fetch TODOs")
        

    def create_todo(task: str):
        url = f"{base_url}todos/"
        
        response = requests.post(url,  data = {
            "title": task
        })
        data = response.json()
        if data["success"]:
            return data["data"]
        else:
            raise Exception("Unable to create a todo" + str(data))
