# Jejo Task Manager 1
from app.taskmanager import TaskManager

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
