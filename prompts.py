# =====================================
# BOBBY AI STUDIO v2.8
# Prompt Engineering Center
# =====================================

import json
from datetime import datetime


FILE = "data/prompts.json"


def load_prompts():

    try:

        with open(FILE, "r") as file:
            return json.load(file)

    except:

        return []



def save_prompts(data):

    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)



def create_prompt():

    print("\n--- CREATE AI PROMPT ---")

    title = input("Prompt title: ")
    category = input("Category (Image/Video/Character/Story): ")
    idea = input("Your idea: ")

    prompts = load_prompts()

    new_prompt = {

        "title": title,
        "category": category,
        "idea": idea,
        "date": str(datetime.now())

    }

    prompts.append(new_prompt)

    save_prompts(prompts)

    print("\n✅ Prompt saved successfully!")



# 🔥 v2.8 AUTOMATION FUNCTION
def auto_create_prompt(title, category, idea):

    prompts = load_prompts()

    new_prompt = {

        "title": title,
        "category": category,
        "idea": idea,
        "date": str(datetime.now())

    }

    prompts.append(new_prompt)

    save_prompts(prompts)

    print("✅ Automated Prompt Created!")



def view_prompts():

    print("\n--- SAVED PROMPTS ---")

    prompts = load_prompts()


    if prompts:

        for prompt in prompts:

            print("\nTitle:", prompt["title"])
            print("Category:", prompt["category"])
            print("Idea:", prompt["idea"])
            print("Date:", prompt["date"])


    else:

        print("No prompts found.")



def search_prompt():

    print("\n--- SEARCH PROMPT ---")

    keyword = input("Enter title: ")

    prompts = load_prompts()


    for prompt in prompts:

        if prompt["title"] == keyword:

            print(prompt)

            return


    print("Prompt not found!")



def prompt_menu():

    while True:

        print("\n============================")
        print("   PROMPT ENGINEERING v2.3")
        print("============================")
        print("1. Create Prompt")
        print("2. View Prompts")
        print("3. Search Prompt")
        print("4. Back to Main Menu")
        print("============================")


        choice = input("Choose option: ")


        if choice == "1":

            create_prompt()


        elif choice == "2":

            view_prompts()


        elif choice == "3":

            search_prompt()


        elif choice == "4":

            break


        else:

            print("Invalid choice!")