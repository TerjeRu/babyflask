from flask import Flask, request, render_template, redirect, abort
from models import db, EmployeeModel

def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee_data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the Flask app
    db.init_app(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    # Route to create a new employee
    @app.route('/data/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('createpage.html')
        if request.method == 'POST':
            employee_id = request.form['employee_id']
            name = request.form['name']
            position = request.form['position']
            employee = EmployeeModel(employee_id=employee_id, name=name, position=position)
            db.session.add(employee)
            db.session.commit()
            return redirect('/data')

    # Route to update an existing employee
    @app.route('/data/<int:id>/update', methods=['GET', 'POST'])
    def update(id):
        employee = EmployeeModel.query.filter_by(employee_id=id).first()
        if not employee:
            return f"Employee with id = {id} does not exist."

        if request.method == 'POST':
            employee.name = request.form['name']
            employee.position = request.form['position']
            db.session.commit()
            return redirect(f'/data/{id}')

        return render_template('update.html', employee=employee)

    # Route to retrieve and display a list of all employees
    @app.route('/data')
    def retrieve_data_list():
        employees = EmployeeModel.query.all()
        return render_template('datalist.html', employees=employees)

    # Route to retrieve and display a single employee's information
    @app.route('/data/<int:id>')
    def retrieve_single_employee(id):
        employee = EmployeeModel.query.filter_by(employee_id=id).first()
        if employee:
            return render_template('data.html', employee=employee)
        return f"Employee with id = {id} does not exist."

    # Route to delete an employee
    @app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
    def delete(id):
        employee = EmployeeModel.query.filter_by(employee_id=id).first()
        if request.method == 'POST':
            if employee:
                db.session.delete(employee)
                db.session.commit()
                return redirect('/data')
            abort(404)

        return render_template('delete.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=5000)