from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")

db = client["ytmanager"]
video_collection = db["videos"]
print(video_collection)

def list_all_videos():
    video_list = video_collection.find()
    for index, video in enumerate(video_list, start=1):
        print(f"\n#{index} \nID: {video["_id"]}, \nName: {video["name"]}, Time: {video["time"]}")

def add_video(name, time):
    video_collection.insert_one({
        "name": name,
        "time": time
    })
    print("✅ Video Added Successfully")

def update_video(id, name, time):
    print("VIDEO ID:", id)
    video_collection.update_one({"_id": ObjectId(id)}, {"$set": {
        "name": name,
        "time": time
    }})
    print("✅ Video Updated Successfully")

def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})
    print("✅ Video Deleted Successfully")



def main():
    while True:
        print("\n----YOUTUBE MANAGER WITH MongoDB----")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit The App")

        choice = input("Enter your choice: \n")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter the Video Name: \n")
                time = input("Enter the Video Time: \n")
                add_video(name, time)
            case "3":
                id = input("Enter the Video ID: \n")
                name = input("Enter the Video Name: \n")
                time = input("Enter the Video Time: \n")
                update_video(id, name, time)
            case "4":
                id = input("Enter the Video ID: \n")
                delete_video(id)
            case "5":
                print("Exiting the App!")
                break
            case _:
                print("Invalid Choice")



if __name__ == "__main__":
    main()