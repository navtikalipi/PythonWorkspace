import logging
import bonus_calculator
import leave_calculator

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def salary_calc():
    logging.info("Salary calculation started")

    basic_salary = float(input("Enter your basic salary: "))
    designation = input("Enter your designation: ")
    leave = int(input("Enter total leaves: "))

    logging.info(
        f"Inputs -> salary={basic_salary}, designation={designation}, leaves={leave}"
    )

    bonus = basic_salary * bonus_calculator.bonus_calc(designation)
    deduction = leave_calculator.leave_calc(basic_salary, leave)

    salary = basic_salary + bonus - deduction

    logging.info(f"Final salary calculated: {salary}")
    print("Your salary is", salary)

salary_calc()
