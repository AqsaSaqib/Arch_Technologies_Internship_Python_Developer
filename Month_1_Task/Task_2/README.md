# 📝 To-Do List Application

A simple **Python command-line To-Do List Application** that allows users to add tasks, view tasks, mark tasks as completed, remove completed tasks, and track overall progress.

## 📌 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Remove completed tasks
* 📊 View task summary
* 📈 Display visual progress percentage
* 🔢 Show completed and pending tasks
* ❌ Validate empty task names
* ⚠️ Handle invalid task numbers and menu choices
* 🚪 Exit the application easily

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Lists
* Dictionaries
* `while` loops
* `if/elif/else` statements
* `try/except` error handling
* `input()` and `print()`
* List comprehensions/generator expressions
* String formatting (f-strings)

## 📂 Project Structure

```text
todo-list/
│
├── todo.py
└── README.md
```

## ⚙️ How It Works

The application stores tasks in a Python list.

Each task is represented using a dictionary containing:

```python
{
    "name": "Complete Python assignment",
    "completed": False
}
```

The `completed` value is either:

* `False` → Task is pending
* `True` → Task is completed

## 🚀 Installation

### Step 1: Install Python

Make sure **Python 3** is installed on your computer.

Check your Python version using:

```bash
python --version
```

### Step 2: Download the Project

Place the Python file and `README.md` in the same folder.

### Step 3: Run the Application

Open a terminal in the project directory and run:

```bash
python todo.py
```

> If your Python file has a different name, replace `todo.py` with your filename.

## 🎮 How to Use

When the application starts, the following menu is displayed:

```text
1. Add Task
2. View Tasks
3. Complete Task
4. Remove Completed Task
5. Task Summary
6. Exit
```

Enter a number from **1 to 6** to select an option.

### 1. Add Task

Allows the user to add a new task.

Example:

```text
Enter task: Complete Python assignment
✅ Task added successfully!
```

Empty task names are not accepted.

```text
Enter task:
❌ Task cannot be empty.
```

### 2. View Tasks

Displays all currently stored tasks.

Example:

```text
========================================
📋 YOUR TO-DO LIST
========================================
1. [✓] Complete Python assignment
2. [ ] Learn Functions
3. [ ] Practice Python
```

* `[✓]` means the task is completed.
* `[ ]` means the task is pending.

The progress bar is also displayed:

```text
Progress: [██████----] 66%
Completed: 2/3 tasks
```

### 3. Complete Task

Allows the user to mark a task as completed by entering its task number.

Example:

```text
Enter task number to complete: 2
✅ Task marked as completed!
```

If the task is already completed:

```text
⚠️ Task is already completed.
```

### 4. Remove Completed Task

Allows the user to remove a task **only after it has been completed**.

Example:

```text
Enter completed task number to remove: 2
🗑️ Removed: Learn Functions
```

Pending tasks cannot be removed:

```text
⚠️ You can only remove completed tasks.
```

### 5. Task Summary

Displays the overall task statistics.

Example:

```text
📊 TASK SUMMARY
------------------------------
Total Tasks     : 5
Completed Tasks : 3
Pending Tasks   : 2

Progress: [██████----] 60%
Completed: 3/5 tasks
```

### 6. Exit

Exits the application.

```text
👋 Thank you for using the To-Do List!
```

## 📈 Progress Calculation

The application calculates progress using the number of completed tasks compared with the total number of tasks.

For example:

```text
Total Tasks     = 5
Completed Tasks = 3
Pending Tasks   = 2
```

Therefore:

```text
Progress = 60%
```

The application represents progress using a 10-character progress bar:

```text
[██████----] 60%
```

## 🧠 Python Concepts Demonstrated

| Concept        | Usage                                           |
| -------------- | ----------------------------------------------- |
| Functions      | Dividing the application into reusable sections |
| Lists          | Storing all tasks                               |
| Dictionaries   | Representing individual tasks                   |
| Boolean values | Tracking task completion                        |
| `while` loop   | Keeping the application running                 |
| `if/elif/else` | Handling menu choices                           |
| `enumerate()`  | Displaying task numbers                         |
| `sum()`        | Counting completed tasks                        |
| `len()`        | Finding the number of tasks                     |
| `try/except`   | Handling invalid numerical input                |
| `input()`      | Getting user input                              |
| `print()`      | Displaying information                          |
| `pop()`        | Removing completed tasks                        |
| f-strings      | Formatting output                               |

## 🔄 Application Flow

```text
             ┌───────────────┐
             │     Start     │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  Show Menu    │
             └───────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
     Add Task    View Tasks   Complete
          │          │          │
          └──────────┼──────────┘
                     │
              Remove Task
                     │
              Task Summary
                     │
                     ▼
                Exit / Loop
```

## 👩‍💻 Author

**Aqsa Saqib**

## 📄 License

This project is created for **educational and learning purposes**.
