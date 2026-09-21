# 🎲 Dice Rolling Game

A simple **Python command-line Dice Rolling Game** where users can roll two dice, view their roll history, and check game statistics.

## 📌 Features

* 🎲 Roll two six-sided dice
* 🔢 Calculate the total of both dice
* 🔥 Detect **Doubles** when both dice have the same value
* ⭐ Detect **Lucky 7**
* 🏆 Detect the highest possible score (12)
* 📜 View complete roll history
* 📊 View game statistics

  * Total number of rolls
  * Highest score
  * Lowest score
  * Average score
* ❌ Handle invalid menu choices
* 🚪 Exit the game with a summary

## 🛠️ Technologies Used

* **Python 3**
* **random module**
* Python functions
* Lists
* Tuples
* Loops
* Conditional statements
* f-strings
* User input/output

## 📂 Project Structure

```text
dice-rolling-game/
│
├── dice_game.py
└── README.md
```

## ⚙️ How It Works

The program uses Python's built-in `random` module to generate random values between **1 and 6** for each die.

### 1. Roll the Dice

The `roll_dice()` function generates two random numbers:

```python
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
```

It returns both dice values.

### 2. Display the Result

The `show_result()` function displays:

* Die 1 value
* Die 2 value
* Total score

It also checks for special results such as:

* Doubles
* Lucky 7
* Highest possible score

### 3. Store Roll History

Every roll is stored in the `history` list as a tuple:

```python
(die1, die2, total)
```

For example:

```text
[(3, 5, 8), (6, 6, 12), (2, 5, 7)]
```

### 4. View Statistics

The `show_statistics()` function calculates:

* Number of rolls
* Highest total
* Lowest total
* Average total

The average is calculated using:

```python
sum(totals) / len(totals)
```

### 5. View History

The `show_history()` function displays every previous roll in an easy-to-read format.

Example:

```text
📜 ROLL HISTORY
------------------------------
Roll 1: 3 + 5 = 8
Roll 2: 6 + 6 = 12
Roll 3: 2 + 5 = 7
```

## 🚀 Installation

### Step 1: Install Python

Make sure **Python 3** is installed on your computer.

You can check by running:

```bash
python --version
```

### Step 2: Download or Clone the Project

Place the Python file and `README.md` in the same folder.

### Step 3: Run the Program

Open a terminal in the project directory and run:

```bash
python dice_game.py
```

## 🎮 How to Play

When the program starts, you will see the following menu:

```text
1. Roll Dice
2. View History
3. View Statistics
4. Exit
```

Enter a number from **1 to 4**.

### Option 1 — Roll Dice

Generates two random dice values and displays the result.

Example:

```text
==============================
🎲 DICE RESULT
==============================
Die 1       : 4
Die 2       : 3
Total       : 7
⭐ Lucky 7!
```

### Option 2 — View History

Displays all dice rolls made during the current game.

### Option 3 — View Statistics

Displays statistics such as:

```text
📊 GAME STATISTICS
------------------------------
Total Rolls : 5
Highest     : 12
Lowest      : 3
Average     : 7.40
```

### Option 4 — Exit

Exits the game and displays the total number of rolls.

## 🧠 Python Concepts Demonstrated

This project is useful for practicing basic Python programming concepts.

| Concept            | Usage                                      |
| ------------------ | ------------------------------------------ |
| `import`           | Importing the `random` module              |
| Functions          | Organizing the program into reusable parts |
| `random.randint()` | Generating random dice values              |
| Variables          | Storing dice values and totals             |
| Tuples             | Storing each roll                          |
| Lists              | Maintaining roll history                   |
| `while` loop       | Keeping the game running                   |
| `if/elif/else`     | Handling menu choices and conditions       |
| `input()`          | Getting user choices                       |
| `print()`          | Displaying results                         |
| `max()`            | Finding the highest score                  |
| `min()`            | Finding the lowest score                   |
| `sum()`            | Calculating the total                      |
| f-strings          | Formatting output                          |

## 📊 Example Gameplay

```text
===================================
🎲 WELCOME TO DICE ROLLING GAME 🎲
===================================

1. Roll Dice
2. View History
3. View Statistics
4. Exit

Enter your choice: 1

==============================
🎲 DICE RESULT
==============================
Die 1       : 6
Die 2       : 6
Total       : 12
🔥 DOUBLE! Both dice are the same!
🏆 Highest possible score!
```

## 🔮 Possible Future Improvements

The project can be extended with additional features such as:

* Add a player name
* Add a scoring system
* Add multiple players
* Add a winning/losing condition
* Save roll history to a file
* Add colored terminal output
* Add sound effects
* Add a graphical user interface (GUI)
* Add a leaderboard
* Add different types of dice

## 👩‍💻 Author

**Aqsa Saqib**

## 📄 License

This project is created for **educational and learning purposes**.
