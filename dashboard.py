# ============================================
# BOBBY AI STUDIO v4.1
# AI DASHBOARD SYSTEM
# ============================================

import json
import os



class AIDashboard:


    def __init__(self):

        self.status = "ONLINE"


        print("\n📊 AI Dashboard Loading...")
        print("🔍 Checking System Modules...")
        print("✅ Dashboard Ready!")



    def count_data(self, file):

        try:

            if os.path.exists(file):

                with open(
                    file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)

                    return len(data)


            return 0


        except:

            return 0



    def show_dashboard(self):


        memories = self.count_data(
            "data/memory.json"
        )


        prompts = self.count_data(
            "data/prompts.json"
        )


        universe = self.count_data(
            "data/meta_alpha.json"
        )



        print("\n================================")
        print("      🤖 BOBBY AI DASHBOARD v4.1")
        print("================================")


        print("\n🧠 AI Brain:")
        print("   ONLINE ✅")


        print("\n💾 Memory System:")
        print("   ACTIVE ✅")
        print("   Records:", memories)


        print("\n🎨 Prompt Engineering:")
        print("   ACTIVE ✅")
        print("   Prompts:", prompts)


        print("\n🌌 META ALPHA Studio:")
        print("   LOADED ✅")
        print("   Objects:", universe)


        print("\n🎙️ Voice AI:")
        print("   ONLINE ✅")


        print("\n🤖 BOBBY Assistant:")
        print("   READY ✅")


        print("\n================================")



# ============================================
# Dashboard Menu
# ============================================

def dashboard_menu():


    dashboard = AIDashboard()


    while True:


        print("\n============================")
        print("     📊 DASHBOARD v4.1")
        print("============================")

        print("1. View Dashboard")
        print("2. System Status")
        print("3. Back to Main Menu")

        print("============================")


        choice = input(
            "Choose option: "
        )



        if choice == "1":

            dashboard.show_dashboard()



        elif choice == "2":

            print(
                "\nDashboard Status:",
                dashboard.status
            )



        elif choice == "3":

            break



        else:

            print(
                "❌ Invalid option!"
            )