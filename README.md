# 🐍 Python Developer Internship — Arch Technologies

Welcome to my **Python Developer Internship** project repository at **Arch Technologies**.

This repository contains the projects and practical tasks I completed during my **two-month internship**, with a focus on developing Python programming skills through hands-on command-line applications.

Throughout the internship, I progressed from fundamental Python programming concepts to more structured applications involving game logic, data management, input validation, authentication, transaction processing, and application state management.

---

## 📌 Internship Overview

During this two-month internship, I completed **four Python-based projects** divided into two monthly task sets.

| Month      | Task   | Project                   | Main Focus                                                |
| ---------- | ------ | ------------------------- | --------------------------------------------------------- |
| 📅 Month 1 | Task 1 | 🎲 Dice Rolling Game      | Randomization, lists, tuples, functions, statistics       |
| 📅 Month 1 | Task 2 | 📝 To-Do List Application | Lists, dictionaries, task management, validation          |
| 📅 Month 2 | Task 1 | 🎯 Number Guessing Game   | Game logic, difficulty levels, scoring, loops             |
| 📅 Month 2 | Task 2 | 🏧 ATM Simulation         | Authentication, transactions, validation, data management |

---

# 📂 Repository Structure

```text
Arch_Technologies_Internship_Python_Developer/
│
├── Month_1_Task/
│   │
│   ├── Task_1/
│   │   ├── Dice_Rolling_Game.py
│   │   └── README.md
│   │
│   ├── Task_2/
│   │   ├── To_Do_List_Application.py
│   │   └── README.md
│   │
│   └── README.md
│
├── Month_2_Task/
│   │
│   ├── Task_1/
│   │   ├── Number_guessing_Game.py
│   │   └── README.md
│   │
│   ├── Task_2/
│   │   ├── ATM_Simulation.py
│   │   └── README.md
│   │
│   └── README.md
│
└── README.md
```

---

# 📅 Month 1 — Python Fundamentals

The first month focused on strengthening core Python programming concepts by developing simple but functional command-line applications.

The projects helped me practice Python syntax, functions, data structures, loops, conditions, user input, and basic data processing.

---

## 🎲 Task 1 — Dice Rolling Game

The **Dice Rolling Game** is a Python command-line application that allows users to roll two six-sided dice and analyze their results.

### ✨ Features

* 🎲 Roll two six-sided dice
* 🔢 Calculate the total score
* 🔥 Detect doubles
* ⭐ Detect Lucky 7
* 🏆 Detect the highest possible score
* 📜 Maintain complete roll history
* 📊 Display game statistics
* 📈 Calculate average score
* ❌ Handle invalid menu choices
* 🚪 Exit with a game summary

### 🧠 Concepts Practiced

* `random` module
* `random.randint()`
* Functions
* Lists
* Tuples
* `while` loops
* Conditional statements
* `max()`
* `min()`
* `sum()`
* User input/output
* f-strings

### ▶️ Run

```bash
cd Month_1_Task/Task_1
python Dice_Rolling_Game.py
```

### 📖 Documentation

[View Dice Rolling Game Documentation](./Month_1_Task/Task_1/README.md)

---

## 📝 Task 2 — To-Do List Application

The **To-Do List Application** is a command-line task management system that allows users to create and manage tasks.

Each task contains a task name and completion status.

### ✨ Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Remove completed tasks
* 📊 View task summary
* 📈 Display progress percentage
* 🔢 Track completed and pending tasks
* ❌ Validate empty task names
* ⚠️ Handle invalid task numbers
* 🚪 Exit the application

### 🧠 Concepts Practiced

* Functions
* Lists
* Dictionaries
* Boolean values
* `while` loops
* Conditional statements
* `enumerate()`
* `sum()`
* `len()`
* `try-except`
* List comprehensions
* Generator expressions
* `input()` and `print()`
* f-strings

### ▶️ Run

```bash
cd Month_1_Task/Task_2
python To_Do_List_Application.py
```

### 📖 Documentation

[View To-Do List Documentation](./Month_1_Task/Task_2/README.md)

---

# 📅 Month 2 — Practical Python Applications

The second month focused on building more interactive applications and applying Python concepts to more complete problem-solving scenarios.

The projects introduced additional concepts such as difficulty-based logic, scoring systems, authentication, transaction processing, input validation, and session management.

---

## 🎯 Task 1 — Number Guessing Game

The **Number Guessing Game** is an interactive Python command-line game where the player attempts to guess a randomly generated number within a limited number of attempts.

The game includes multiple difficulty levels, hints, scoring, and multiple rounds.

### ✨ Features

* 👤 Player name input
* 🎮 Three difficulty levels
* 🔢 Random number generation
* ❤️ Limited attempts
* ⬆️ Too High / Too Low hints
* 🔥 Close-number hints
* ⭐ Difficulty-based scoring
* 🔄 Multiple rounds
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
* `for` and `while` loops
* Conditional statements
* `try-except`
* Arithmetic operations
* Score calculation
* Input validation
* String formatting
* Game flow management

### ▶️ Run

```bash
cd Month_2_Task/Task_1
python Number_guessing_Game.py
```

### 📖 Documentation

[View Number Guessing Game Documentation](./Month_2_Task/Task_1/README.md)

---

## 🏧 Task 2 — ATM Simulation

The **ATM Simulation** is a Python command-line application that simulates common ATM operations.

Users authenticate with a PIN before accessing their account. After successful authentication, they can check their balance, withdraw and deposit money, view transaction history, and change their PIN.

### ✨ Features

