import json
import os
from typing import List, Dict

class TaskManager:
    """A command-line task manager application for managing tasks.
    
    This class provides a complete task management system with the following features:
    - Task creation with title, description and priority
    - Task listing with filtering options
    - Task searching by keywords
    - Task sorting by priority or status 
    - Task updates and deletion
    - Task completion tracking
    - Persistent storage using JSON
    
    The tasks are stored in a JSON file with the following structure:
    {
        "id": int,          # Unique identifier for the task
        "title": str,       # Task title
        "description": str, # Optional task description
        "priority": str,    # Priority level: "high", "medium", or "low"
        "completed": bool   # Task completion status
    }
    """
    
    def __init__(self, filename: str = "task/tasks.json"):
        """Initialize TaskManager with a file for persistent storage.
        
        Creates a new TaskManager instance that loads/saves tasks from/to the specified JSON file.
        If the file doesn't exist, it will be created when saving tasks.
        
        Args:
            filename (str): Path to the JSON file for task storage. Defaults to "task/tasks.json"
        """
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from the JSON file.
        
        Reads the task list from the JSON storage file. If the file exists and is valid JSON,
        the tasks will be loaded into memory. If there are any errors reading the file
        (e.g., invalid JSON, file permissions), an empty task list will be used.
        
        Raises:
            json.JSONDecodeError: If the file contains invalid JSON (handled internally)
        """
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
        except json.JSONDecodeError:
            print("Error reading tasks file. Starting with empty task list.")
            self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to the JSON file.
        
        Writes the current task list to the JSON storage file with proper formatting.
        Creates the file if it doesn't exist. Any errors during saving are caught
        and reported to the user.
        
        Raises:
            Exception: For any I/O related errors (handled internally)
        """
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, title: str, description: str = "", priority: str = "medium") -> None:
        """Add a new task with priority and description.
        
        Creates a new task with the given parameters and adds it to the task list.
        Automatically assigns a unique ID and sets completion status to False.
        The changes are immediately persisted to storage.
        
        Args:
            title (str): Title of the task
            description (str, optional): Detailed description of the task. Defaults to empty string
            priority (str, optional): Priority level of the task. Must be one of:
                "high", "medium", or "low". Defaults to "medium"
        """
        task_id = self.tasks[-1]['id'] + 1 if self.tasks else 1
        priority = priority.lower()
        if priority not in ["high", "medium", "low"]:
            priority = "medium"
            
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def list_tasks(self, filter_status: str = None, filter_priority: str = None) -> None:
        """Display tasks with optional filtering.
        
        Shows all tasks or a filtered subset based on completion status and/or priority.
        Tasks are displayed in a formatted table with ID, completion status, title,
        priority, and description (if present).
        
        Args:
            filter_status (str, optional): Filter tasks by completion status.
                Must be either "done" or "pending". Defaults to None (show all)
            filter_priority (str, optional): Filter tasks by priority level.
                Must be "high", "medium", or "low". Defaults to None (show all)
        """
        filtered_tasks = self.tasks

        if filter_status:
            is_completed = filter_status.lower() == 'done'
            filtered_tasks = [t for t in filtered_tasks if t["completed"] == is_completed]
            
        if filter_priority:
            filtered_tasks = [t for t in filtered_tasks if t["priority"] == filter_priority.lower()]

        if not filtered_tasks:
            print("No tasks found.")
            return

        print("\nCurrent Tasks:")
        print("-" * 60)
        for task in filtered_tasks:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['title']} - {task['priority'].upper()}")
            if task["description"]:
                print(f"   Description: {task['description']}")
        print("-" * 60)

    def search_tasks(self, keyword: str) -> None:
        """Search tasks by keyword in title or description.
        
        Performs a case-insensitive search for tasks containing the given keyword
        in either their title or description. Displays matching tasks in the same
        format as list_tasks().
        
        Args:
            keyword (str): Search term to look for in task titles and descriptions
        """
        keyword = keyword.lower()
        matches = [t for t in self.tasks if 
                  keyword in t["title"].lower() or 
                  keyword in t["description"].lower()]
        
        if not matches:
            print(f"No tasks found matching '{keyword}'")
            return
            
        print(f"\nTasks matching '{keyword}':")
        print("-" * 60)
        for task in matches:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['title']} - {task['priority'].upper()}")
            if task["description"]:
                print(f"   Description: {task['description']}")
        print("-" * 60)

    def clear_completed(self) -> None:
        """Remove all completed tasks.
        
        Permanently removes all tasks marked as completed from the task list
        and updates the storage file. Reports the number of tasks removed.
        This operation cannot be undone.
        """
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t["completed"]]
        removed_count = initial_count - len(self.tasks)
        self.save_tasks()
        print(f"Removed {removed_count} completed tasks.")

    def sort_tasks(self, sort_by: str) -> None:
        """Display tasks sorted by priority or status.
        
        Shows all tasks sorted by either priority level or completion status.
        For priority sorting, the order is: high -> medium -> low
        For status sorting, pending tasks come before completed tasks.
        
        Args:
            sort_by (str): Sorting criterion. Must be either "priority" or "status"
        """
        sorted_tasks = self.tasks.copy()  # Create a copy to avoid modifying original list
        
        if sort_by == "priority":
            priority_order = {"high": 0, "medium": 1, "low": 2}
            sorted_tasks.sort(key=lambda x: priority_order[x["priority"]])
        elif sort_by == "status":
            sorted_tasks.sort(key=lambda x: x["completed"])
            
        print("\nSorted Tasks:")
        print("-" * 60)
        for task in sorted_tasks:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['title']} - {task['priority'].upper()}")
            if task["description"]:
                print(f"   Description: {task['description']}")
        print("-" * 60)

    def update_task(self, task_id: int, new_title: str) -> None:
        """Update the title of an existing task.
        
        Changes the title of the task with the given ID and saves the changes.
        If no task exists with the given ID, an error message is displayed.
        
        Args:
            task_id (int): ID of the task to update
            new_title (str): New title to set for the task
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
        
        Permanently removes the task with the given ID from the task list
        and updates the storage file. If no task exists with the given ID,
        an error message is displayed. This operation cannot be undone.
        
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
        
        Sets the completion status of the task with the given ID to True
        and saves the changes. If no task exists with the given ID,
        an error message is displayed.
        
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