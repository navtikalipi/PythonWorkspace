import logging

def bonus_calc(designation):
    designation = designation.lower()
    logging.debug(f"Calculating bonus for {designation}")

    if designation == "coder":
        logging.info("Bonus rate: 10%")
        return 0.10
    elif designation == "designer":
        logging.info("Bonus rate: 15%")
        return 0.15
    elif designation == "manager":
        logging.info("Bonus rate: 5%")
        return 0.05
    else:
        logging.warning(f"Invalid designation: {designation}")
        return 0.0
