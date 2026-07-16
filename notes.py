# =====================================
# BOBBY AI STUDIO v2.0
# Notes System Module
# =====================================


FILE = "data/notes.txt"


def add_note():

    print("\n--- ADD NOTE ---")

    note = input("Enter your note: ")

    with open(FILE, "a") as file:
        file.write(note + "\n")

    print("\n✅ Note saved successfully!")


def view_notes():

    print("\n--- SAVED NOTES ---")

    try:
        with open(FILE, "r") as file:
            content = file.read()

            if content:
                print(content)
            else:
                print("No notes found.")

    except FileNotFoundError:
        print("No notes available.")


def notes_menu():

    while True:

        print("\n============================")
        print("        NOTES SYSTEM")
        print("============================")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Back to Main Menu")
        print("============================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")