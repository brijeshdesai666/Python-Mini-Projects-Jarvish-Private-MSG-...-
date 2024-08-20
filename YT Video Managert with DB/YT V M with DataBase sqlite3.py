import sqlite3

conn = sqlite3.connect('Youtube video MG with DB.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_video():
    cursor.execute('SELECT * FROM videos')
    result = cursor.fetchall()
    if not result:
        print("************\nNo any videos available, Please Enter video\n************")
    else:
        print("\n\nList of available Videos:")
        for row in result:
            print(row)


def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    conn.commit()


def update_video(id, name, time):
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (name, time, id))
    conn.commit()

def delete_video(id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (id,))
    conn.commit()


if __name__ == '__main__':
    while True:
        print("\n*****************  Welcome to youtube Video Manager App With DB | Please select choice  *****************")
        print("1. For List out videos")
        print("2. for  Adding video")
        print("3. for Updating video")
        print("4. for Delete video")
        print("0. for Exit")
        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_video()
            case '2':
                name = input("Enter video name: ")
                time = input('Enter Video duration: ')
                add_video(name, time)
            case '3':
                id = input("Enter id of the video for update: ")
                name = input("Enter new Video name: ")
                time = input("Enter new video duration: ")
                update_video(id,name, time)
            case '4':
                id = input("Enter id the video for delete: ")
                delete_video(id)
            case '0':
                break
            case _:
                print("Invalid case")
    conn.close()