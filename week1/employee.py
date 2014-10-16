class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Hourly(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weekly_pay(self, hours):
        if hours <= 40:
            return hours*self.salary
        else:
            excess = self.salary * 1.5
            return (hours - 40) * excess + 40 * self.salary


class Salaried(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weekly_pay(self, hours):
        return self.salary / 52


class Manager(Salaried):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self. bonus = bonus

    def weekly_pay(self, hours):
        return self.bonus + super().weekly_pay(hours)


def main():
    staff = []
    staff.append(Hourly("Morgan, Harry", 30.0))
    staff.append(Salaried("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: %.2f" % pay)

if __name__ == "__main__":
    main()
