# =====================================
# BOBBY AI STUDIO v2.8
# Story Generator Module
# =====================================


def create_story():

    print("\n--- CREATE STORY ---")

    title = input("Enter story title: ")
    genre = input("Enter genre: ")
    idea = input("Enter story idea: ")

    story = {
        "Title": title,
        "Genre": genre,
        "Idea": idea
    }

    with open("data/stories.txt", "a") as file:
        file.write(str(story) + "\n")

    print("\n✅ Story saved successfully!")


# 🔥 v2.8 AUTOMATION FUNCTION
def auto_create_story(title, genre, idea):

    story = {
        "Title": title,
        "Genre": genre,
        "Idea": idea
    }

    with open("data/stories.txt", "a") as file:
        file.write(str(story) + "\n")

    print("✅ Automated Story Created!")


def view_stories():

    print("\n--- SAVED STORIES ---")

    try:

        with open("data/stories.txt", "r") as file:

            content = file.read()

            if content:
                print(content)

            else:
                print("No stories found.")

    except FileNotFoundError:

        print("No stories created yet.")



def story_menu():

    while True:

        print("\n============================")
        print("      STORY GENERATOR")
        print("============================")
        print("1. Create Story")
        print("2. View Stories")
        print("3. Back to Main Menu")
        print("============================")

        choice = input("Choose an option: ")


        if choice == "1":

            create_story()


        elif choice == "2":

            view_stories()


        elif choice == "3":

            break


        else:

            print("Invalid choice!")