# student-task-manager
Project status: Completed


A Python console application to add, display, complete and delete student tasks.
Built as Lab Assignment 4 for CSC418 (DevOps for Cloud Computing) to practise
a complete Git and GitHub workflow.
## Features
- Add tasks (empty titles are rejected)
- Display all tasks with their status
- Mark one or several tasks as completed
- Delete tasks using a valid task ID
- Summary of total, completed and pending tasks
- Automated tests and a GitHub Actions workflow
## Requirements
- Python 3.10 or newer
- Git
## Setup
    git clone https://github.com/PakeezaHassan5/student-task-manager.git
    cd student-task-manager
## Usage
    python main.py
Choose an option from the menu (1-6) and follow the prompts.
See docs/user-guide.md for a detailed guide.
## Running the tests
    python -m unittest discover -s tests v
## Project structure
- main.py: console menu
- task_manager.py: Task and TaskManager classes
- tests/: unit tests
- docs/: user guide
- .github/workflows/: GitHub Actions workflow
## Author
Pakeeza Hassan (Reg. No. FA23-BSE-151), COMSATS University Islamabad, Lahore Campus
## License

MIT License