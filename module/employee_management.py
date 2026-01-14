import bonus_calculator
import leave_calculator

def salary_calc():
    basic_salary = float(input("Enter your basic salary: "))
    designation = input("Enter your designation: ").capitalize()
    leave = int(input("Enter total leaves: "))

    bonus = basic_salary * bonus_calculator.bonus_calc(designation)
    deduction = leave_calculator.leave_calc(basic_salary, leave)

    salary = basic_salary + bonus - deduction

    print("Your salary is", salary)

salary_calc()
