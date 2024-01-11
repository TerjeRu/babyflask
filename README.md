# babyflask
# Flask Employee Management System

## About
This Flask-based web application is a simple Employee Management System, demonstrating CRUD (Create, Read, Update, Delete) operations in a Python web environment. It uses Flask along with Flask_SQLAlchemy for efficient database interactions.
All is contained in a Docker image

## Features
- **Create Employee Records**: Add new employee details to the system.
- **Read Employee Information**: View a list of all employees or detailed information about specific employees.
- **Update Employee Details**: Edit existing employee information.
- **Delete Employee Records**: Remove employees from the system.

## Technologies Used
- Python
- Flask
- Flask_SQLAlchemy
- SQLite
- Docker

## How did I create this?
The app is based on this free tutorial.
https://www.askpython.com/python-modules/flask/flask-crud-application
(be aware that "@app.before_first_request" is deprecated- use this instead: https://stackoverflow.com/questions/73570041/flask-deprecated-before-first-request-how-to-update

## Why?
This is a personal project to learn about various concepts used in the DevOps pipeline. This app is just to get somthing online that can be updated and monitored using standard practices for modern development and operations in IT.
I have created a GPT to help guide the project: https://chat.openai.com/g/g-ukSdQlG6p-devops-project-mentor

## Contributing
Fork away matey!

## License
GNU General Public License v3

## How to setup
1. **Open Visual Studio Code**: 
   - Launch VS Code on your computer.

2. **Open Terminal in VS Code**: 
   - Go to the top menu in VS Code.
   - Select `Terminal` -> `New Terminal`.
   - This opens a terminal at the bottom of VS Code.

3. **Navigate to Your Desired Folder**: 
   - Use the `cd` command to navigate.
   - Example: `cd Desktop`.

4. **Clone the Repository**: 
   - Run the command: `git clone https://github.com/TerjeRu/babyflask.git`.
   - This creates a folder named `babyflask` with the repository contents.

5. **Navigate to the Repository Folder**: 
   - Change directory with `cd babyflask`.

6. **Create a Virtual Environment**: 
   - Run: `python -m venv env`.
   - This creates a new folder `env` in your project directory.

7. **Activate the Virtual Environment**:
   - On Windows, run: `.\env\Scripts\activate`.
   - On macOS/Linux, run: `source env/bin/activate`.

8. **Install Required Packages**: 
   - Run: `pip install -r requirements.txt`.
   - This installs all necessary Python packages.

9. **Start Working on the Project**: 
   - The Python interpreter from the activated virtual environment will be used.

10. **Deactivate the Virtual Environment**: 
   - Once done, run `deactivate` in the terminal to exit the environment.
