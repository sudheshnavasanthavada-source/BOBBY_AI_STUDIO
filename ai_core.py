# ==========================================
# 🧠 BOBBY AI CORE v5.4
# AI Brain + Router + Workflow Engine
# ==========================================


from ai_router import route_command
from workflow import execute_workflow



def process_command(command):

    print("🧠 AI CORE PROCESSING:", command)


    try:

        # Step 1: Analyze command
        result = route_command(command)


        module = result["module"]
        action = result["action"]


        # Step 2: Execute workflow
        response = execute_workflow(
            module,
            action,
            command
        )


        return response


    except Exception as e:

        print("❌ AI CORE ERROR:", e)

        return (
            "❌ AI Core Error:\n"
            + str(e)
        )



# ==========================
# TEST MODE
# ==========================

if __name__ == "__main__":

    print(
        process_command(
            "Create META ALPHA character"
        )
    )