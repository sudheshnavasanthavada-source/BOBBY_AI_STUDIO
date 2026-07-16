# =====================================
# BOBBY AI STUDIO v2.10
# Main Control Center
# =====================================

import stories
import prompts
import memory
import notes
import files
import ai_tools
import ui
import settings
import workflow
import security
import pro_foundation



def show_menu():

    ui.separator()

    print("       BOBBY AI STUDIO v2.10")

    ui.separator()

    print("1. Story Generator")
    print("2. Prompt Engineering")
    print("3. Memory System")
    print("4. Notes")
    print("5. File Management")
    print("6. AI Tools Hub")
    print("7. Settings")
    print("8. Workflow Automation")
    print("9. Security & Backup")
    print("10. Pro Foundation")
    print("11. Exit")

    ui.separator()



def workflow_menu():

    while True:

        ui.separator()

        print("       WORKFLOW AUTOMATION v2.8")

        ui.separator()

        print("1. Create Workflow")
        print("2. View Workflows")
        print("3. Run Workflow")
        print("4. Back")

        ui.separator()


        choice = input("Choose option: ")


        if choice == "1":
            workflow.create_workflow()

        elif choice == "2":
            workflow.view_workflows()

        elif choice == "3":
            workflow.run_workflow()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")



def main():

    ui.startup_animation()

    ui.show_banner()


    while True:

        show_menu()

        choice = input("Choose option: ")


        if choice == "1":
            stories.story_menu()

        elif choice == "2":
            prompts.prompt_menu()

        elif choice == "3":
            memory.memory_menu()

        elif choice == "4":
            notes.notes_menu()

        elif choice == "5":
            files.file_menu()

        elif choice == "6":
            ai_tools.ai_tools_menu()

        elif choice == "7":
            settings.settings_menu()

        elif choice == "8":
            workflow_menu()

        elif choice == "9":
            security.security_menu()

        elif choice == "10":
            pro_foundation.pro_menu()

        elif choice == "11":
            print("\nClosing BOBBY AI STUDIO...")
            break

        else:
            print("Invalid choice! Try again.")



if __name__ == "__main__":
    main()