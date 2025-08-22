# -- This Project created by Atak_o --
# -------------------------------------
# This Project is Open_source A.I project so you can change everything you want!
# -------------------------------------

import time
import random

# Normalize helper (safe for Turkish inputs too)
def norm(s: str) -> str:
    return " ".join(s.strip().casefold().split())

# Login system:
# --------------------
def login():
    print("System is starting...")
    time.sleep(1.2)

    username = input("Please enter your username: ")
    print("Checking username, please wait...")
    time.sleep(1)
    # Change Your_Name to the name you want.
    if username == "Your_Name":
        print("✅ Username is correct.")
        time.sleep(0.5)

        password = input("Please enter the password: ")
        print("Checking password, please wait...")
        time.sleep(1)
        # Change Your_password to the password you want.
        if password == "Your_password":
            print("✅ Password is correct.")
            time.sleep(0.5)
            return True
        else:
            print("❌ Wrong password.")
            password = input("Please try again: ")
            print("Checking again, please wait...")
            time.sleep(1)
            if password == "141214":
                print("✅ Password is correct.")
                time.sleep(0.5)
                return True
            else:
                print("❌ Wrong again. Login failed.")
                return False
    else:
        print("❌ Wrong username.")
        print("System shutting down...")
        time.sleep(1)
        return False

# Door game command:
# --------------------
def door_game():
    print("🎮 Door game starting...")
    time.sleep(0.8)
    print("If you find a dinosaur → 40 points, a herd of donkeys → 30 points, and a house → 100 points.")
    door = norm(input("Please choose a door! (1/2/3): "))

    if door == "1":
        print("🟥 You opened the red door and met a dinosaur. 🦖 Could you escape?")
    elif door == "2":
        print("🟩 You opened the green door and found a herd of donkeys. 😅 Your ears are ringing!")
    elif door == "3":
        print("🟦 You opened the blue door and reached your cozy house! 🏡 Time to relax by the fireplace.")
    else:
        print("🚫 Invalid choice. Please enter 1, 2, or 3.")

# Multiple riddles:
# -----------------
def riddle():
    riddles = [
        {"q": "🧠 Gives knowledge to everyone! Our best friend! What is it?", "answers": {"book", "kitap"}},
        {"q": "🧩 I always move forward, never go back. What am I?", "answers": {"time", "zaman"}},
        {"q": "✨ The more you take, the bigger it gets. What is it?", "answers": {"hole", "delik"}},
        {"q": "🌙 You can’t see me in the day, I shine at night. What am I?", "answers": {"moon", "ay"}},
    ]
    q = random.choice(riddles)
    user = norm(input(q["q"] + " "))
    if user in q["answers"]:
        print("✅ Correct answer! Well done! 😎")
    else:
        correct = "/".join(sorted(q["answers"]))
        print(f"❌ Wrong. The correct answer was: {correct}")

# Department selection
# -------------------
def department_selection():
    q = norm(input("Which one do you like the most: coding, drawing, or testing? "))
    if q == "coding":
        print("👩‍💻 Welcome to the Development Department!")
    elif q in {"drawing", "çizim", "cizim"}:
        print("🎨 Welcome to the Design Department!")
    elif q == "testing":
        print("🧪 Welcome to the Quality Control Department!")
    else:
        print("🙃 Sorry, we don’t have a department for you.")

# Game recommendation:
# -------------------
def game_suggestion():
    q1 = norm(input("What is your favorite game type? (racing, fighting, shooter): "))
    q2 = norm(input("Do you like playing with friends? (yes/no): "))

    if q1 == "fighting" and q2 == "yes":
        print("You will love playing Street Fighter.")
    elif q1 == "fighting" and q2 == "no":
        print("Sorry, no recommendations ):")
    elif q1 == "racing" and q2 == "yes":
        print("You will love Cars 3: Driven To Win!")
    elif q1 == "racing" and q2 == "no":
        print("You will love Assetto Corsa!")
    elif q1 == "shooter" and q2 == "yes":
        print("You will love Call of Duty!")
    elif q1 == "shooter" and q2 == "no":
        print("You will love Rainbow Six Siege!")
    else:
        print("Sorry, no game suggestions!")

