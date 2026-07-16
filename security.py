# =====================================
# BOBBY AI STUDIO v2.9
# Security & Backup System
# =====================================

import os
import shutil
from datetime import datetime


BACKUP_FOLDER = "data/backups"


def create_backup_folder():

    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)



def create_backup():

    create_backup_folder()

    backup_name = "backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_path = os.path.join(
        BACKUP_FOLDER,
        backup_name
    )


    os.makedirs(backup_path)


    for item in os.listdir("data"):

        if item == "backups":
            continue


        source = os.path.join("data", item)

        destination = os.path.join(
            backup_path,
            item
        )


        if os.path.isdir(source):

            shutil.copytree(source, destination)

        else:

            shutil.copy2(source, destination)


    print("\n✅ Backup Created Successfully!")
    print("Backup:", backup_name)



def view_backups():

    create_backup_folder()

    backups = os.listdir(BACKUP_FOLDER)


    print("\n🔐 BACKUP HISTORY")


    if backups:

        for backup in backups:
            print("-", backup)

    else:

        print("No backups found.")



def security_check():

    print("\n🔍 SYSTEM SECURITY CHECK")


    files = [
        "stories.py",
        "prompts.py",
        "memory.py",
        "notes.py",
        "files.py",
        "workflow.py",
        "settings.py"
    ]


    for file in files:

        if os.path.exists(file):

            print("✅", file)

        else:

            print("❌ Missing:", file)



def security_menu():

    while True:

        print("\n============================")
        print("     SECURITY & BACKUP")
        print("============================")

        print("1. Create Backup")
        print("2. View Backups")
        print("3. Security Check")
        print("4. Back")

        print("============================")


        choice = input("Choose option: ")


        if choice == "1":

            create_backup()


        elif choice == "2":

            view_backups()


        elif choice == "3":

            security_check()


        elif choice == "4":

            break


        else:

            print("Invalid option!")