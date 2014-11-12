import data


help_info = 'list_employees - list all employees id-employee-position\n' + \
            'monthly_spending - return the sum of all monthly wages\n' + \
            'yearly_sepnding - return the sum of all wages + bonuses\n' + \
            'add_employee - enter add employee mode\n' + \
            'delete_employee - deletes an employee given an id number\n' + \
            'update_employee - updates an employee for a given id\n' + \
            'exit - exit the program'


class Commands:

    DATA_MANIPULATION_FUNCS = {
        'list_employees': data.list_employees,
        'monthly_spending': data.monthly_spending,
        'yearly_spending': data.yearly_sepnding,
        'add_employee': data.add_employee,
        'delete_employee': data.delete_employee,
        'update_employee': data.delete_employee
        }

    @staticmethod
    def execute(command, cursor, database):
        if command in Commands.DATA_MANIPULATION_FUNCS:
            return Commands.DATA_MANIPULATION_FUNCS[command](cursor, database)
        if command == 'help':
            return help_info
        return 'Error! Invalid command!\nFor more information type help'


def main():
    print('Welcome, this is company database program for info type help')
    info = data.create_database()
    database = info['data']
    cursor = info['cursor']

    while True:
        command = input('Enter command>')
        if command == 'exit':
            break

        output = Commands.execute(command, cursor, database)
        if output is not None:
            print(output)

    database.close()


if __name__ == '__main__':
    main()
