# ==========================================
# 🔀 BOBBY AI ROUTER v5.3
# Module Decision Engine
# ==========================================


def route_command(command):

    print("🔀 AI ROUTER ANALYZING:", command)


    command = command.lower()


    if "meta alpha" in command or "character" in command:
        
        return {
            "module": "META ALPHA Studio",
            "action": "creative_generation"
        }


    elif "memory" in command or "remember" in command:

        return {
            "module": "Memory System",
            "action": "memory_operation"
        }


    elif "voice" in command:

        return {
            "module": "Voice AI",
            "action": "voice_command"
        }


    elif "dashboard" in command or "status" in command:

        return {
            "module": "Dashboard",
            "action": "system_status"
        }


    else:

        return {
            "module": "AI Core",
            "action": "general_response"
        }



if __name__ == "__main__":

    print(
        route_command(
            "Create META ALPHA character"
        )
    )