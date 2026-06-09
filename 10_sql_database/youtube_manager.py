import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL,
            url TEXT          
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos") #Get all items from videos table and hold it on Cursor Object
    print("-"*50)
    for row in cursor.fetchall():
        id, name, time, url = row
        print(f"{id}. Name: {name}, Duration: {time}\nURL: {url}\n")    
    print("-"*50)


def add_video(name, time, url):
    cursor.execute("INSERT INTO videos (name, time, url) VALUES(?, ?, ?)", (name, time, url))
    conn.commit()

def update_video(id, name, time, url):
    cursor.execute("UPDATE videos SET name = ?, time = ?, url = ? WHERE id = ?", (name, time, url, id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()

def main():
    while True:
        print("\n----YOUTUBE MANAGER WITH DB----")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit The App")

        choice = input("Enter your choice: \n")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: \n")
            time = input("Enter the video time: \n")
            url = input("Enter the video url: \n")
            add_video(name, time, url)

        elif choice == "3":
            id = input("Enter Video ID to Update: \n")
            name = input("Enter the video name: \n")
            time = input("Enter the video time: \n")
            url = input("Enter the video url: \n")
            update_video(id, name, time, url)

        elif choice == "4":
            id = input("Enter Video ID to Delete: \n")
            delete_video(id)

        elif choice == "5":
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()