# 🏧 ATM Simulation

A simple **Python command-line ATM Simulation** that allows users to securely log in using a PIN and perform common banking operations such as checking balance, withdrawing money, depositing money, viewing transactions, and changing their PIN.

This project was developed as part of my **Python Developer Internship at Arch Technologies** to practice Python programming, input validation, loops, conditions, lists, and basic transaction management.

## 📌 Features

* 🔐 PIN verification with **3 login attempts**
* 👤 Display account holder name
* 💰 Check current account balance
* 💵 Withdraw money
* 💳 Deposit money
* 📋 View recent transaction history
* 🔐 Change account PIN
* 🧾 Display final session summary
* 🕐 Show current date and time
* ⚠️ Validate invalid user inputs
* 💸 Withdrawal and deposit limits
* 🔢 Withdrawal amount must be a multiple of Rs. 500
* 🚪 Securely exit the ATM session

## 🛠️ Technologies Used

* **Python 3**
* `datetime` module
* Python functions and built-in features
* Lists
* Loops
* Conditional statements
* Exception handling
* User input/output
* String formatting

## 📂 Project Structure

```text
Task_2/
│
├── ATM_Simulation.py
└── README.md
```

## ⚙️ How It Works

The program starts by displaying an ATM welcome screen and asks the user to enter their PIN.

The user has **three attempts** to enter the correct PIN. If all three attempts are incorrect, the account is locked and the program exits.

After successful login, the main ATM menu is displayed.

### 1. 🔐 PIN Login

The program verifies the user's PIN before allowing access to the account.

```python
for attempt in range(3):
    user_pin = input("Enter your PIN: ")
```

If the correct PIN is entered, the user can access all ATM operations.

If the PIN is incorrect three times, the account is locked.

### 2. 💰 Check Balance

The **Check Balance** option displays the user's current account balance.

Example:

```text
💰 Your Current Balance:
Rs. 50,000
```

The balance is updated automatically whenever a successful deposit or withdrawal is made.

### 3. 💵 Withdraw Money

The withdrawal option allows the user to withdraw money from their account.

The program checks several conditions before completing the transaction:

* Amount must be greater than zero
* Amount must be a multiple of Rs. 500
* Maximum withdrawal is Rs. 20,000
* Amount cannot exceed the available balance
* Invalid input is handled using `try-except`

Example:

```text
Enter withdrawal amount: Rs. 5000

✅ Withdrawal successful!
Amount withdrawn: Rs. 5,000
Remaining balance: Rs. 45,000
```

### 4. 💳 Deposit Money

Users can also deposit money into their account.

The program validates the amount before adding it to the balance.

The maximum deposit limit is **Rs. 100,000** per transaction.

Example:

```text
Enter deposit amount: Rs. 10000

✅ Deposit successful!
Amount deposited: Rs. 10,000
New balance: Rs. 60,000
```

### 5. 📋 Mini Statement

The **Mini Statement** option displays the user's recent transactions.

Transactions are stored in a Python list:

```python
transactions = []
```

Each successful deposit or withdrawal is added to the list.

The program displays the **latest five transactions**.

Example:

```text
📋 MINI STATEMENT
--------------------------------------------------
Recent Transactions:

1. Deposit - Rs. 10,000
2. Withdraw - Rs. 5,000
3. Deposit - Rs. 2,000

--------------------------------------------------
Current Balance: Rs. 57,000
```

### 6. 🔐 Change PIN

The user can change their existing PIN from the ATM menu.

The program first verifies the current PIN and then checks:

* New PIN contains exactly 4 digits
* New PIN is different from the old PIN
* New PIN confirmation matches

Example:

```text
Enter your current PIN: 1234
Enter new 4-digit PIN: 5678
Confirm new PIN: 5678

✅ PIN changed successfully!
```

### 7. 🧾 Session Summary

When the user exits the ATM, a final session summary is displayed.

It includes:

* Account holder name
* Total number of transactions
* Final account balance
* Current date and time

Example:

