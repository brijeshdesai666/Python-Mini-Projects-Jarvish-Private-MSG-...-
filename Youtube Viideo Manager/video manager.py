import json

file = 'youtube.txt'


def load_video():
    try:
        with open(file, 'r') as f:
            result = json.load(f)
            return result
    except FileNotFoundError:
        return []


def save_video(videos):
    with open(file, 'w') as f:
        json.dump(videos, f)


def list_video(videos):
    if not videos:
        print("************\nNo any videos available, Please Enter video\n************")
    print("\n\nList of available Videos:")

    for i, obj in enumerate(videos, start=1):
        print(f"{i}. {obj['Name']}, {obj['Time']}")


def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Duration: ")
    videos.append({'Name': name, 'Time': time})
    save_video(videos)


def update_video(videos):
    list_video(videos)
    ind = int(input("Enter video Number for Update: ")) - 1
    if 0 <= ind < len(videos):
        name = input("Enter New video Name: ")
        time = input("Enter New Video duration: ")
        videos[ind] = {'Name':name, 'Time':time}
        save_video(videos)
    else:
        print("\n*********  invalid Index!!  *********\n")


def delete_video(videos):
    list_video(videos)
    ind = int(input("Enter video Number for Delete: ")) - 1
    if 0 <= ind < len(videos):
        del videos[ind]
        save_video(videos)
    else:
        print("\n*********  invalid Index!!  *********\n")


if __name__ == '__main__':
    while True:
        videos = load_video()
        print("\n*****************  Welcome to youtube Video Manager App | Please select choice  *****************")
        print("1. For List out videos")
        print("2. for  Adding video")
        print("3. for Updating video")
        print("4. for Delete video")
        print("0. for Exit")
        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '0':
                break
            case _:
                print("Invalid case")
