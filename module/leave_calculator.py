def leave_calc(basic_salary, days):
    if days > 15:
        return days * (basic_salary / 30)
    return 0.0
