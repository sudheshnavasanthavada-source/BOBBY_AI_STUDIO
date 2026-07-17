# BOBBY AI STUDIO v5.7
# Main Controller

from stories import story_generator
from prompts import prompt_generator
from memory import add_memory, view_memory
from notes import notes_manager
from recall import show_recall


def main_menu():

    while True:

        print("\n==============================")
        print("      BOBBY AI STUDIO v5.7")
        print("==============================")

        print("1. Story Generator")
        print("2. Prompt Generator")
        print("3. Memory System")
        print("4. Notes")
        print("5. View Memories")
        print("6. Memory Recall")
        print("7. Exit")

        choice = input("\nEnter your choice: ")


        if choice == "1":

            story_generator()


        elif choice == "2":

            prompt_generator()


        elif choice == "3":

            add_memory()


        elif choice == "4":

            notes_manager()


        elif choice == "5":

            view_memory()


        elif choice == "6":

            keyword = input("\nSearch memory: ")

            show_recall(keyword)


        elif choice == "7":

            print("\n🚀 Closing BOBBY AI STUDIO...")
            break


        else:

            print("\n❌ Invalid choice. Try again.")



if __name__ == "__main__":

    main_menu()