import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_videos(videos):
    print("\n")
    print("*" * 30)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")
    print("*" * 30)

def add_video(videos):
    name = input("enter the title of the video: ")
    time = input("enter the duration of the video: ")
    videos.append({"name": name, "time": time})
    save_data(videos)
    


def update_video(videos):
    list_videos(videos)
    index = int(input("enter the index of the video you want to update: "))
    if 1 <= index <= len(videos):
        name = input("enter the new title of the video: ")
        time = input("enter the new duration of the video: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data(videos)
    else:
        print("invalid index, please try again")



def delete_video(videos):
    list_videos(videos)
    index = int(input("enter the index of the video you want to delete: "))
    if 1 <= index <= len(videos):
        videos.pop(index - 1)
        save_data(videos)
    else:
        print("invalid index, please try again")


def main():

    videos = load_data() #this will load data from the list and if data is not present it will return an empty list




    while True:
        print("welcome to srijits youtube manager app")
        print("1. list all youtube videos")
        print("2. add single youtube video")
        print("3. update a youtube video details")
        print("4. delete a video")
        print("5. exit")
        choice = input("enter your choice: ")
        print("\n")  
        print(videos)  #this will print the list of videos after every choice, so that user can see the updated list of videos after every operation
        
        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("exiting the app")
                break    
            case _:  #default case
                print("invalid choice, please try again")
                
if __name__ == "__main__":  #this line ensures that the main function is called only when this script is run directly, and not when it is imported as a module in another script.
    main()  #thunder 
    
