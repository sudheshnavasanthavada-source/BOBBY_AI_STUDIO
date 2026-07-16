# =====================================
# BOBBY AI STUDIO v2.1
# Advanced Memory System
# =====================================

import json
from datetime import datetime


FILE = "data/memory.json"


def load_memory():

    try:
        with open(FILE, "r") as file:
            return json.load(file)

    except:
        return {}


def save_memory_file(data):

    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_memory():

    print("\n--- ADD MEMORY ---")

    name = input("Memory name: ")
    value = input("Memory information: ")
    category = input("Category: ")

    data = load_memory()

    data[name] = {
        "value": value,
        "category": category,
        "date": str(datetime.now())
    }

    save_memory_file(data)

    print("\n✅ Memory added!")


def view_memory():

    print("\n--- ALL MEMORY ---")

    data = load_memory()

    if data:
        for name, info in data.items():
            print("\nName:", name)
            print("Information:", info["value"])
            print("Category:", info["category"])
            print("Date:", info["date"])

    else:
        print("No memory found.")


def search_memory():

    print("\n--- SEARCH MEMORY ---")

    keyword = input("Search name: ")

    data = load_memory()

    if keyword in data:
        print(data[keyword])

    else:
        print("Memory not found.")


def delete_memory():

    print("\n--- DELETE MEMORY ---")

    name = input("Memory name to delete: ")

    data = load_memory()

    if name in data:
        del data[name]
        save_memory_file(data)
        print("✅ Memory deleted!")

    else:
        print("Memory not found.")


def memory_menu():

    while True:

        print("\n============================")
        print("     ADVANCED MEMORY v2.1")
        print("============================")
        print("1. Add Memory")
        print("2. View Memory")
        print("3. Search Memory")
        print("4. Delete Memory")
        print("5. Back to Main Menu")
        print("============================")

        choice = input("Choose option: ")


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
            print("Invalid option!")