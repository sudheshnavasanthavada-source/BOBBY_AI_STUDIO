# ============================================
# BOBBY AI STUDIO v3.5
# MAIN PROGRAM
# ============================================

from ai_core import AICore
from ai_router import AIRouter


# ============================================
# Initialize AI Brain
# ============================================

brain = AICore()
router = AIRouter()



# ============================================
# Main Menu
# ============================================

def show_menu():

    print("\n" + "=" * 45)
    print("        🤖 BOBBY AI STUDIO v3.5")
    print("          🧠 AI CREATIVE HUB")
    print("=" * 45)

    print("1.  Story Generator")
    print("2.  Prompt Engineering")
    print("3.  Memory System")
    print("4.  Notes")
    print("5.  File Management")
    print("6.  AI Tools Hub")
    print("7.  Settings")
    print("8.  Workflow Automation")
    print("9.  Security & Backup")
    print("10. Pro Foundation")
    print("11. BOBBY Assistant")
    print("12. AI Model Center")
    print("13. META ALPHA Studio")
    print("14. Voice AI")
    print("15. Exit")

    print("=" * 45)



# ============================================
# Main System Loop
# ============================================

def main():

    print("\n🚀 Welcome to BOBBY AI STUDIO")
    print("🧠 AI Brain Foundation Loaded Successfully!")
    print("⚡ All Systems Ready")


    while True:


        try:

            show_menu()


            choice = input(
                "Choose option: "
            ).strip()



            if choice == "15":

                print("\n👋 Closing BOBBY AI STUDIO...")
                print("🧠 AI Brain Shutdown Complete.")
                print("Goodbye Bobby! 🚀\n")

                break



            module_name, function = router.route(choice)



            if function:

                brain.process(
                    module_name,
                    function
                )


            else:

                print("\n❌ Invalid option!")



        except KeyboardInterrupt:

            print("\n\n⚠ Program interrupted.")
            print("🧠 AI Brain Shutdown Complete.")

            break



        except Exception as error:

            print("\n❌ System Error:")
            print(error)



# ============================================
# Start Application
# ============================================

if __name__ == "__main__":

    main()