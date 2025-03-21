"""
Jejo Task Manager - Main Application Module

This module provides the main command-line interface for the Jejo Task Manager application.
It handles user interaction, menu display, and task management operations by integrating
with the TaskManager class.

Features:
- Interactive menu-driven interface
- Task creation with customizable properties (title, description, priority)
- Task listing with filtering and sorting options
- Task updates and deletion
- Task completion tracking
- Search functionality
- Error handling and input validation

Dependencies:
- app.taskmanager.TaskManager: Core task management functionality

Usage:
Run this script directly to start the Task Manager application:
    $ python main.py

The application will display a menu with numbered options (1-10).
Follow the prompts to perform various task management operations.
"""

from app.taskmanager import TaskManager

def print_menu() -> None:
    """
    Display the main menu options for the Task Manager application.
    
    The menu shows all available operations numbered from 1 to 10:
    1. Add Task - Create a new task with title, description, and priority
    2. List Tasks - Display all tasks with optional filters
    3. Update Task - Modify existing task details
    4. Delete Task - Remove a task from the system
    5. Mark Task as Complete - Update task completion status
    6. Search Tasks - Find tasks by keyword
    7. Filter Tasks - View tasks by status or priority
    8. Sort Tasks - Organize tasks by priority or status
    9. Clear Completed Tasks - Remove all completed tasks
    10. Exit - Close the application
    """
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Sort Tasks")
    print("9. Clear Completed Tasks")
    print("10. Exit")

def main():
    """
    Main function to run the Task Manager application.
    
    This function:
    - Creates a TaskManager instance for managing tasks
    - Implements the main application loop
    - Handles user input and menu selection
    - Provides error handling for invalid inputs
    - Manages the flow between different task operations
    
    The function runs until the user selects the exit option (10)
    or terminates the program.
    
    Error Handling:
    - ValueError: Handles invalid numeric inputs
    - General exceptions: Catches and displays other runtime errors
    """
    task_manager = TaskManager()
    
    while True:
        print_menu()
        try:
            choice = input("\nEnter your choice (1-10): ")
            
            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description (optional): ")
                priority = input("Enter priority (high/medium/low) [default=medium]: ").lower()
                task_manager.add_task(title, description, priority)
            
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
                keyword = input("Enter search keyword: ")
                task_manager.search_tasks(keyword)
                
            elif choice == "7":
                print("\nFilter by:")
                print("1. Status (done/pending)")
                print("2. Priority (high/medium/low)")
                filter_choice = input("Enter choice (1-2): ")
                
                if filter_choice == "1":
                    status = input("Enter status (done/pending): ")
                    task_manager.list_tasks(filter_status=status)
                elif filter_choice == "2":
                    priority = input("Enter priority (high/medium/low): ")
                    task_manager.list_tasks(filter_priority=priority)
                    
            elif choice == "8":
                print("\nSort by:")
                print("1. Priority")
                print("2. Status")
                sort_choice = input("Enter choice (1-2): ")
                
                if sort_choice == "1":
                    task_manager.sort_tasks("priority")
                elif sort_choice == "2":
                    task_manager.sort_tasks("status")
                    
            elif choice == "9":
                confirm = input("Are you sure you want to clear all completed tasks? (y/n): ")
                if confirm.lower() == 'y':
                    task_manager.clear_completed()
                    
            elif choice == "10":
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
