import sqlite3


def create_database():
    company_name = input('company_name>')
    company_name += '.db'
    connection = sqlite3.connect(company_name)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff(id INTEGER PRIMARY KEY,
                name TEXT, salary INTEGER, bonus INTEGER, position TEXT)''')

    connection.commit()

    return {'data': connection, 'cursor': cursor}


def list_employees(cursor, database):
    employees = cursor.execute(
        ''' SELECT id, name, position FROM staff''')

    output = ''
    for row in employees:
        output += ('{0} - {1} - {2}\n'.format(row['id'],
                                              row['name'],
                                              row['position']))
    return output


def add_employee(cursor, database):
    employee = get_employee_info()
    cursor.execute(
        ''' INSERT INTO staff(name, salary, bonus, position)
        VALUES(?,?,?,?)''', employee)
    database.commit()

    return 'Employee succsefully added'


def sum_monthly_salaries(cursor):
    employee_salaries = cursor.execute('''SELECT salary FROM staff''')
    return sum([row['salary'] for row in employee_salaries])


def monthly_spending(cursor, database):
    return 'Total monthly spending is {0}'.format(sum_monthly_salaries(cursor))


def sum_of_bonuses(cursor):
    employee_bonuses = cursor.execute('''SELECT bonus FROM staff''')
    return sum([row['bonus'] for row in employee_bonuses])


def yearly_sepnding(cursor, database):
    months_in_year = 12
    yearly_salaries = months_in_year*sum_monthly_salaries(cursor)
    total_spending = yearly_salaries + sum_of_bonuses(cursor)
    return 'Total yearly spending is {0}'.format(total_spending)


def delete_employee(cursor, database):
    employee_id = get_employee_id()
    cursor.execute('''DELETE FROM staff WHERE id = ?''', (employee_id,))
    database.commit()

    return 'Employee succsefully deleted!'


def update_eployee(cursor, database):
    new_employee_data = get_employee_info() + tuple(get_employee_id())
    cursor.execute('''UPDATE staff SET name = ?, salary = ?,
        bonus = ?, position = ? WHERE id = ?''', new_employee_data)
    database.commit()


def get_employee_id():
    return input('id>')


def get_employee_info():
    name = input('name>')
    salary = input('salary>')
    bonus = input('bonus>')
    position = input('position>')
    return (name, salary, bonus, position)
