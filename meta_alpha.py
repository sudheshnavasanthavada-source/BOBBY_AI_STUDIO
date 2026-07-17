# ============================================
# BOBBY AI STUDIO v3.4.1
# META ALPHA STUDIO
# ============================================

import json
import os
from datetime import datetime


META_FILE = "data/meta_alpha.json"



# ============================================
# Storage
# ============================================

def setup_meta():

    if not os.path.exists("data"):
        os.makedirs("data")


    if not os.path.exists(META_FILE):

        with open(META_FILE, "w") as file:
            json.dump([], file)



def load_meta():

    setup_meta()

    with open(META_FILE, "r") as file:
        return json.load(file)



def save_meta(data):

    with open(META_FILE, "w") as file:
        json.dump(data, file, indent=4)



# ============================================
# Create Scene
# ============================================

def create_scene():

    print("\n--- CREATE META ALPHA SCENE ---")

    title = input("Scene Title: ")

    idea = input("Scene Idea: ")


    scene = {

        "type": "Scene",
        "title": title,
        "description": idea,
        "date": str(datetime.now())

    }


    data = load_meta()

    data.append(scene)

    save_meta(data)


    print("\n✅ META ALPHA Scene Saved!")



# ============================================
# Create Character
# ============================================

def create_character():

    print("\n--- CREATE CHARACTER ---")


    name = input("Character Name: ")

    role = input("Character Role: ")

    description = input(
        "Character Description: "
    )


    character = {

        "type": "Character",
        "name": name,
        "role": role,
        "description": description,
        "date": str(datetime.now())

    }


    data = load_meta()

    data.append(character)

    save_meta(data)


    print("\n✅ Character Added!")



# ============================================
# View Universe
# ============================================

def view_universe():

    print("\n--- META ALPHA UNIVERSE ---")


    data = load_meta()


    if not data:

        print("No data found.")
        return



    for index, item in enumerate(data):

        print("\n--------------------")

        print("ID:", index)

        print("Type:", item["type"])


        if item["type"] == "Scene":

            print("Title:", item["title"])

            print("Idea:",
                  item["description"])


        else:

            print("Name:",
                  item["name"])

            print("Role:",
                  item["role"])

            print("Description:",
                  item["description"])



# ============================================
# Edit Data
# ============================================

def edit_data():

    data = load_meta()


    if not data:

        print("No data available.")
        return



    view_universe()


    choice = input(
        "\nEnter ID to edit: "
    )


    try:

        index = int(choice)

        item = data[index]


        print("\nEditing:",
              item["type"])



        if item["type"] == "Character":


            item["role"] = input(
                "New Role: "
            )


            item["description"] = input(
                "New Description: "
            )


        else:


            item["title"] = input(
                "New Title: "
            )


            item["description"] = input(
                "New Idea: "
            )



        item["date"] = str(datetime.now())


        save_meta(data)


        print("\n✅ Updated Successfully!")



    except:

        print("\n❌ Invalid ID!")



# ============================================
# Delete Data
# ============================================

def delete_data():

    data = load_meta()


    view_universe()


    choice = input(
        "\nEnter ID to delete: "
    )


    try:

        index = int(choice)

        removed = data.pop(index)

        save_meta(data)


        print(
            "\n✅ Deleted:",
            removed["type"]
        )


    except:

        print("\n❌ Invalid ID!")



# ============================================
# META ALPHA MENU
# ============================================

def meta_alpha_menu():


    while True:


        print("\n============================")
        print("   🌌 META ALPHA STUDIO v3.4.1")
        print("============================")

        print("1. Create Scene")
        print("2. Create Character")
        print("3. View Universe")
        print("4. Edit Data")
        print("5. Delete Data")
        print("6. Back to Main Menu")

        print("============================")


        choice = input(
            "Choose option: "
        )



        if choice == "1":

            create_scene()


        elif choice == "2":

            create_character()


        elif choice == "3":

            view_universe()


        elif choice == "4":

            edit_data()


        elif choice == "5":

            delete_data()


        elif choice == "6":

            break


        else:

            print("❌ Invalid option!")