* 🔐 PIN verification with 3 attempts
* 👤 Account holder information
* 💰 Balance inquiry
* 💵 Money withdrawal
* 💳 Money deposit
* 📋 Mini statement
* 🔐 PIN change
* 🧾 Session summary
* 🕐 Current date and time
* ⚠️ Input validation
* 💸 Withdrawal and deposit limits
* 🔢 Withdrawal amount validation
* 🚪 Secure session exit

### 💳 Transaction Rules

| Operation          | Rule                            |
| ------------------ | ------------------------------- |
| PIN Login          | Maximum 3 attempts              |
| Withdrawal         | Greater than Rs. 0              |
| Withdrawal         | Multiple of Rs. 500             |
| Maximum Withdrawal | Rs. 20,000                      |
| Withdrawal         | Cannot exceed available balance |
| Deposit            | Greater than Rs. 0              |
| Maximum Deposit    | Rs. 100,000                     |
| New PIN            | Exactly 4 digits                |
| PIN Change         | Must be different from old PIN  |

### 🧠 Concepts Practiced

* Variables
* Functions
* Lists
* Loops
* Conditional statements
* `try-except`
* Input validation
* String methods
* Transaction management
* `datetime`
* `append()`
* `len()`
* `break`
* f-strings

### ▶️ Run

```bash
cd Month_2_Task/Task_2
python ATM_Simulation.py
```

### 📖 Documentation

[View ATM Simulation Documentation](./Month_2_Task/Task_2/README.md)

---

# 🛠️ Technologies & Tools

The projects developed during the internship primarily use Python and its standard library.

### Programming

* 🐍 **Python 3**
* Python Standard Library

### Python Modules

* `random`
* `datetime`

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Command Line / Terminal

### Documentation

* Markdown
* GitHub README files

No external Python packages are required to run these projects.

---

# 🧠 Python Skills Developed

Throughout the two-month internship, I practiced and strengthened a range of Python programming concepts.

### 🔹 Python Fundamentals

* Variables
* Data types
* Operators
* Input/output
* String manipulation
* Type conversion

### 🔹 Control Flow

* `if`
* `elif`
* `else`
* `for` loops
* `while` loops
* `break`
* Nested conditions

### 🔹 Functions

* Creating functions
* Reusable program logic
* Passing arguments
* Returning values
* Organizing application logic

### 🔹 Data Structures

* Lists
* Tuples
* Dictionaries
* Boolean values

### 🔹 Error Handling

* `try-except`
* Input validation
* Handling invalid menu choices
* Handling invalid numerical input

### 🔹 Data Processing

* `sum()`
* `min()`
* `max()`
* `len()`
* `enumerate()`
* List comprehensions
* Generator expressions

### 🔹 Application Logic

* Random number generation
* Game state management
* Score calculation
* Attempt tracking
* Progress calculation
* Balance management
* Transaction tracking
* Authentication logic

---

# 📈 Internship Learning Progress

The projects represent a gradual progression in Python development.

```text
                 🐍 PYTHON DEVELOPER INTERNSHIP
                              │
                              ▼
                    📅 MONTH 1
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
      🎲 Dice Rolling                    📝 To-Do List
             │                                 │
      Randomization                       Data Structures
      Functions                           Lists
      Tuples                             Dictionaries
      Statistics                         Task Management
             │                                 │
             └────────────────┬────────────────┘
                              ▼
                    📅 MONTH 2
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
      🎯 Number Guessing                 🏧 ATM Simulation
             │                                 │
      Game Logic                         Authentication
      Difficulty                         Transactions
      Scoring                            Validation
      Attempts                           Balance Management
      Multiple Rounds                    Session Management
             │                                 │
             └────────────────┬────────────────┘
                              ▼
                    🚀 PRACTICAL PYTHON
                              │
                              ▼
                  PROBLEM-SOLVING SKILLS
```

---

# 📊 Project Comparison

| Project                 | Main Concepts                                       | Application Type   |
| ----------------------- | --------------------------------------------------- | ------------------ |
| 🎲 Dice Rolling Game    | Randomization, functions, lists, tuples, statistics | Game               |
| 📝 To-Do List           | Lists, dictionaries, task management, validation    | Productivity       |
| 🎯 Number Guessing Game | Randomization, loops, scoring, difficulty           | Game               |
| 🏧 ATM Simulation       | Authentication, transactions, validation, lists     | Banking Simulation |

---

# 🎯 Internship Objectives

The main objectives of this internship were to gain practical experience with Python programming and apply programming concepts to real-world-style problems.

During the two months, I worked on:

* Building command-line applications
* Understanding application requirements
* Designing program logic
* Working with Python data structures
* Creating reusable functions
* Implementing input validation
* Handling errors and unexpected input
* Managing application state
* Processing and displaying data
* Creating interactive user interfaces through the terminal
* Organizing projects into structured folders
* Writing project documentation
* Using Git and GitHub for project management

---

# 🚀 Future Learning

The foundation developed through these projects can be extended toward more advanced Python development areas, including:

* Object-Oriented Programming
* File handling
* JSON and CSV data processing
* Database integration
* REST APIs
* Web development with Flask or FastAPI
* Automation and scripting
* Testing and debugging
* Data analysis
* Machine Learning
* Artificial Intelligence

---

# 📚 Internship Projects

### Month 1

* 🎲 [Dice Rolling Game](./Month_1_Task/Task_1/)
* 📝 [To-Do List Application](./Month_1_Task/Task_2/)

### Month 2

* 🎯 [Number Guessing Game](./Month_2_Task/Task_1/)
* 🏧 [ATM Simulation](./Month_2_Task/Task_2/)

---

# 👩‍💻 Author

**Aqsa Saqib**

**Python Developer Intern — Arch Technologies**

---

# 📄 License

These projects were developed for **educational and internship learning purposes** as part of my Python Developer Internship at **Arch Technologies**.
