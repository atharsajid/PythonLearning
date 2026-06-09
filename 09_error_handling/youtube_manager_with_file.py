from loader import loading
from separator import separator
from menu_picker import menu_picker
import json

fileName = "youtube.txt"

def load_data():
    try:
        with open(fileName, "r") as file:
            return json.load(file) #It will load file and convert to json
    except FileNotFoundError:
        return []

def save_data(videos):
    with open(fileName, "w") as file:
        json.dump(videos, file) #It will save json on file


def video_detail(video):
    return f"Name: {video["name"]}, Duration: {video["time"]}\nURL: {video["url"]}"


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video_detail(video)} \n")


def add_video(videos):
    name = input("Enter Video Name: \n")
    time = input("Enter Time Duration: \n")
    url = input("Enter Video URL: \n")
    
    videos.append({
        "name": name if name else "-",
        "time": time if time else "-",
        "url": url if url else "-"
    })
    save_data(videos)
    loading("Adding, Please Wait")
    print("✅ Video Added Successfully...")


def update_video(videos):
    index = menu_picker(videos)
    print(f"Selected: {video_detail(videos[index])}")
    
    
    name = input("Enter Video Name: \n")
    time = input("Enter Time Duration: \n")
    url = input("Enter Video URL: \n")

    if name:
        videos[index]["name"] = name
    if time:
        videos[index]["time"] = time
    if url:
        videos[index]["url"] = url

    save_data(videos)
    loading("Updating...")
    print("✅ Video Updated Successfully...")


def delete_video(videos):
    index = menu_picker(videos)
    del videos[index]
    save_data(videos)
    loading("Deleting...")
    print("✅ Video Deleted Successfully...")
    
def main():
    videos = load_data()
    print("\n----YOUTUBE MANAGER----")
    while True:
        separator(23)
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit The App")

        while True:
            userInput = input()
            try:
                userInput = int(userInput)
                if 6 > userInput > 0:
                    break
                else:
                    print("You have entered incorrect value, Please Select from 1 to 5")
            except:
                print("You have entered incorrect value, Please Select from 1 to 5")

        loading("Please Wait...")
        video_length = len(videos)
        match userInput:
            case 1:
                if video_length > 0:
                    print("Here is your Youtube List")
                    separator()
                    list_all_videos(videos)
                    separator()
                    loading("", 3)
                else:
                    print("You haven't added any videos yet")
                    loading("", 3)
            case 2:
                separator()
                print("Add a video")
                separator()
                add_video(videos)
                    
            case 3:
                separator()
                print("Update a video")
                separator()
                if video_length > 0:
                    update_video(videos)
                else:
                    print("You haven't added any videos yet")
                
                    
            case 4:
                separator()
                print("Delete a video")
                separator()
                if video_length > 0:
                    delete_video(videos)
                else:
                    print("You haven't added any videos yet")
                
            case 5:
                print("Exiting The App...")
            
            case _: #Default
                print("Invalid Choice")
        
        loading()
        while True:
            try:
                print("Select Option:")
                print("0. Go Back to Main Menu")
                print("5. Exit the Application")
                userInput = int(input())
                if userInput != 5 and userInput != 0:
                    print("You have entered incorrect value, Please Select from 1 to 5")
                else:
                    break
            except:
                print("You have entered incorrect value, Please Select from 1 to 5")
        
        match userInput:
            case 5:
                print("Exiting The App...")
                break


if __name__ == "__main__":
    main()
            




