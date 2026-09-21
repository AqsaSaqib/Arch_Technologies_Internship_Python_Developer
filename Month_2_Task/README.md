# 🐍 Month 2 — Python Developer Internship

This folder contains the **Month 2 tasks** completed as part of my **Python Developer Internship at Arch Technologies**.

The projects in Month 2 focus on developing more interactive command-line applications using Python. These tasks build upon fundamental programming concepts and introduce practical features such as difficulty levels, scoring systems, input validation, authentication, transaction management, and session summaries.

---

## 📌 Month 2 Overview

During Month 2, I developed two Python command-line applications:

| Task      | Project                  | Description                                                                                                                         |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| 🎯 Task 1 | **Number Guessing Game** | An interactive guessing game with multiple difficulty levels, limited attempts, hints, scoring, and multiple rounds.                |
| 🏧 Task 2 | **ATM Simulation**       | A simulated ATM system with PIN authentication, balance management, deposits, withdrawals, transaction history, and PIN management. |

---

## 📂 Project Structure

```text
Month_2_Task/
│
├── Task_1/
│   ├── Number_guessing_Game.py
│   └── README.md
│
├── Task_2/
│   ├── ATM_Simulation.py
│   └── README.md
│
└── README.md
```

---

# 🎯 Task 1 — Number Guessing Game

The **Number Guessing Game** is an interactive Python command-line game where the player attempts to guess a randomly generated number within a limited number of attempts.

The game provides different difficulty levels, helpful hints, and a scoring system based on the player's performance.

### ✨ Features

* 👤 Player name input
* 🎮 Three difficulty levels
* 🔢 Random number generation
* ❤️ Difficulty-based attempt limits
* ⬆️ Too High / Too Low hints
* 🔥 Close-number hints
* ⭐ Difficulty-based scoring
* 🔄 Multiple game rounds
* 🛡️ Input validation
* 📊 Total score tracking
* 🏆 Rounds won tracking
* 🧾 Final game summary

### 🎯 Difficulty Levels

| Difficulty | Number Range | Attempts |
| ---------- | ------------ | -------- |
| Easy       | 1–50         | 8        |
| Medium     | 1–100        | 7        |
| Hard       | 1–200        | 6        |

### 🧠 Concepts Practiced

* `random` module
* `random.randint()`
* Variables
* Loops
* Conditional statements
* `try-except`
* User input/output
* Arithmetic operations
* Score calculation
* String formatting
* Game flow management

### ▶️ Run the Game

Open a terminal inside the `Task_1` directory and run:

```bash
python Number_guessing_Game.py
```

### 📖 Documentation

For complete game features, scoring rules, gameplay examples, and implementation details, see:

**[Task 1 — Number Guessing Game README](./Task_1/README.md)**

---

# 🏧 Task 2 — ATM Simulation

The **ATM Simulation** is a Python command-line application that simulates common ATM operations.

Users must authenticate using a PIN before accessing their account. After successful login, they can check their balance, withdraw or deposit money, view transaction history, and change their PIN.

### ✨ Features

* 🔐 PIN verification with 3 attempts
* 👤 Account holder information
* 💰 Balance inquiry
* 💵 Money withdrawal
* 💳 Money deposit
* 📋 Mini statement
* 🔐 PIN change functionality
* 🧾 Session summary
* 🕐 Current date and time
* ⚠️ Input validation
* 💸 Withdrawal and deposit limits
* 🔢 Withdrawal amount validation
* 🚪 Secure session exit

### 💳 Transaction Rules

| Operation          | Rule                             |
| ------------------ | -------------------------------- |
| PIN Login          | Maximum 3 attempts               |
| Withdrawal         | Must be greater than Rs. 0       |
| Withdrawal         | Must be a multiple of Rs. 500    |
| Maximum Withdrawal | Rs. 20,000                       |
| Withdrawal         | Cannot exceed available balance  |
| Deposit            | Must be greater than Rs. 0       |
| Maximum Deposit    | Rs. 100,000                      |
| New PIN            | Exactly 4 digits                 |
| PIN Change         | New PIN must differ from old PIN |

