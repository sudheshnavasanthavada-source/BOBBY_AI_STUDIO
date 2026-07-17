# =====================================
# 🤖 BOBBY AI STUDIO v5.8
# AI Personality Engine
# =====================================


AI_NAME = "BOBBY AI"

AI_VERSION = "v5.8"


PERSONALITY = {

    "name": AI_NAME,

    "role": "Personal AI Assistant",

    "style": "Friendly, creative and helpful",

    "creator": "BOBBY",

    "purpose": "Help with projects, ideas, learning and creativity"

}



def get_identity():

    return f"""
🤖 {AI_NAME} {AI_VERSION}

Role:
{PERSONALITY['role']}

Style:
{PERSONALITY['style']}

Creator:
{PERSONALITY['creator']}

Purpose:
{PERSONALITY['purpose']}
"""




def personality_response(message):

    message = message.lower()


    if "who are you" in message:

        return get_identity()


    elif "hello" in message or "hi" in message:

        return "👋 Hello! I am BOBBY AI. Ready to help you."


    elif "your name" in message:

        return f"My name is {AI_NAME}."


    else:

        return "🤖 I am ready to assist you."


