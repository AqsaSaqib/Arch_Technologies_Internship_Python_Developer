def show_progress(tasks):
    if not tasks:
        print("\nProgress: [----------] 0%")
        return
    completed = sum(task["completed"] for task in tasks)
    total = len(tasks)
    percentage = int((completed / total) * 100)
    filled = int(percentage / 10)
    empty = 10 - filled
    bar = "█" * filled + "-" * empty

    print(f"\nProgress: [{bar}] {percentage}%")
    print(f"Completed: {completed}/{total} tasks")

def add_task(tasks):
    task_name = input("\nEnter task: ").strip()

    if not task_name:
        print("❌ Task cannot be empty.")
        return
    tasks.append({
        "name": task_name,
        "completed": False
    })
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("\n📋 No tasks available.")
        return
    print("\n" + "=" * 40)
    print("📋 YOUR TO-DO LIST")
    print("=" * 40)

    for i, task in enumerate(tasks, 1):
        if task["completed"]:
            status = "✓"
        else:
            status = " "

        print(f"{i}. [{status}] {task['name']}")
    show_progress(tasks)

def complete_task(tasks):
    if not tasks:
        print("\n❌ No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):

            if tasks[number - 1]["completed"]:
                print("⚠️ Task is already completed.")
            else:
                tasks[number - 1]["completed"] = True
                print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def remove_task(tasks):
    if not tasks:
        print("\n❌ No tasks available.")
        return
    view_tasks(tasks)

    try:
        number = int(input("\nEnter completed task number to remove: "))

        if 1 <= number <= len(tasks):

            if tasks[number - 1]["completed"]:
                removed = tasks.pop(number - 1)
                print(f"🗑️ Removed: {removed['name']}")
            else:
                print("⚠️ You can only remove completed tasks.")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

def show_summary(tasks):
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed
    print("\n📊 TASK SUMMARY")
    print("-" * 30)
    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")

    show_progress(tasks)

# Main Program
tasks = []
print("=" * 40)
print("       📝 TO-DO LIST APPLICATION")
print("=" * 40)

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Completed Task")
    print("5. Task Summary")
    print("6. Exit")
    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        remove_task(tasks)

    elif choice == "5":
        show_summary(tasks)

    elif choice == "6":
        print("\n👋 Thank you for using the To-Do List!")
        break

    else:
        print("\n❌ Invalid choice! Please select 1-6.")
