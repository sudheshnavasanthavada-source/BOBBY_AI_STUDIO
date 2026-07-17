# ============================================
# BOBBY AI STUDIO v3.0
# AI CORE
# ============================================

class AICore:

    def __init__(self):
        print("\n" + "=" * 45)
        print("🧠 Initializing BOBBY AI Brain...")
        print("⚡ Loading Core Modules...")
        print("✅ AI Brain Online!")
        print("=" * 45)

    def process(self, module_name, function):
        """
        Executes an AI module safely.
        """

        try:
            print(f"\n🚀 Launching {module_name}...\n")
            function()

        except Exception as error:
            print("\n❌ Module Failed!")
            print(f"Module : {module_name}")
            print(f"Reason : {error}")