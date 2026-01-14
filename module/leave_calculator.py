import logging

def leave_calc(basic_salary, days):
    logging.debug(f"Leave calc started: salary={basic_salary}, days={days}")

    if days > 15:
        deduction = days * (basic_salary / 30)
        logging.info(f"Leave deduction applied: {deduction}")
        return deduction

    logging.info("No leave deduction applied")
    return 0.0