```text
==================================================
             🧾 SESSION SUMMARY
==================================================
Account Holder : Aqsa
Transactions   : 4
Final Balance  : Rs. 57,000
Date & Time    : 21-09-2026 07:30 PM

🙏 Thank you for using Python ATM!
💳 Please collect your card.
==================================================
```

## 🚀 Installation

### Step 1: Install Python

Make sure **Python 3** is installed on your computer.

You can check the installed version using:

```bash
python --version
```

### Step 2: Download or Clone the Project
Download the project or clone the repository and open the ATM project folder.
Make sure the following files are available:
```text
Task_2/
├── ATM_Simulation.py
└── README.md
```

### Step 3: Run the Program
Open a terminal in the project directory and run:
```bash
python ATM_Simulation.py
```

## 🔑 Default Account Details
```text
Account Holder : Aqsa
PIN            : 1234
Initial Balance: Rs. 50,000
```
> **Note:** These are sample credentials used for this educational project.

## 🎮 How to Use
After successful login, the following menu is displayed:
```text
1. 💰 Check Balance
2. 💵 Withdraw Money
3. 💳 Deposit Money
4. 📋 Mini Statement
5. 🔐 Change PIN
6. 🚪 Exit
```
Enter an option from **1 to 6** to perform the desired operation.

### Option 1 — Check Balance
Displays the current account balance.

### Option 2 — Withdraw Money
Allows the user to withdraw money after checking the withdrawal rules and available balance.

### Option 3 — Deposit Money
Adds money to the account after validating the deposit amount.

### Option 4 — Mini Statement
Displays the latest five successful transactions.

### Option 5 — Change PIN
Allows the user to change their existing 4-digit PIN.

### Option 6 — Exit
Ends the ATM session and displays the final account summary.

## 🧠 Python Concepts Demonstrated
This project demonstrates several important Python programming concepts:
| **Concept**    | **Usage**                                 |
| -------------- | ----------------------------------------- |
| Variables      | Storing account details, PIN, and balance |
| `input()`      | Taking user input                         |
| `if/elif/else` | Handling conditions and menu options      |
| `for` loop     | Limiting PIN login attempts               |
| `while` loop   | Keeping the ATM menu running              |
| Lists          | Storing transaction history               |
| `try-except`   | Handling invalid numeric input            |
| `append()`     | Adding transactions to the list           |
| `len()`        | Counting transactions                     |
| `datetime`     | Displaying current date and time          |
| f-strings      | Formatting output                         |
| String methods | Validating and processing PIN input       |
| `break`        | Exiting loops and ending the session      |

## 📊 Transaction Rules
| **Operation**      | **Rule**                      |
| ------------------ | ----------------------------- |
| PIN Attempts       | Maximum 3 attempts            |
| Withdrawal         | Must be greater than Rs. 0    |
| Withdrawal         | Must be a multiple of Rs. 500 |
| Maximum Withdrawal | Rs. 20,000                    |
| Withdrawal         | Cannot exceed account balance |
| Deposit            | Must be greater than Rs. 0    |
| Maximum Deposit    | Rs. 100,000                   |
| New PIN            | Exactly 4 digits              |
| PIN Change         | New PIN must be different     |

## 📸 Example Gameplay
```text
==================================================
             🏧 PYTHON ATM
==================================================
Enter your PIN: 1234
✅ Login successful!
==================================================
Welcome, Aqsa!
==================================================

1. 💰 Check Balance
2. 💵 Withdraw Money
3. 💳 Deposit Money
4. 📋 Mini Statement
5. 🔐 Change PIN
6. 🚪 Exit

Choose an option (1-6): 2

💵 WITHDRAW MONEY
Enter withdrawal amount: Rs. 5000

✅ Withdrawal successful!
Amount withdrawn: Rs. 5,000
Remaining balance: Rs. 45,000
```

## 👩‍💻 Author
**Aqsa Saqib**
**Python Developer Intern — Arch Technologies**

## 📄 License
This project is created for **educational and internship learning purposes**.
