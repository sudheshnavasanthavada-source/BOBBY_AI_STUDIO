# ============================================
# BOBBY AI STUDIO v5.7
# PROMPT ENGINEERING CENTER
# ============================================

import json
import os
from datetime import datetime


PROMPT_FILE = "data/prompts.json"


# ============================================
# Setup Storage
# ============================================

def setup_prompts():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(PROMPT_FILE):

        with open(PROMPT_FILE, "w") as file:
            json.dump([], file)



def load_prompts():

    setup_prompts()

    with open(PROMPT_FILE, "r") as file:
        return json.load(file)



def save_prompts(prompts):

    with open(PROMPT_FILE, "w") as file:
        json.dump(prompts, file, indent=4)



# ============================================
# Create AI Prompt
# ============================================

def create_prompt():

    print("\n--- CREATE AI PROMPT ---")

    title = input("Prompt title: ")

    category = input(
        "Category (Image/Video/Character/Story): "
    )

    idea = input(
        "Your idea: "
    )


    prompt = {

        "title": title,

        "category": category,

        "idea": idea,

        "date": str(datetime.now())

    }


    prompts = load_prompts()

    prompts.append(prompt)

    save_prompts(prompts)


    print("\n✅ Prompt saved successfully!")



# ============================================
# View Saved Prompts
# ============================================

def view_prompts():

    print("\n--- SAVED PROMPTS ---")


    prompts = load_prompts()


    if not prompts:

        print("No prompts found.")
        return


    for prompt in prompts:

        print("\n---------------------")

        print("Title:", prompt["title"])

        print("Category:", prompt["category"])

        print("Idea:", prompt["idea"])

        print("Date:", prompt["date"])




# ============================================
# Smart Search Prompt
# ============================================

def search_prompt():

    print("\n--- SEARCH PROMPT ---")


    search = input(
        "Enter title: "
    ).lower()


    prompts = load_prompts()


    found = False


    for prompt in prompts:


        if search in prompt["title"].lower():

            print("\n✅ Prompt Found")

            print("---------------------")

            print("Title:", prompt["title"])

            print("Category:", prompt["category"])

            print("Idea:", prompt["idea"])

            print("Date:", prompt["date"])


            found = True



    if not found:

        print("\n❌ Prompt not found!")



# ============================================
# ⭐ v5.7 CONNECTOR FUNCTION
# Used by main.py
# ============================================

def prompt_generator():

    prompt_menu()



# ============================================
# Prompt Menu
# ============================================

def prompt_menu():

    while True:

        print("\n============================")
        print("   PROMPT ENGINEERING v5.7")
        print("============================")

        print("1. Create Prompt")
        print("2. View Prompts")
        print("3. Search Prompt")
        print("4. Back to Main Menu")

        print("============================")


        choice = input(
            "Choose option: "
        )


        if choice == "1":

            create_prompt()


        elif choice == "2":

            view_prompts()


        elif choice == "3":

            search_prompt()


        elif choice == "4":

            break


        else:

            print("❌ Invalid option!")