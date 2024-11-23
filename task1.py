tasks = []

# Function to add a task
def add_task(title):
    tasks.append({'title': title, 'completed': False})

# Function to view tasks
def view_tasks():
    for task in tasks:
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"Task: {task['title']}, Status: {status}")

# Function to remove a task
def remove_task(title):
    global tasks
    tasks = [task for task in tasks if task['title'] != title]

# Function to mark a task as complete
def complete_task(title):
    for task in tasks:
        if task['title'] == title:
            task['completed'] = True
            break

# Main program loop
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Complete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Enter task title: ")
        add_task(title)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        title = input("Enter task title to remove: ")
        remove_task(title)
    elif choice == '4':
        title = input("Enter task title to complete: ")
        complete_task(title)
    elif choice == '5':
        break
    else:
        print("Invalid option. Try again.")
