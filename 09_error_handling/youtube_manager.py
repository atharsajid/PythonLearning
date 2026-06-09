import time
from loader import loading
from separator import separator
from menu_picker import menu_picker

videos = []

def list_all_videos(videos):
    for x in range(0, len(videos)):
        print(f"{x + 1}. {videos[x]}")


def add_video(videos):
    while True:
        videoUrl = input("Enter Youtube Video URL: \n")
        if videoUrl:
            break
    
    videos.append(videoUrl)
    loading("Adding, Please Wait")
    print("✅ Video Added Successfully...")


def update_video(videos):
    index = menu_picker(videos)
    while True:
        videoUrl = input("Enter Youtube Video URL: \n")
        if videoUrl:
            break
    videos[index] = videoUrl
    loading("Updating...")
    print("✅ Video Updated Successfully...")


def delete_video(videos):
    index = menu_picker(videos)
    videos[index:index+1] = []
    loading("Deleting...")
    print("✅ Video Deleted Successfully...")
    


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


            
            