# Intern test:
# -------------------
def intern_test():
    print("📝 Intern test started!")
    print("Choose your level: 'beginner', 'intermediate', 'advanced'")
    python_level = norm(input("How much Python do you know? "))

    if python_level in {"intermediate", "advanced"}:
        print("✅ Welcome intern! Now a mini Python quiz begins...")
        time.sleep(1)

        questions = [
            {"q": "1) Which stops drawing in Turtle?\nA) t.pendown()  B) t.penup()  C) t.goto()", "a": "b"},
            {"q": "2) Which one is a Python data type?\nA) int  B) fast  C) speed", "a": "a"},
            {"q": "3) What does 'print()' do?\nA) Returns length  B) Makes text lowercase  C) Prints text", "a": "c"},
        ]

        correct_count = 0
        for s in questions:
            ans = norm(input(s["q"] + " "))
            if ans == s["a"]:
                print("✅ Correct!")
                correct_count += 1
            else:
                print("❌ Wrong!")

        print(f"📊 Test finished! You got {correct_count}/{len(questions)} correct.")

        if correct_count == len(questions):
            print("🎉 Congratulations! Perfect score, your level is really good!")
        else:
            print("😅 Not bad, but you should study more!")
    elif python_level == "beginner":
        print("❌ Sorry, you don’t meet the requirements 😕")
    else:
        print("🚫 Didn’t understand, please write 'beginner', 'intermediate', or 'advanced'.")

# Help command:
# -------------------
def help_menu():
    print("Loading command list...")
    time.sleep(0.6)
    print(
        "\nCommands:\n"
        " • door game        : Starts a door choosing game.\n"
        " • intern test      : Mini Python test by level.\n"
        " • riddle           : Asks random riddles.\n"
        " • game suggestion  : Suggests a game based on your choices.\n"
        " • department       : Suggests a department for you.\n"
        " • coin toss        : Flips a coin.\n"
        " • help             : Shows this menu.\n"
        " • exit             : Closes the program.\n"
    )

# --- COIN TOSS ---
def coin_toss(flips: int = 1):
    """Flips a coin. If flips > 1, tosses multiple times."""
    print("🪙 Flipping the coin...")
    time.sleep(0.6)
    results = []
    for _ in range(max(1, int(flips))):
        results.append(random.choice(["Heads", "Tails"]))
        time.sleep(0.2)
    if len(results) == 1:
        print("Result:", results[0])
    else:
        print("Results:", ", ".join(results))
        print(f"Summary → Heads: {results.count('Heads')} | Tails: {results.count('Tails')}")

# --- MAIN LOOP ---
def main():
    if login():
        print("🧠 Welcome, how can I assist you?")
        while True:
            raw = input("Enter command (type 'help' for commands, 'exit' to quit): ")
            command = norm(raw)

            if command in {"door game"}:
                door_game()
            elif command == "riddle":
                print("Loading riddle, please wait...")
                time.sleep(0.5)
                riddle()
            elif command == "intern test":
                print("Intern test loading, please wait...")
                time.sleep(0.5)
                intern_test()
            elif command == "game suggestion":
                print("Loading game suggestion, please wait...")
                time.sleep(0.5)
                game_suggestion()
            elif command == "help":
                help_menu()
            elif command in {"coin toss", "flip", "toss"}:
                parts = raw.strip().split()
                flips = 1
                if parts and parts[-1].isdigit():
                    flips = int(parts[-1])
                coin_toss(flips=flips)
            elif command == "department":
                department_selection()
            elif command in {"exit", "quit"}:
                print("Shutting down... Goodbye!")
                break
            else:
                print("🚫 Invalid command. Type 'help' to see available commands.")
    else:
        print("Login failed. Shutting down...")

if __name__ == "__main__":
    main()
