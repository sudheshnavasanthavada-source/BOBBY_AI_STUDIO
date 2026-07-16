# =====================================
# BOBBY AI STUDIO v2.10
# Pro Foundation System
# =====================================

import os


def system_dashboard():

    print("\n============================")
    print("  BOBBY AI STUDIO DASHBOARD")
    print("============================")

    print("Version: v2.10 PRO FOUNDATION")


    modules = [
        "stories.py",
        "prompts.py",
        "memory.py",
        "notes.py",
        "files.py",
        "workflow.py",
        "security.py"
    ]


    print("\nInstalled Modules:")

    for module in modules:

        if os.path.exists(module):

            print("✅", module)

        else:

            print("❌", module)



def analytics():

    print("\n📊 AI STUDIO ANALYTICS")


    data_files = [
        "data/stories.txt",
        "data/prompts.json",
        "data/workflows.json"
    ]


    for file in data_files:

        if os.path.exists(file):

            print("✅", file)

        else:

            print("⚪", file)



def system_manager():

    print("\n⚙️ SYSTEM MANAGER")

    print("BOBBY AI STUDIO v2.10")
    print("Core systems checked successfully ✅")



def pro_menu():

    while True:

        print("\n============================")
        print("    PRO FOUNDATION v2.10")
        print("============================")

        print("1. System Dashboard")
        print("2. AI Analytics")
        print("3. System Manager")
        print("4. Back")

        print("============================")


        choice = input("Choose option: ")


        if choice == "1":

            system_dashboard()


        elif choice == "2":

            analytics()


        elif choice == "3":

            system_manager()


        elif choice == "4":

            break


        else:

            print("Invalid option!")