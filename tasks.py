# =====================================
# 🚀 BOBBY AI STUDIO v5.10
# Autonomous Task Manager
# =====================================


import json
import os


TASK_FILE = "data/tasks.json"



def setup_tasks():

    if not os.path.exists("data"):
        os.makedirs("data")


    if not os.path.exists(TASK_FILE):

        with open(TASK_FILE, "w") as file:

            json.dump([], file)




def load_tasks():

    setup_tasks()


    with open(TASK_FILE, "r") as file:

        return json.load(file)




def save_tasks(tasks):

    with open(TASK_FILE, "w") as file:

        json.dump(tasks, file, indent=4)




def add_task():

    print("\n--- CREATE TASK ---")


    task = input("Enter task: ")


    tasks = load_tasks()


    new_task = {

        "task": task,

        "status": "Pending"

    }


    tasks.append(new_task)


    save_tasks(tasks)


    print("\n✅ Task Created!")




def view_tasks():

    print("\n📋 ACTIVE TASKS\n")


    tasks = load_tasks()


    if not tasks:

        print("No tasks found.")

        return



    for index, task in enumerate(tasks, start=1):

        print("----------------")

        print(index, ".", task["task"])

        print("Status:", task["status"])




def task_manager():

    while True:


        print("\n============================")

        print("     TASK MANAGER v5.10")

        print("============================")

        print("1. Add Task")

        print("2. View Tasks")

        print("3. Back")

        print("============================")


        choice = input("Choose option: ")



        if choice == "1":

            add_task()


        elif choice == "2":

            view_tasks()


        elif choice == "3":

            break


        else:

            print("Invalid choice!")