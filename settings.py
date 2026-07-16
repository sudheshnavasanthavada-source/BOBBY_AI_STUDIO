# =====================================
# BOBBY AI STUDIO v2.6
# Settings & Customization Module
# =====================================

import json
import os


SETTINGS_FILE = "data/settings.json"


def load_settings():

    try:
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)

    except:
        return {
            "creator": "BOBBY",
            "studio_name": "BOBBY AI STUDIO",
            "version": "v2.6"
        }


def save_settings(settings):

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def view_settings():

    print("\n--- CURRENT SETTINGS ---")

    settings = load_settings()

    for key, value in settings.items():
        print(key, ":", value)


def change_creator():

    settings = load_settings()

    name = input("Enter creator name: ")

    settings["creator"] = name

    save_settings(settings)

    print("✅ Creator name updated!")


def change_studio_name():

    settings = load_settings()

    name = input("Enter studio name: ")

    settings["studio_name"] = name

    save_settings(settings)

    print("✅ Studio name updated!")


def settings_menu():

    while True:

        print("\n============================")
        print("     SETTINGS v2.6")
        print("============================")
        print("1. View Settings")
        print("2. Change Creator Name")
        print("3. Change Studio Name")
        print("4. Back to Main Menu")
        print("============================")

        choice = input("Choose option: ")

        if choice == "1":
            view_settings()

        elif choice == "2":
            change_creator()

        elif choice == "3":
            change_studio_name()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")