# ============================================
# BOBBY AI STUDIO v3.5
# VOICE AI ENGINE
# ============================================

import datetime



class VoiceAIEngine:


    def __init__(self):

        self.status = "ONLINE"

        print("\n🎙️ Voice AI System Loading...")
        print("🧠 Connecting BOBBY Assistant...")
        print("✅ Voice AI Engine Online!")



    def listen(self):

        print("\n🎤 Listening...")

        command = input(
            "Voice Command: "
        )

        return command



    def process(self, command):

        command = command.lower()


        if "hello" in command:

            return "Hello Bobby! Voice AI is ready."


        elif "time" in command:

            return (
                "Current time is "
                + str(datetime.datetime.now())
            )


        elif "meta alpha" in command:

            return (
                "META ALPHA Studio is active."
            )


        elif "status" in command:

            return (
                "All BOBBY AI STUDIO systems are online."
            )


        else:

            return (
                "Command received successfully. "
                "Advanced AI connection coming in future updates."
            )



    def speak(self, response):

        print("\n🔊 BOBBY Voice:")
        print(response)




# ============================================
# VOICE AI MENU
# ============================================

def voice_ai_menu():


    engine = VoiceAIEngine()



    while True:


        print("\n============================")
        print("      🎙️ VOICE AI v3.5")
        print("============================")

        print("1. Voice Command")
        print("2. System Status")
        print("3. Back to Main Menu")

        print("============================")


        choice = input(
            "Choose option: "
        )



        if choice == "1":

            command = engine.listen()

            response = engine.process(
                command
            )

            engine.speak(
                response
            )



        elif choice == "2":

            print(
                "\nSystem Status:",
                engine.status
            )



        elif choice == "3":

            break



        else:

            print(
                "\n❌ Invalid option!"
            )