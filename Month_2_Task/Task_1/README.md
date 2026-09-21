# 🎯 Number Guessing Game
A simple and interactive **Python command-line Number Guessing Game** developed as part of my **Python Developer Internship at Arch Technologies**.

The game allows the player to choose a difficulty level, guess a randomly generated number within a limited number of attempts, receive helpful hints, and earn a score based on their performance.

## 📌 Features
* 👤 Player name input
* 🎮 Three difficulty levels
* 🔢 Random number generation
* ❤️ Limited attempts based on difficulty
* ⬆️ Too High and Too Low hints
* 🔥 Close-number hints
* ⭐ Difficulty-based scoring system
* 🔄 Multiple game rounds
* 🛡️ Input validation
* 📊 Total score tracking
* 🏆 Rounds won tracking
* 🧾 Final game summary

## 🛠️ Technologies Used
* **Python 3**
* `random` module
* Variables
* Loops
* Conditional statements
* Exception handling
* User input/output
* String formatting

## 📂 Project Structure

```text
Task_1/
│
├── Number_guessing_Game.py
└── README.md
```

## ⚙️ How It Works
The game starts by asking the player to enter their name. After that, the player can select one of three difficulty levels.

Each difficulty level has a different number range and number of attempts. The program then generates a random secret number and gives the player a limited number of chances to guess it.

### 1. 👤 Player Name
The program first asks the player to enter their name.

```python
player = input("Enter your name: ").strip()
```

The entered name is later displayed in the final game results.

### 2. 🎮 Select Difficulty
The player can choose from three difficulty levels:

```text
1. Easy   (1 - 50, 8 attempts)
2. Medium (1 - 100, 7 attempts)
3. Hard   (1 - 200, 6 attempts)
```

Each level provides a different number range and number of attempts.

## 🎯 Difficulty Levels

| **Difficulty** | **Number Range** | **Attempts** |
| -------------- | ---------------: | -----------: |
| Easy           |           1 - 50 |            8 |
| Medium         |          1 - 100 |            7 |
| Hard           |          1 - 200 |            6 |

### 3. 🔢 Generate Random Number
After selecting the difficulty, the program generates a secret number using Python's `random` module.

```python
secret_number = random.randint(minimum, maximum)
```

The player does not know this number and must guess it within the available attempts.

### 4. ❤️ Limited Attempts
The number of attempts depends on the selected difficulty.

For example, Easy mode gives the player **8 attempts**, while Hard mode gives only **6 attempts**.

The program keeps track of the remaining attempts:

```python
remaining = max_attempts - attempts
```

### 5. ⬆️ Guess Hints
After every valid guess, the program provides feedback.

If the guess is smaller than the secret number:

```text
⬆️ Too low!
```

If the guess is greater than the secret number:

```text
⬇️ Too high!
```

This helps the player move closer to the correct answer.

### 6. 🔥 Close Number Hint
The game also provides additional hints when the player's guess is close to the secret number.

For example:

```text
🔥 Very close!
```

or:

```text
🙂 You're getting closer.
```

The hint depends on the difference between the guess and the secret number.

### 7. ⭐ Scoring System
The player receives points when they guess the correct number.

The score depends on:

* Number of attempts used
* Selected difficulty level

Medium and Hard difficulty provide additional bonus points.

The total score is stored throughout the game:

```python
total_score += score
```

### 8. 🔄 Multiple Rounds
After completing a round, the player can choose whether to continue playing.

```text
Do you want to play another round? (yes/no):
```

If the player selects **yes**, a new round starts with a new random number.

If the player selects **no**, the game ends and displays the final results.

## 🏆 Final Results
When the player exits the game, a final summary is displayed.

It includes:

* Player name
* Total rounds won
* Total score
* Performance message

Example:

```text
==================================================
             📊 FINAL RESULTS
==================================================
👤 Player       : Aqsa
🏆 Rounds Won   : 3
⭐ Total Score  : 110

🔥 Excellent performance!
==================================================
       Thanks for playing! 🎯
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

Download the project or place the Python file and `README.md` inside the same project folder.

```text
Task_1/
├── Number_guessing_Game.py
└── README.md
```

### Step 3: Run the Program

Open a terminal in the project directory and run:

```bash
python Number_guessing_Game.py
```

## 🎮 How to Play

When the program starts, enter your name and select a difficulty level.

```text
==================================================
       🎯 NUMBER GUESSING GAME
==================================================

Enter your name: Aqsa

Choose Difficulty:
1. Easy   (1 - 50, 8 attempts)
2. Medium (1 - 100, 7 attempts)
3. Hard   (1 - 200, 6 attempts)

Enter choice (1-3): 2
```

The program then generates a secret number.

```text
--------------------------------------------------
🎮 Medium Mode
I'm thinking of a number between 1 and 100.
You have 7 attempts.
--------------------------------------------------

Attempts remaining: 7
Enter your guess: 50

⬆️ Too low!
```

Continue guessing until:

* 🎉 You guess the correct number
* 💀 You use all available attempts

After the round, you can choose to play again or exit.

## 🧠 Python Concepts Demonstrated

| **Concept**            | **Usage**                                        |
| ---------------------- | ------------------------------------------------ |
| Variables              | Storing player, score, attempts, and numbers     |
| `random.randint()`     | Generating the secret number                     |
| `if/elif/else`         | Handling difficulty and guessing conditions      |
| `while` loop           | Running the guessing process and multiple rounds |
| `for` loop             | Validating difficulty selection                  |
| `try-except`           | Handling invalid numeric input                   |
| `input()`              | Taking player input                              |
| Lists                  | Handling valid choices                           |
| Arithmetic operators   | Calculating score and number difference          |
| `break`                | Ending rounds and loops                          |
| String formatting      | Displaying game information                      |
| Functions/method logic | Organizing the game flow                         |

## 📊 Scoring Rules

The basic score is calculated according to the number of attempts remaining.

```python
score = (max_attempts - attempts + 1) * 10
```

Additional bonus points are awarded for higher difficulty levels:

| **Difficulty** | **Bonus** |
| -------------- | --------: |
| Easy           |         0 |
| Medium         |       +10 |
| Hard           |       +20 |

This means that successfully completing a harder level can result in a higher score.

## 📸 Example Gameplay

```text
==================================================
       🎯 NUMBER GUESSING GAME
==================================================

Enter your name: Aqsa

Choose Difficulty:
1. Easy   (1 - 50, 8 attempts)
2. Medium (1 - 100, 7 attempts)
3. Hard   (1 - 200, 6 attempts)

Enter choice (1-3): 1

--------------------------------------------------
🎮 Easy Mode
I'm thinking of a number between 1 and 50.
You have 8 attempts.
--------------------------------------------------

Attempts remaining: 8
Enter your guess: 25

⬆️ Too low!

Attempts remaining: 7
Enter your guess: 38

🔥 Very close!

Attempts remaining: 6
Enter your guess: 40

🎉 CONGRATULATIONS!
🎯 You guessed the number: 40
🔢 Attempts used: 3
⭐ Score earned: 60
```

## 👩‍💻 Author
**Aqsa Saqib**
**Python Developer Intern — Arch Technologies**

## 📄 License
This project is created for **educational and internship learning purposes**.
