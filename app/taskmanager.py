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