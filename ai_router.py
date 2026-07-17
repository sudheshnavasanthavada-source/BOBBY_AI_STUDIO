# ============================================
# BOBBY AI STUDIO v3.5
# AI ROUTER SYSTEM
# ============================================


class AIRouter:


    def __init__(self):

        print("🔀 AI Router Online")



    def route(self, choice):


        routes = {


            "1": (
                "Story Generator",
                self.load_story
            ),


            "2": (
                "Prompt Engineering",
                self.load_prompts
            ),


            "3": (
                "Memory System",
                self.load_memory
            ),


            "4": (
                "Notes",
                self.load_notes
            ),


            "5": (
                "File Management",
                self.load_files
            ),


            "6": (
                "AI Tools Hub",
                self.load_tools
            ),


            "7": (
                "Settings",
                self.load_settings
            ),


            "8": (
                "Workflow Automation",
                self.load_workflow
            ),


            "9": (
                "Security & Backup",
                self.load_security
            ),


            "10": (
                "Pro Foundation",
                self.load_pro
            ),


            "11": (
                "BOBBY Assistant",
                self.load_assistant
            ),


            "12": (
                "AI Model Center",
                self.load_ai_models
            ),


            "13": (
                "META ALPHA Studio",
                self.load_meta_alpha
            ),


            "14": (
                "Voice AI",
                self.load_voice_ai
            )

        }


        return routes.get(choice, (None, None))



# ============================================
# Module Loaders
# ============================================


    def load_story(self):

        from stories import story_menu
        story_menu()



    def load_prompts(self):

        from prompts import prompt_menu
        prompt_menu()



    def load_memory(self):

        from memory import memory_menu
        memory_menu()



    def load_notes(self):

        from notes import notes_menu
        notes_menu()



    def load_files(self):

        from file_manager import file_menu
        file_menu()



    def load_tools(self):

        from tools import tools_menu
        tools_menu()



    def load_settings(self):

        from settings import settings_menu
        settings_menu()



    def load_workflow(self):

        from workflow import workflow_menu
        workflow_menu()



    def load_security(self):

        from security import security_menu
        security_menu()



    def load_pro(self):

        from pro_foundation import pro_menu
        pro_menu()



    def load_assistant(self):

        from assistant import assistant_menu
        assistant_menu()



    def load_ai_models(self):

        from ai_models import ai_model_menu
        ai_model_menu()



    def load_meta_alpha(self):

        from meta_alpha import meta_alpha_menu
        meta_alpha_menu()



    # ========================================
    # VOICE AI v3.5
    # ========================================

    def load_voice_ai(self):

        from voice_ai import voice_ai_menu

        voice_ai_menu()