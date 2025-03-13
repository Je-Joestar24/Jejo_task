# Task Manager

A simple command-line Task Manager application written in Python that allows users to manage their tasks efficiently. Tasks are stored in a JSON file for persistent storage.

## Features
- Add new tasks
- List all tasks
- Update task titles
- Delete tasks
- Mark tasks as completed
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
6. Exit the program

### Example Commands:
- **Adding a Task**
  ```
  Enter task title: Buy groceries
  Task 'Buy groceries' added successfully!
  ```

- **Listing Tasks**
  ```
  Current Tasks:
  -----------------------------------
  1. [ ] Buy groceries
  -----------------------------------
  ```

- **Marking a Task as Complete**
  ```
  Enter task ID to mark as complete: 1
  Task 1 marked as completed!
  ```

## File Structure
```
task-manager/
│── task_manager.py  # Main script file
│── tasks.json       # Storage file for tasks
│── README.md        # Project documentation
```

## Contributing
Feel free to submit issues or feature requests. If you'd like to contribute, fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

---

Happy Task Managing! 🚀