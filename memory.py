# ==========================================
# 💾 BOBBY MEMORY SYSTEM v5.7
# Smart Memory Module
# ==========================================


import json
import os


MEMORY_FILE = "data/memories.json"



def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []


    with open(MEMORY_FILE, "r") as file:

        return json.load(file)




def save_memory(memory):

    os.makedirs(
        "data",
        exist_ok=True
    )


    memories = load_memory()

    memories.append(memory)


    with open(MEMORY_FILE, "w") as file:

        json.dump(
            memories,
            file,
            indent=4
        )




# ==========================================
# Original AI Memory Command System
# ==========================================

def memory_action(command):

    print(
        "💾 MEMORY PROCESSING:",
        command
    )


    command_lower = command.lower()



    if "remember" in command_lower:


        information = command.replace(
            "remember",
            ""
        ).strip()


        memory = {

            "information": information

        }


        save_memory(memory)


        return (
            "💾 MEMORY SAVED\n\n"
            f"🧠 Remembered: {information}"
        )




    elif "show memory" in command_lower:


        memories = load_memory()


        if not memories:

            return "💾 No memories found."



        return (
            "💾 STORED MEMORIES\n\n"
            +
            "\n".join(
                [
                    str(m)
                    for m in memories
                ]
            )
        )



    else:

        return "💾 Memory System Ready"




# ==========================================
# ⭐ v5.7 MAIN MENU CONNECTORS
# ==========================================


def add_memory():

    print("\n--- ADD MEMORY ---")


    information = input(
        "Enter memory: "
    )


    memory = {

        "information": information

    }


    save_memory(memory)


    print("\n✅ Memory Saved!")





def view_memory():

    print("\n--- STORED MEMORIES ---")


    memories = load_memory()


    if not memories:

        print("No memories found.")

        return



    for memory in memories:

        print("\n🧠", memory)