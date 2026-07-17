# =====================================
# 🧠 BOBBY AI STUDIO v5.9
# Knowledge Base System
# =====================================


import json


KNOWLEDGE_FILE = "knowledge/knowledge_base.json"



def load_knowledge():

    try:

        with open(KNOWLEDGE_FILE,"r") as file:

            return json.load(file)

    except:

        return []




def search_knowledge(keyword):

    knowledge = load_knowledge()

    results = []


    for item in knowledge:

        if keyword.lower() in str(item).lower():

            results.append(item)


    return results




def show_knowledge(keyword):

    results = search_knowledge(keyword)


    if results:

        print("\n📚 KNOWLEDGE FOUND\n")


        for item in results:

            print("----------------")
            print("Title:", item["title"])
            print("Category:", item["category"])
            print("Information:", item["information"])


    else:

        print("\n❌ No knowledge found")