import random

print("=" * 50)
print("       🎯 NUMBER GUESSING GAME")
print("=" * 50)

player = input("Enter your name: ").strip()

total_score = 0
rounds_won = 0

while True:

    print("\nChoose Difficulty:")
    print("1. Easy   (1 - 50, 8 attempts)")
    print("2. Medium (1 - 100, 7 attempts)")
    print("3. Hard   (1 - 200, 6 attempts)")

    while True:
        choice = input("Enter choice (1-3): ")

        if choice in ["1", "2", "3"]:
            break

        print("❌ Invalid choice! Please select 1, 2 or 3.")

    # Difficulty settings
    if choice == "1":
        minimum = 1
        maximum = 50
        max_attempts = 8
        difficulty = "Easy"

    elif choice == "2":
        minimum = 1
        maximum = 100
        max_attempts = 7
        difficulty = "Medium"

    else:
        minimum = 1
        maximum = 200
        max_attempts = 6
        difficulty = "Hard"

    secret_number = random.randint(minimum, maximum)
    attempts = 0
    won = False

    print("\n" + "-" * 50)
    print(f"🎮 {difficulty} Mode")
    print(f"I'm thinking of a number between {minimum} and {maximum}.")
    print(f"You have {max_attempts} attempts.")
    print("-" * 50)

    # Game loop
    while attempts < max_attempts:

        remaining = max_attempts - attempts

        try:
            guess = int(
                input(
                    f"\nAttempts remaining: {remaining}\n"
                    f"Enter your guess: "
                )
            )

            if guess < minimum or guess > maximum:
                print(
                    f"⚠️ Please enter a number "
                    f"between {minimum} and {maximum}."
                )
                continue

        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:

            won = True

            # Score based on remaining attempts
            score = (max_attempts - attempts + 1) * 10

            # Difficulty bonus
            if difficulty == "Medium":
                score += 10
            elif difficulty == "Hard":
                score += 20

            total_score += score
            rounds_won += 1

            print("\n🎉 CONGRATULATIONS!")
            print(f"🎯 You guessed the number: {secret_number}")
            print(f"🔢 Attempts used: {attempts}")
            print(f"⭐ Score earned: {score}")

            break

        elif guess < secret_number:

            difference = secret_number - guess

            print("⬆️ Too low!")

            if difference <= 5:
                print("🔥 Very close!")
            elif difference <= 15:
                print("🙂 You're getting closer.")

        else:

            difference = guess - secret_number

            print("⬇️ Too high!")

            if difference <= 5:
                print("🔥 Very close!")
            elif difference <= 15:
                print("🙂 You're getting closer.")

    # If player loses
    if not won:
        print("\n💀 GAME OVER!")
        print(f"The correct number was: {secret_number}")

    # Play again
    while True:
        again = input("\nDo you want to play another round? (yes/no): ").lower()

        if again in ["yes", "no"]:
            break

        print("❌ Please enter yes or no.")

    if again == "no":
        break


# Final Summary
print("\n" + "=" * 50)
print("             📊 FINAL RESULTS")
print("=" * 50)

print(f"👤 Player       : {player}")
print(f"🏆 Rounds Won   : {rounds_won}")
print(f"⭐ Total Score  : {total_score}")

if total_score >= 100:
    print("🔥 Excellent performance!")

elif total_score >= 50:
    print("👏 Good performance!")

else:
    print("💪 Keep practicing!")

print("=" * 50)
print("       Thanks for playing! 🎯")
print("=" * 50)