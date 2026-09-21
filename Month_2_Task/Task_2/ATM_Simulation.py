from datetime import datetime

# Account Details
name = "Aqsa"
pin = "1234"
balance = 50000
transactions = []


# ---------------- LOGIN ----------------

print("=" * 50)
print("             🏧 PYTHON ATM")
print("=" * 50)

for attempt in range(3):

    user_pin = input("Enter your PIN: ")

    if user_pin == pin:
        print("\n✅ Login successful!")
        break
    else:
        print("❌ Wrong PIN!")

else:
    print("\n🚫 Account locked due to 3 wrong attempts.")
    exit()


# ---------------- MAIN MENU ----------------

while True:

    print("\n" + "=" * 50)
    print(f"Welcome, {name}!")
    print("=" * 50)

    print("""
1. 💰 Check Balance
2. 💵 Withdraw Money
3. 💳 Deposit Money
4. 📋 Mini Statement
5. 🔐 Change PIN
6. 🚪 Exit
""")

    option = input("Choose an option (1-6): ")


    # ---------------- BALANCE ----------------

    if option == "1":

        print("\n💰 Your Current Balance:")
        print(f"Rs. {balance:,}")


    # ---------------- WITHDRAW ----------------

    elif option == "2":

        print("\n💵 WITHDRAW MONEY")

        try:
            amount = int(input("Enter withdrawal amount: Rs. "))

            if amount <= 0:
                print("❌ Enter a valid amount.")

            elif amount % 500 != 0:
                print("⚠️ Amount must be a multiple of Rs. 500.")

            elif amount > 20000:
                print("⚠️ Maximum withdrawal limit is Rs. 20,000.")

            elif amount > balance:
                print("❌ Insufficient balance.")

            else:
                balance -= amount

                transactions.append(
                    f"Withdraw - Rs. {amount:,}"
                )

                print("\n✅ Withdrawal successful!")
                print(f"Amount withdrawn: Rs. {amount:,}")
                print(f"Remaining balance: Rs. {balance:,}")

        except ValueError:
            print("❌ Please enter numbers only.")


    # ---------------- DEPOSIT ----------------

    elif option == "3":

        print("\n💳 DEPOSIT MONEY")

        try:
            amount = int(input("Enter deposit amount: Rs. "))

            if amount <= 0:
                print("❌ Enter a valid amount.")

            elif amount > 100000:
                print("⚠️ Maximum deposit limit is Rs. 100,000.")

            else:
                balance += amount

                transactions.append(
                    f"Deposit - Rs. {amount:,}"
                )

                print("\n✅ Deposit successful!")
                print(f"Amount deposited: Rs. {amount:,}")
                print(f"New balance: Rs. {balance:,}")

        except ValueError:
            print("❌ Please enter numbers only.")


    # ---------------- MINI STATEMENT ----------------

    elif option == "4":

        print("\n" + "=" * 50)
        print("              📋 MINI STATEMENT")
        print("=" * 50)

        if len(transactions) == 0:
            print("No transactions made yet.")

        else:
            print("Recent Transactions:\n")

            for i, transaction in enumerate(transactions[-5:], 1):
                print(f"{i}. {transaction}")

        print("\n" + "-" * 50)
        print(f"Current Balance: Rs. {balance:,}")


    # ---------------- CHANGE PIN ----------------

    elif option == "5":

        print("\n🔐 CHANGE PIN")

        old_pin = input("Enter your current PIN: ")

        if old_pin != pin:
            print("❌ Incorrect PIN.")

        else:

            new_pin = input("Enter new 4-digit PIN: ")

            if not new_pin.isdigit() or len(new_pin) != 4:
                print("❌ PIN must contain exactly 4 digits.")

            elif new_pin == pin:
                print("⚠️ New PIN must be different from old PIN.")

            else:

                confirm = input("Confirm new PIN: ")

                if new_pin == confirm:
                    pin = new_pin
                    print("✅ PIN changed successfully!")

                else:
                    print("❌ PIN confirmation does not match.")


    # ---------------- EXIT ----------------

    elif option == "6":

        print("\n" + "=" * 50)
        print("             🧾 SESSION SUMMARY")
        print("=" * 50)

        print(f"Account Holder : {name}")
        print(f"Transactions   : {len(transactions)}")
        print(f"Final Balance  : Rs. {balance:,}")

        current_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

        print(f"Date & Time    : {current_time}")

        print("\n🙏 Thank you for using Python ATM!")
        print("💳 Please collect your card.")
        print("=" * 50)

        break


    # ---------------- INVALID OPTION ----------------

    else:

        print("❌ Invalid option! Please choose between 1 and 6.")