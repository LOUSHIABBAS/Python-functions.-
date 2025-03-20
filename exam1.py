import math
BLUE = "\033[1;34m"
RED = "\033[1;31m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
MAGENTA = "\033[1;35m"
RESET = "\033[0;0m"


# title: Midterm Exam CIS-125
# Author: Ali Abbas
# Date : 03 20 2025


def getInfo():  # Get user info (name, rating, salary)
    full_name = input("Enter employee full name: ")
    emp_rating = int(input("Enter employee performance rating (0-10): "))
    emp_salary = float(input("Enter employee's current salary: "))
    return full_name, emp_rating, emp_salary


def calculateRaise(rating, current_salary): # ( Calculate employee raise )
    if rating >= 0 and rating <= 2:
        RAISE = .03
        print(f"{CYAN}You received a 3% raise{RESET}")
    elif rating >= 3 and rating <= 5:
         RAISE = .05
         print(f"{CYAN}You received a 5% raise{RESET}")
    elif rating >= 6 and rating <= 7:
        RAISE = .10
        print(f"{CYAN}You received a 10% raise{RESET}")
    elif rating >= 8 and rating <= 10:
        RAISE = .20
        print(f"{CYAN}You received a 10% raise{RESET}")
    else:
        return print("No raise received")
    new_salary = current_salary + (current_salary * RAISE)
    return new_salary



def main(): # ( Call functions and output final message )
    full_name, emp_rating, emp_salary = getInfo()

    new_salary = calculateRaise(emp_rating, emp_salary)

    print(f"{BLUE}{full_name.title()}'s new salary is: ${new_salary:,.2f}.")



if __name__  == "__main__":  # ( Call main )
    main()