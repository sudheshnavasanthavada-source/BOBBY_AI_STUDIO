# ==========================================
# 🤖 BOBBY ASSISTANT v5.2
# AI CORE CONNECTED
# ==========================================

import customtkinter as ctk


def assistant_menu():

    print("🤖 ASSISTANT MODULE STARTED")


    window = ctk.CTkToplevel()

    window.title("🤖 BOBBY Assistant v5.2")

    window.geometry("900x650")


    # AI CORE CONNECTION

    try:
        from ai_core import process_command
        print("🧠 AI CORE CONNECTED")

    except Exception as e:
        print("❌ AI CORE ERROR:", e)

        def process_command(command):
            return "AI Core not available"



    # =========================
    # TITLE
    # =========================

    title = ctk.CTkLabel(
        window,
        text="🤖 BOBBY ASSISTANT v5.2",
        font=("Arial",32,"bold")
    )

    title.pack(
        pady=25
    )


    # =========================
    # CHAT BOX
    # =========================

    chat_box = ctk.CTkTextbox(
        window,
        width=750,
        height=350,
        font=("Arial",18)
    )

    chat_box.pack(
        pady=20
    )


    chat_box.insert(
        "end",
        "🤖 BOBBY AI: AI Core Connected 🚀\n\n"
    )



    # =========================
    # COMMAND FUNCTION
    # =========================

    def send_command():

        command = entry.get()


        if command:

            chat_box.insert(
                "end",
                "👤 You: "
                + command
                + "\n"
            )


            response = process_command(command)


            chat_box.insert(
                "end",
                "🤖 BOBBY AI: "
                + str(response)
                + "\n\n"
            )


            entry.delete(
                0,
                "end"
            )



    # =========================
    # INPUT BOX
    # =========================

    entry = ctk.CTkEntry(
        window,
        width=600,
        height=40,
        placeholder_text="Enter AI command..."
    )

    entry.pack(
        pady=10
    )



    send_button = ctk.CTkButton(
        window,
        text="🚀 Execute",
        height=40,
        command=send_command
    )

    send_button.pack(
        pady=10
    )


    print("✅ ASSISTANT v5.2 READY")