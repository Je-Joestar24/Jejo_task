# Jejo Task Manager

A simple command-line Task Manager application written in Python that allows users to manage their tasks efficiently. Tasks are stored in a JSON file for persistent storage.

## Features
- Add new tasks with priority levels and descriptions
- List all tasks with filtering options
- Update task titles and details
- Delete tasks
- Mark tasks as completed
- Search tasks by keywords
- Filter tasks by status or priority
- Sort tasks by priority or status
- Clear all completed tasks at once
- Persistent task storage using a JSON file

## Prerequisites
Before running this project, ensure you have the following installed:
- **Python 3.x** (Download from [python.org](https://www.python.org/))
- **A Code Editor or IDE** (Recommended: [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/))

## Installation
1. **Clone the Repository** (or download the `task_manager.py` file)
   ```sh
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   ```

2. **Ensure Python is Installed**
   ```sh
   python --version
   ```
   If not installed, download and install Python from [here](https://www.python.org/downloads/).

## Usage
Run the script using Python:

```sh
python task_manager.py
```

Once running, follow the on-screen menu to:
1. Add tasks
2. List tasks
3. Update task titles
4. Delete tasks
5. Mark tasks as complete
6. Search tasks
7. Filter tasks
8. Sort tasks
9. Clear completed tasks
10. Exit program

### Example Commands:
- **Adding a Task**
  ```
  Enter task title: Buy groceries
  Enter task description (optional): Get milk, eggs, and bread
  Enter priority (high/medium/low) [default=medium]: high
  Task 'Buy groceries' added successfully!
  ```

- **Listing Tasks**
  ```
  Current Tasks:
  ------------------------------------------------------------
  1. [ ] Buy groceries - HIGH
     Description: Get milk, eggs, and bread
  ------------------------------------------------------------
  ```

- **Searching Tasks**
  ```
  Enter search keyword: groceries
  Tasks matching 'groceries':
  ------------------------------------------------------------
  1. [ ] Buy groceries - HIGH
     Description: Get milk, eggs, and bread
  ------------------------------------------------------------
  ```

- **Filtering Tasks**
  ```
  Filter by:
  1. Status (done/pending)
  2. Priority (high/medium/low)
  Enter choice (1-2): 2
  Enter priority (high/medium/low): high
  ```

- **Sorting Tasks**
  ```
  Sort by:
  1. Priority
  2. Status
  Enter choice (1-2): 1
  ```

## Task Properties
Each task includes:
- **ID**: Unique identifier
- **Title**: Task name
- **Description**: Optional detailed description
- **Priority**: High, Medium (default), or Low
- **Status**: Complete or Pending

## File Structure
```
Jejo_task/
│── main.py               # Main script file
│── README.md             # Project documentation
|── task/tasks.json       # Storage file for tasks
|── app/taskmanager.py    # Task Manager Class & functionalities

```

---

Happy Task Managing! 🚀