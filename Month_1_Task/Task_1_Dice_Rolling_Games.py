import random
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def show_result(die1, die2):
    total = die1 + die2
    print("\n" + "=" * 30)
    print("🎲 DICE RESULT")
    print("=" * 30)
    print(f"Die 1       : {die1}")
    print(f"Die 2       : {die2}")
    print(f"Total       : {total}")

    if die1 == die2:
        print("🔥 DOUBLE! Both dice are the same!")
    if total == 7:
        print("⭐ Lucky 7!")
    if total == 12:
        print("🏆 Highest possible score!")
def show_statistics(history):
    if not history:
        return
    totals = [roll[2] for roll in history]
    print("\n📊 GAME STATISTICS")
    print("-" * 30)
    print(f"Total Rolls : {len(history)}")
    print(f"Highest     : {max(totals)}")
    print(f"Lowest      : {min(totals)}")
    print(f"Average     : {sum(totals) / len(totals):.2f}")
def show_history(history):
    if not history:
        print("\nNo rolls yet.")
        return
    print("\n📜 ROLL HISTORY")
    print("-" * 30)
    for number, (die1, die2, total) in enumerate(history, 1):
        print(f"Roll {number}: {die1} + {die2} = {total}")
print("=" * 35)
print("🎲 WELCOME TO DICE ROLLING GAME 🎲")
print("=" * 35)
history = []
while True:
    print("\n1. Roll Dice")
    print("2. View History")
    print("3. View Statistics")
    print("4. Exit")
    choice = input("\nEnter your choice: ").strip()
    if choice == "1":

        die1, die2 = roll_dice()
        total = die1 + die2
        history.append((die1, die2, total))
        show_result(die1, die2)
    elif choice == "2":
        show_history(history)
    elif choice == "3":
        show_statistics(history)
    elif choice == "4":
        print("\nThanks for playing! 🎲")
        print(f"You made {len(history)} roll(s).")
        break
    else:
        print("\n❌ Invalid choice! Please select 1-4.")