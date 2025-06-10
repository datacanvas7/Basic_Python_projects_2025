# %% [markdown]
# # To-Do List Application
# 
# This application allows you to manage tasks with basic CRUD (Create, Read, Update, Delete) operations and file handling. It uses a **priority queue** (implemented with `deque`) to prioritize tasks.

# %% [markdown]
# ## Features
# - **Add Tasks**: Add tasks with optional priority (`high`, `medium`, `low`).
# - **Delete Tasks**: Delete tasks by their index.
# - **Show Tasks**: Display all tasks in the to-do list.
# - **Save Tasks**: Tasks are saved to a file (`todo_list.txt`) and loaded automatically when the application starts.

# %% [markdown]
# ## Code Explanation
# 
# ### 1. **Initialization**
# - The `ToDoList` class initializes a `deque` to store tasks and a file (`todo_list.txt`) to save tasks.
# - Tasks are loaded from the file (if it exists) when the application starts.
# 
# ### 2. **Add Task**
# - The `add_task` method adds a task to the to-do list with an optional priority.
#   - `high` priority tasks are added to the front of the queue.
#   - `medium` priority tasks are added to the middle.
#   - `low` priority tasks are added to the end.
# 
# ### 3. **Delete Task**
# - The `delete_task` method removes a task by its index.
# 
# ### 4. **Show Tasks**
# - The `show_tasks` method displays all tasks in the to-do list.
# 
# ### 5. **Interactive Menu**
# - The `interactive_todo_list` function provides a menu-driven interface to:
#   - Add tasks (with custom input for task and priority).
#   - Delete tasks (by task number).
#   - Show all tasks.
#   - Exit the application.

# %% [markdown]
# ---
# # Code Attached

# %%
# Import required libraries
import os
from collections import deque

# Markdown: ## To-Do List Application
# This application allows you to manage tasks with basic CRUD operations and file handling.

class ToDoList:
    def __init__(self):
        # Initialize a deque to store tasks (priority queue)
        self.tasks = deque()
        # File to save tasks
        self.filename = "todo_list.txt"
        # Load tasks from file if it exists
        self.load_tasks()

    def load_tasks(self):
        """
        Load tasks from a file if it exists.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    task = line.strip()
                    if task:  # Avoid empty lines
                        self.tasks.append(task)

    def save_tasks(self):
        """
        Save tasks to a file.
        """
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task, priority="low"):
        """
        Add a task to the to-do list with optional priority.
        Priority can be 'low', 'medium', or 'high'.
        """
        if priority == "high":
            self.tasks.appendleft(task)  # Add to the front of the queue
        elif priority == "medium":
            # Add to the middle (approximation)
            mid = len(self.tasks) // 2
            self.tasks.insert(mid, task)
        else:
            self.tasks.append(task)  # Add to the end of the queue
        print(f"Task added: {task} (Priority: {priority})")
        self.save_tasks()

    def delete_task(self, task_index):
        """
        Delete a task by its index.
        """
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks[task_index]
            del self.tasks[task_index]
            print(f"Task deleted: {removed_task}")
            self.save_tasks()
        else:
            print("Invalid task index!")

    def show_tasks(self):
        """
        Display all tasks in the to-do list.
        """
        if not self.tasks:
            print("No tasks in the to-do list!")
        else:
            print("🌟 Your To-Do List 🌟")
            for idx, task in enumerate(self.tasks):
                print(f"{idx + 1}. {task}")

# Markdown: ## Interactive To-Do List
# Below is an example of how to use the ToDoList class interactively in a Jupyter Notebook.

def interactive_todo_list():
    """
    Interactive function to add, delete, and show tasks.
    """
    # Initialize the to-do list
    todo = ToDoList()

    while True:
        print("\n📝 To-Do List Menu 📝")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            # Add a task
            task = input("Enter the task: ")
            priority = input("Enter priority (high/medium/low): ").lower()
            if priority not in ["high", "medium", "low"]:
                print("Invalid priority! Defaulting to 'low'.")
                priority = "low"
            todo.add_task(task, priority)

        elif choice == "2":
            # Delete a task
            todo.show_tasks()
            task_index = input("Enter the task number to delete: ")
            if task_index.isdigit():
                todo.delete_task(int(task_index) - 1)  # Convert to 0-based index
            else:
                print("Invalid task number!")

        elif choice == "3":
            # Show all tasks
            todo.show_tasks()

        elif choice == "4":
            # Exit the program
            print("Exiting the to-do list. Goodbye! 👋")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the interactive to-do list
interactive_todo_list()

# %%



