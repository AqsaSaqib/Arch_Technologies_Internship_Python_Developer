# 🏧 ATM Simulation
A console-based **ATM Simulation** developed in Python as part of my **Python Developer Internship at Arch Technologies**.
This project simulates common ATM operations and provides a simple interactive menu through which users can securely access their account, manage their balance, and view their transactions.

## ✨ Features
* 🔐 PIN verification with a maximum of 3 attempts
* 💰 Check current account balance
* 💵 Withdraw money with validation
* 💳 Deposit money
* 📋 View recent transaction history
* 🔐 Change existing PIN
* 🧾 Display session summary
* 🕐 Show current date and time
* ⚠️ Handle invalid inputs and transaction limits

## 🛠️ Technologies Used
* **Python 3**
* **datetime** module

## 🔑 Default Account Details
The program starts with the following sample account:
```text
Account Holder: Aqsa
PIN: 1234
Balance: Rs. 50,000
```

## 🎮 How It Works
When the program starts, the user must enter the correct PIN. The user gets three attempts before the account is locked.
After successful login, an ATM menu is displayed with different options:
1. **Check Balance** – Displays the current account balance.
2. **Withdraw Money** – Allows withdrawal while checking the balance, withdrawal limit, and valid amount.
3. **Deposit Money** – Adds money to the account after validating the amount.
4. **Mini Statement** – Displays recent transactions.
5. **Change PIN** – Allows the user to securely update their 4-digit PIN.
6. **Exit** – Displays the final balance, number of transactions, and session date/time.

## ▶️ How to Run
1. Make sure **Python 3** is installed.
2. Save the code as:
```text
atm_simulation.py
```
3. Run the following command:
```bash
python ATM_Simulation.py
```
4. Enter the default PIN `1234` to access the ATM.

## 📚 Python Concepts Used
This project demonstrates practical use of:
* Variables and data types
* Conditional statements
* `for` and `while` loops
* Lists for transaction storage
* `try-except` for error handling
* User input validation
* String formatting
* `datetime` for date and time

## 🎯 Learning Outcome
Through this project, I practiced building a menu-driven Python application and learned how to handle user input, account balance operations, transaction records, validation, and basic security logic.

## 👩‍💻 Internship
**Python Developer Intern — Arch Technologies**
Developed as an internship task to demonstrate practical Python programming and problem-solving skills.
