# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy to work with Flask
db = SQLAlchemy()

# Define the EmployeeModel class which will represent the 'employees' table in the database
class EmployeeModel(db.Model):
    # Specify the name of the table
    __tablename__ = "employees"

    # Define the columns in the table
    id = db.Column(db.Integer, primary_key=True)  # A unique identifier for each employee
    employee_id = db.Column(db.Integer(), unique=True)  # A unique employee ID
    name = db.Column(db.String(45))  # Employee's name with a max length of 45 characters
    position = db.Column(db.String(45))  # Employee's position with a max length of 45 characters

    # Constructor for the EmployeeModel class
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id  # Set the employee ID
        self.name = name  # Set the employee's name
        self.position = position  # Set the employee's position

    # Representation method for the EmployeeModel instances
    def __repr__(self):
        # How an instance of EmployeeModel will be printed
        return f"{self.name}:{self.employee_id}"
