class Employee:

    def __init__(self, years_of_experience, position_name, name_of_employee):
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.name_of_employee = name_of_employee

    def calculate_salary(self):
        base_salary = 2500
        calculated_salary = None

        if 0 <self.years_of_experience <=2:
            calculated_salary = base_salary + 1500

        elif 2 <self.years_of_experience <=5:
            calculated_salary = base_salary + 2500

        elif self.years_of_experience > 5:
            calculated_salary = base_salary + 3500

        else:
            print("Wrong value inserted")

        print("The calculated salary is : %s" %calculated_salary)
        print("xxxx")

        return calculated_salary



    def candidate_for_bonus(self, the_calculated_salary):
        salary_with_bonus = None

        if "front_end" in self.position_name:
            salary_with_bonus = the_calculated_salary * 1.1

        if self.years_of_experience > 2 :
            salary_with_bonus = the_calculated_salary * 1.2

        print("The bonus for the position %s is : %s" %(self.position_name, salary_with_bonus))

class Programmer(Employee):

    def __init__(self, years_of_experience, position_name, name_of_employee):
        super().__init__(years_of_experience, position_name, name_of_employee)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.name_of_employee = name_of_employee

    def print_data(self):
        print("The employee %s works as a %s in our company" %(self.name_of_employee, self.position_name))

# 1st instance
junior_python_programmer = Programmer(1, "front_end", "Joseph")

# Execute of methods
calculated_salary_value = junior_python_programmer.calculate_salary()
junior_python_programmer.candidate_for_bonus(calculated_salary_value)
junior_python_programmer.print_data()

print("\n")
# 2nd instance
senior_devops = Programmer (6, "senior_devops", "Dan")

# Execute of methods
calculated_salary_value = senior_devops.calculate_salary()
senior_devops.candidate_for_bonus(calculated_salary_value)
senior_devops.print_data()


