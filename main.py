def save_file(filename, content):
    file = open(filename, "a")
    file.write(content + "\n")
    file.close()




print("==============================")
print("🤖 BOBBY AI STUDIO v1.4")
print("==============================")

print("1. Generate Story Idea")
print("2. Create AI Prompt")
print("3. AI Story Generator")
print("4. Cinematic Prompt Generator")
print("5. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print("✨ Story Idea Generator Activated!")
    story = "A futuristic world where AI and humans work together."
    print(story)
    save_file("stories.txt", story)

elif choice == "2":
    print("🎨 Prompt Creator Activated!")
    print("Create a cinematic AI scene of a futuristic city.")

elif choice == "3":
    topic = input("Enter a story topic: ")
    print("✨ Creating story...")
    print("Story:")

    story = "In the future, " + topic + " changed the world with AI."

    print(story)
    save_file("stories.txt", story)

elif choice == "4":
    scene = input("Enter a scene idea: ")
    print("🎬 Creating cinematic prompt...")
    
    prompt = "A cinematic scene of " + scene + ", ultra detailed, movie style, dramatic lighting."

    print("Prompt:")
    print(prompt)

    save_file("prompts.txt", prompt)
elif choice == "5":
    print("Goodbye Bobby! 🚀")