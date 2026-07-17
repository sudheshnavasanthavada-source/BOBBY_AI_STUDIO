import customtkinter as ctk
from tkinter import messagebox


class BobbyMainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("🤖 BOBBY AI STUDIO v5.1")
        self.geometry("1400x850")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )


        logo = ctk.CTkLabel(
            self.sidebar,
            text="🤖\nBOBBY AI\nSTUDIO",
            font=("Arial",26,"bold")
        )

        logo.pack(pady=30)


        buttons = [
            ("🏠 Home", self.home),
            ("🤖 Assistant", self.assistant),
            ("💾 Memory", self.memory),
            ("🎨 Prompts", self.prompts),
            ("🌌 META ALPHA", self.meta_alpha),
            ("🎙️ Voice AI", self.voice_ai),
            ("📊 Dashboard", self.dashboard),
            ("⚙️ Settings", self.settings)
        ]


        for name, command in buttons:

            ctk.CTkButton(
                self.sidebar,
                text=name,
                height=45,
                command=command
            ).pack(
                padx=15,
                pady=8,
                fill="x"
            )


        self.main = ctk.CTkFrame(self)

        self.main.pack(
            expand=True,
            fill="both"
        )


        self.home()



    def clear(self):

        for widget in self.main.winfo_children():
            widget.destroy()



    def home(self):

        self.clear()

        ctk.CTkLabel(
            self.main,
            text="Welcome to BOBBY AI STUDIO",
            font=("Arial",34,"bold")
        ).pack(pady=50)


    def assistant(self):

        print("🔥 ASSISTANT BUTTON CLICKED")

        try:
            from assistant import assistant_menu
            assistant_menu()

        except Exception as e:
            messagebox.showerror(
                "Assistant Error",
                str(e)
            )


    def memory(self):
        messagebox.showinfo("Memory","💾 Memory System")


    def prompts(self):
        messagebox.showinfo("Prompts","🎨 Prompt Engineering")


    def meta_alpha(self):
        messagebox.showinfo("META ALPHA","🌌 META ALPHA Studio")


    def voice_ai(self):
        messagebox.showinfo("Voice AI","🎙️ Voice AI")


    def dashboard(self):
        messagebox.showinfo("Dashboard","📊 Dashboard")


    def settings(self):
        messagebox.showinfo("Settings","⚙️ Settings")