# =====================================
# BOBBY AI STUDIO v2.8
# File Management System
# =====================================

import os


DATA_FOLDER = "data"


def create_file():

    print("\n--- CREATE FILE ---")

    filename = input("Enter file name (without extension): ")

    filepath = os.path.join(DATA_FOLDER, filename + ".txt")


    if os.path.exists(filepath):

        print("❌ File already exists!")


    else:

        with open(filepath, "w") as file:

            file.write("")


        print("✅ File created successfully!")



# 🔥 v2.8 AUTOMATION FUNCTION
def auto_save_project(project_name, content):

    if not os.path.exists(DATA_FOLDER):

        os.makedirs(DATA_FOLDER)


    filepath = os.path.join(
        DATA_FOLDER,
        project_name + ".txt"
    )


    with open(filepath, "w") as file:

        file.write(content)


    print("✅ Automated Project Saved!")



def view_files():

    print("\n--- FILES ---")


    files = os.listdir(DATA_FOLDER)


    if files:

        for file in files:

            print(file)


    else:

        print("No files found.")



def read_file():

    print("\n--- READ FILE ---")


    filename = input("Enter file name (without extension): ")


    filepath = os.path.join(
        DATA_FOLDER,
        filename + ".txt"
    )


    if os.path.exists(filepath):

        with open(filepath, "r") as file:

            print("\nContents:\n")

            print(file.read())


    else:

        print("❌ File not found!")



def delete_file():

    print("\n--- DELETE FILE ---")


    filename = input("Enter file name (without extension): ")


    filepath = os.path.join(
        DATA_FOLDER,
        filename + ".txt"
    )


    if os.path.exists(filepath):

        os.remove(filepath)

        print("✅ File deleted successfully!")


    else:

        print("❌ File not found!")



def file_menu():

    while True:

        print("\n============================")
        print("    FILE MANAGEMENT")
        print("============================")
        print("1. Create File")
        print("2. View Files")
        print("3. Read File")
        print("4. Delete File")
        print("5. Back")
        print("============================")


        choice = input("Choose option: ")


        if choice == "1":

            create_file()


        elif choice == "2":

            view_files()


        elif choice == "3":

            read_file()


        elif choice == "4":

            delete_file()


        elif choice == "5":

            break


        else:

            print("Invalid option!")