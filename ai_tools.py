# =====================================
# BOBBY AI STUDIO v2.4
# AI Tools Hub
# =====================================


def word_counter():

    print("\n--- WORD COUNTER ---")

    text = input("Enter text: ")

    words = text.split()

    print("Total words:", len(words))


def text_analyzer():

    print("\n--- TEXT ANALYZER ---")

    text = input("Enter text: ")

    print("Characters:", len(text))
    print("Words:", len(text.split()))


def idea_generator():

    print("\n--- IDEA GENERATOR ---")

    topic = input("Enter topic: ")

    print("\nGenerated Idea:")
    print(
        "Create an advanced project about "
        + topic
        + " with innovative features."
    )


def ai_tools_menu():

    while True:

        print("\n============================")
        print("        AI TOOLS HUB v2.4")
        print("============================")
        print("1. Word Counter")
        print("2. Text Analyzer")
        print("3. Idea Generator")
        print("4. Back to Main Menu")
        print("============================")

        choice = input("Choose option: ")

        if choice == "1":
            word_counter()

        elif choice == "2":
            text_analyzer()

        elif choice == "3":
            idea_generator()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")