    # =========================
    # MODULE CONNECTIONS
    # =========================

    def assistant(self):

        print("🔥 ASSISTANT BUTTON CLICKED")

        try:

            from assistant import assistant_menu

            print("✅ assistant.py imported")

            messagebox.showinfo(
                "Assistant",
                "🤖 Opening BOBBY Assistant..."
            )

            assistant_menu()

            print("✅ Assistant window closed")


        except Exception as e:

            print("❌ ERROR:", e)

            messagebox.showerror(
                "Assistant Error",
                str(e)
            )



    def memory(self):

        messagebox.showinfo(
            "Memory",
            "💾 Memory module connection coming next!"
        )



    def prompts(self):

        messagebox.showinfo(
            "Prompts",
            "🎨 Prompt Engineering module"
        )



    def meta_alpha(self):

        messagebox.showinfo(
            "META ALPHA",
            "🌌 META ALPHA Studio module"
        )



    def voice_ai(self):

        messagebox.showinfo(
            "Voice AI",
            "🎙️ Voice AI module"
        )



    def dashboard(self):

        messagebox.showinfo(
            "Dashboard",
            "📊 Dashboard module"
        )



    def settings(self):

        messagebox.showinfo(
            "Settings",
            "⚙️ Settings module"
        )