import json


def recall_memory(keyword):

    try:
        with open("data/memories.json","r") as file:
            memories = json.load(file)

    except:
        memories = []


    results = []

    for memory in memories:

        if keyword.lower() in str(memory).lower():
            results.append(memory)


    return results



def show_recall(keyword):

    results = recall_memory(keyword)


    if results:

        print("\n🧠 MEMORY FOUND\n")

        for item in results:
            print(item)

    else:
        print("\n❌ No memory found")