

# main class file
# dedicated dirctory fms
# 1.create file
# 2.update file
# 3.read all files
# 4.delete files

import os

class FileSystem:

    def __init__(self):
        self.folder = "FMS"

        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

    # 1. Create File
    def create_file(self):
        file_name = input("Enter file name: ")
        data = input("Enter file content: ")

        with open(os.path.join(self.folder, file_name), "w") as file:
            file.write(data)

        print("File Created Successfully.")

    # 2. Update File
    def update_file(self):
        file_name = input("Enter file name: ")
        data = input("Enter new content: ")

        with open(os.path.join(self.folder, file_name), "a") as file:
            file.write("\n" + data)

        print("File Updated Successfully.")

    # 3. Read All Files
    def read_all_files(self):
        files = os.listdir(self.folder)

        if not files:
            print("No files found.")
            return

        for file in files:
            print(file)

    # 4. Delete File
    def delete_file(self):
        file_name = input("Enter file name: ")

        path = os.path.join(self.folder, file_name)

        if os.path.exists(path):
            os.remove(path)
            print("File Deleted Successfully.")
        else:
            print("File Not Found.")


obj = FileSystem()

while True:
    print("\n------ File Management System ------")
    print("1. Create File")
    print("2. Update File")
    print("3. Read All Files")
    print("4. Delete File")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.create_file()

    elif choice == 2:
        obj.update_file()

    elif choice == 3:
        obj.read_all_files()

    elif choice == 4:
        obj.delete_file()

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        


