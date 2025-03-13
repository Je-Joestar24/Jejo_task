# Jejo Task Manager 1

import json
import os
from typing import List, Dict

class TaskManager:
    """A command-line task manager application for managing tasks."""
    
    def __init__(self, filename: str = "task/tasks.json"):
        """Initialize TaskManager with a file for persistent storage.
        
        Args:
            filename (str): Name of the JSON file to store tasks
        """
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from the JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
        except json.JSONDecodeError:
            print("Error reading tasks file. Starting with empty task list.")
            self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to the JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, title: str) -> None:
        """Add a new task to the list.
        
        Args:
            title (str): Title of the task
        """
        task_id = self.tasks[len(self.tasks) - 1]['id'] + 1
        task = {
            "id": task_id,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def list_tasks(self) -> None:
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nCurrent Tasks:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['title']}")
        print("-" * 50)

    def update_task(self, task_id: int, new_title: str) -> None:
        """Update the title of an existing task.
        
        Args:
            task_id (int): ID of the task to update
            new_title (str): New title for the task
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                self.save_tasks()
                print(f"Task {task_id} updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id: int) -> None:
        """Delete a task from the list.
        
        Args:
            task_id (int): ID of the task to delete
        """
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def mark_complete(self, task_id: int) -> None:
        """Mark a task as completed.
        
        Args:
            task_id (int): ID of the task to mark as completed
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")

def print_menu() -> None:
    """Display the main menu options."""
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

def main():
    """Main function to run the Task Manager application."""
    task_manager = TaskManager()
    
    while True:
        print_menu()
        try:
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == "1":
                title = input("Enter task title: ")
                task_manager.add_task(title)
            
            elif choice == "2":
                task_manager.list_tasks()
            
            elif choice == "3":
                task_manager.list_tasks()
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ")
                task_manager.update_task(task_id, new_title)
            
            elif choice == "4":
                task_manager.list_tasks()
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            
            elif choice == "5":
                task_manager.list_tasks()
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_complete(task_id)
            
            elif choice == "6":
                print("Thank you for using Task Manager!")
                break
            
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
