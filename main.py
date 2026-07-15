print("==============================")
print("🤖 BOBBY AI STUDIO v1.2")
print("==============================")

print("1. Generate Story Idea")
print("2. Create AI Prompt")
print("3. AI Story Generator")
print("4. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print("✨ Story Idea Generator Activated!")
    print("A futuristic world where AI and humans work together.")

elif choice == "2":
    print("🎨 Prompt Creator Activated!")
    print("Create a cinematic AI scene of a futuristic city.")

elif choice == "3":
    topic = input("Enter a story topic: ")
    print("✨ Creating story...")
    print("Story:")
    print("In the future, " + topic + " changed the world with AI.")

elif choice == "4":
    print("Goodbye Bobby! 🚀")