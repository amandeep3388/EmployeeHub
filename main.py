import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost", user="root", password="password", database="employees"
)

def add_employee():
    employee_id = input("Enter Employee Id: ")
    
    if check_employee_existence(employee_id):
        print("Employee already exists. Please try again.")
        display_menu()
    else:
        name = input("Enter Employee Name: ")
        post = input("Enter Employee Post: ")
        salary = input("Enter Employee Salary: ")
        data = (employee_id, name, post, salary)
    
        sql_query = 'INSERT INTO employee_details VALUES (%s, %s, %s, %s)'
        cursor = db_connection.cursor()
        cursor.execute(sql_query, data)
        db_connection.commit()
        print("Employee added successfully.")
        display_menu()

def promote_employee():
    employee_id = int(input("Enter Employee's Id: "))
    
    if not check_employee_existence(employee_id):
        print("Employee does not exist. Please try again.")
        display_menu()
    else:
        increase_amount = int(input("Enter increase in salary: "))
        current_salary = fetch_employee_salary(employee_id)
        new_salary = current_salary + increase_amount
        
        sql_query = 'UPDATE employee_details SET salary=%s WHERE id=%s'
        data = (new_salary, employee_id)
        cursor = db_connection.cursor()
        cursor.execute(sql_query, data)
        db_connection.commit()
        print("Employee promoted successfully.")
        display_menu()

def remove_employee():
    employee_id = input("Enter Employee Id: ")
    
    if not check_employee_existence(employee_id):
        print("Employee does not exist. Please try again.")
        display_menu()
    else:
        sql_query = 'DELETE FROM employee_details WHERE id=%s'
        data = (employee_id,)
        cursor = db_connection.cursor()
        cursor.execute(sql_query, data)
        db_connection.commit()
        print("Employee removed successfully.")
        display_menu()

def check_employee_existence(employee_id):
    sql_query = 'SELECT * FROM employee_details WHERE id=%s'
    cursor = db_connection.cursor(buffered=True)
    data = (employee_id,)
    cursor.execute(sql_query, data)
    return cursor.rowcount == 1

def fetch_employee_salary(employee_id):
    sql_query = 'SELECT salary FROM employee_details WHERE id=%s'
    data = (employee_id,)
    cursor = db_connection.cursor()
    cursor.execute(sql_query, data)
    result = cursor.fetchone()
    return result[0] if result else 0

def display_employees():
    sql_query = 'SELECT * FROM employee_details'
    cursor = db_connection.cursor()
    cursor.execute(sql_query)
    employees = cursor.fetchall()
    for employee in employees:
        print("Employee Id:", employee[0])
        print("Employee Name:", employee[1])
        print("Employee Post:", employee[2])
        print("Employee Salary:", employee[3])
        print("---------------------")
    display_menu()

def display_menu():
    print("Welcome to Employee Management System")
    print("Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Promote Employee")
    print("4. Display Employees")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        remove_employee()
    elif choice == 3:
        promote_employee()
    elif choice == 4:
        display_employees()
    elif choice == 5:
        exit(0)
    else:
        print("Invalid choice. Please try again.")
        display_menu()

display_menu()