### 🧠 Concepts Practiced

* Variables
* Functions and program logic
* Lists
* Loops
* Conditional statements
* `try-except`
* Input validation
* String methods
* Transaction management
* `datetime` module
* `append()`
* `len()`
* f-strings
* `break`

### ▶️ Run the Application

Open a terminal inside the `Task_2` directory and run:

```bash
python ATM_Simulation.py
```

### 🔑 Sample Account Details

```text
Account Holder : Aqsa
PIN            : 1234
Initial Balance: Rs. 50,000
```

> **Note:** These are sample credentials used for this educational project.

### 📖 Documentation

For complete ATM functionality, transaction rules, usage instructions, and implementation details, see:

**[Task 2 — ATM Simulation README](./Task_2/README.md)**

---

# 🛠️ Technologies Used

The Month 2 projects were developed using:

* **Python 3**
* Python Standard Library
* `random` module
* `datetime` module
* Command-Line Interface (CLI)
* VS Code / Python IDE
* Git & GitHub

No external Python packages are required to run these applications.

---

# 🧠 Skills Demonstrated

Month 2 provided practical experience with the following programming skills:

### 🔹 Control Flow

* `if/elif/else`
* `for` loops
* `while` loops
* `break`
* Nested conditions

### 🔹 Functions & Program Organization

* Creating reusable functions
* Separating application logic
* Managing program flow
* Returning and updating values

### 🔹 Data Handling

* Lists
* Variables
* String manipulation
* Numeric data
* Transaction records

### 🔹 Input Validation

* Validating numeric input
* Handling invalid menu choices
* Using `try-except`
* Validating PIN formats
* Validating transaction amounts

### 🔹 Logic & Calculations

* Random number generation
* Score calculation
* Attempt tracking
* Balance calculation
* Transaction processing
* Difference and comparison calculations

### 🔹 User Interaction

* Interactive CLI menus
* User-friendly messages
* Game hints
* Account authentication
* Formatted summaries

---

# 📈 Month 2 Learning Progress

| Area             | What I Practiced                           |
| ---------------- | ------------------------------------------ |
| Randomization    | Generating random numbers                  |
| Game Logic       | Difficulty, attempts, hints, scoring       |
| Input Validation | Handling invalid user input                |
| Error Handling   | Using `try-except`                         |
| Authentication   | PIN-based login                            |
| Data Management  | Managing balances and transactions         |
| Loops            | Repeated gameplay and ATM sessions         |
| Lists            | Storing transaction data                   |
| Date & Time      | Recording session information              |
| Problem Solving  | Designing application logic                |
| CLI Development  | Building interactive terminal applications |
| Documentation    | Creating structured GitHub README files    |

---

# 🎯 Month 2 Objective

The main objective of Month 2 was to move beyond basic Python exercises and develop more complete, interactive applications.

By completing these projects, I gained practical experience in:

* Designing applications around user requirements
* Implementing multi-step program logic
* Building interactive command-line interfaces
* Validating and handling user input
* Managing application state
* Implementing scoring and tracking systems
* Simulating authentication and transactions
* Organizing Python code into logical components
* Creating clear project documentation

---


# 📊 Month 2 Projects Summary

```text
                    MONTH 2
                       │
            ┌──────────┴──────────┐
            │                     │
            ▼                     ▼
     🎯 NUMBER GUESSING      🏧 ATM SIMULATION
            │                     │
            │                     │
      Game Logic             Banking Logic
      Difficulty             PIN Authentication
      Attempts               Balance Management
      Hints                  Deposits
      Scoring                Withdrawals
      Multiple Rounds        Transactions
            │                     │
            └──────────┬──────────┘
                       │
                       ▼
             🐍 PYTHON SKILLS
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
           Logic    Validation  Data
              │        │        │
              └────────┼────────┘
                       ▼
              Practical CLI Apps
```

---

# 👩‍💻 Author

**Aqsa Saqib**

Python Developer Intern — Arch Technologies

---

# 📄 License

These projects were created for **educational and internship learning purposes**.
