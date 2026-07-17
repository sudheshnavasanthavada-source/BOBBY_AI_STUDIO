# ============================================
# BOBBY AI STUDIO v3.1
# SMART MEMORY ENGINE
# ============================================

import json
import os
from datetime import datetime


MEMORY_FILE = "data/memory.json"


# ============================================
# Storage Setup
# ============================================

def setup_memory():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as file:
            json.dump([], file)



def load_memory():

    setup_memory()

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)



def save_memory(data):

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)



# ============================================
# Add Smart Memory
# ============================================

def add_memory():

    print("\n--- ADD SMART MEMORY ---")

    name = input("Memory Name: ")

    information = input("Information: ")

    category = input("Category: ")

    importance = input(
        "Importance (Low/Medium/High): "
    )


    tags = input(
        "Tags (separate with commas): "
    )

    tags = [
        tag.strip()
        for tag in tags.split(",")
    ]


    memory = {

        "name": name,

        "information": information,

        "category": category,

        "importance": importance,

        "tags": tags,

        "created":
            str(datetime.now())

    }


    memories = load_memory()

    memories.append(memory)

    save_memory(memories)


    print("\n✅ Smart Memory Saved!")



# ============================================
# View Memory
# ============================================

def view_memory():

    print("\n--- ALL SMART MEMORY ---")

    memories = load_memory()


    if not memories:

        print("No memory found.")
        return


    for memory in memories:

        print("\n---------------------")

        print("Name:", memory["name"])

        print("Information:",
              memory["information"])

        print("Category:",
              memory["category"])

        print("Importance:",
              memory["importance"])

        print("Tags:",
              ", ".join(memory["tags"]))

        print("Created:",
              memory["created"])



# ============================================
# Smart Search
# ============================================

def search_memory():

    print("\n--- SMART SEARCH ---")

    query = input(
        "Search memory: "
    ).lower()


    memories = load_memory()


    found = False


    for memory in memories:


        text = (

            memory["name"]

            + memory["information"]

            + memory["category"]

            + " ".join(memory["tags"])

        ).lower()


        if query in text:


            print("\n✅ Memory Found")

            print("----------------")

            print("Name:",
                  memory["name"])

            print("Information:",
                  memory["information"])

            print("Category:",
                  memory["category"])

            print("Importance:",
                  memory["importance"])

            print("Tags:",
                  ", ".join(memory["tags"]))


            found = True



    if not found:

        print("\n❌ Memory not found.")



# ============================================
# Delete Memory
# ============================================

def delete_memory():

    print("\n--- DELETE MEMORY ---")

    name = input(
        "Enter memory name: "
    )


    memories = load_memory()


    new_memory = [

        m for m in memories

        if m["name"] != name

    ]


    save_memory(new_memory)


    print("\n✅ Memory Deleted!")



# ============================================
# Memory Menu
# ============================================

def memory_menu():

    while True:

        print("\n============================")
        print("   SMART MEMORY ENGINE v3.1")
        print("============================")

        print("1. Add Smart Memory")
        print("2. View Memory")
        print("3. Search Memory")
        print("4. Delete Memory")
        print("5. Back to Main Menu")

        print("============================")


        choice = input(
            "Choose option: "
        )


        if choice == "1":

            add_memory()


        elif choice == "2":

            view_memory()


        elif choice == "3":

            search_memory()


        elif choice == "4":

            delete_memory()


        elif choice == "5":

            break


        else:

            print("❌ Invalid option!")