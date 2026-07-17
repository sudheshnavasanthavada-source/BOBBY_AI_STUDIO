# ============================================
# BOBBY AI STUDIO v3.2
# BOBBY ASSISTANT ENGINE
# ============================================

import datetime


class BobbyAssistant:

    def __init__(self):

        self.name = "BOBBY Assistant"

        self.version = "v3.2"

        print("\n🧠 BOBBY Assistant Loading...")
        print("🤖 Assistant Online!")
        print("✅ Ready to help!\n")


    def get_response(self, message):

        message = message.lower()


        # Greetings

        if "hello" in message or "hi" in message:

            return (
                "Hello! 👋\n"
                "I am BOBBY Assistant v3.2."
            )


        # Identity

        elif "who are you" in message:

            return (
                "I am BOBBY Assistant 🤖\n"
                "The intelligent assistant inside BOBBY AI STUDIO."
            )


        # Project

        elif "bobby ai studio" in message:

            return (
                "BOBBY AI STUDIO is a personal AI software project "
                "with AI Brain, Memory Engine, Creative Tools and future AI models."
            )


        # META ALPHA

        elif "meta alpha" in message:

            return (
                "META ALPHA is a futuristic sci-fi universe "
                "created inside BOBBY AI STUDIO 🎬"
            )


        # Time

        elif "time" in message:

            return (
                "Current system time: "
                + str(datetime.datetime.now())
            )


        # Help

        elif "help" in message:

            return (
                "I can help with:\n"
                "• BOBBY AI STUDIO\n"
                "• META ALPHA\n"
                "• Project information\n"
                "• General commands"
            )


        # Default

        else:

            return (
                "I am still learning 🧠\n"
                "Future versions will include advanced AI models."
            )



# ============================================
# Assistant Menu
# ============================================

def assistant_menu():

    assistant = BobbyAssistant()


    while True:

        print("============================")
        print("     🤖 BOBBY ASSISTANT v3.2")
        print("============================")
        print("Type 'exit' to return")
        print("============================")


        user = input("\nYou: ")


        if user.lower() == "exit":

            print("\nReturning to BOBBY AI STUDIO...")
            break


        response = assistant.get_response(user)


        print("\nBOBBY AI:")
        print(response)