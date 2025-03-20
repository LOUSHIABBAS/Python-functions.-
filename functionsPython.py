import math
PI = math.pi
BLUE = "\033[1;34m"
RED = "\033[1;31m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
MAGENTA = "\033[1;35m"
RESET = "\033[0;0m"


#title : Python Functions.
# Author: Ali Abbas
# Date : 03 20 2025

# how to use : Clear the (''') above and below any program that you would like to run, play around enjoy. 

#basic input output program using if __name__ == "__main__": and def func. 
'''
def greet_user(username, userage, userheight):
    print(f"Hello {BLUE}{username}{RESET}, you are {RED}{userage}{RESET} years old and {CYAN}{userheight}{RESET} meters tall.")


if __name__ == "__main__":
    
    hisName = input("What is your name? ")

    age = int(input("How old are you? "))

    height = float(input("How tall are you (In meters)?"))
    greet_user(hisName, age, height)
'''

#Normal print func. using formula
'''
def calculator(num1, num2):
    print(f"sum = {BLUE}{num1 + num2}{RESET}") 
    print(f"Difference = {RED}{num1 - num2}{RESET}") 
    print(f"Product = {CYAN}{num1 * num2}{RESET}") 
    print(f"Quoteint = {YELLOW}{num1 / num2}{RESET}") 
    print(f"Floor Division = {GREEN}{num1 // num2}{RESET}")
    print(f"Modulo = {MAGENTA}{num1 % num2}{RESET}")  
if __name__ == "__main__":
    number1 = int(input(f"first number? "))
    number2 = int(input(f"second number? "))
    calculator(number1, number2)
'''

#RADIUS CALCULATOR

'''
def calculator_radius(radius):
    print(f"Circumference = {YELLOW}{2 * PI * radius}{RESET}")  
    print(f"Area of Circle = {GREEN}{PI * radius ** 2}{RESET}")  
    print(f"Square Root of Radius = {MAGENTA}{math.sqrt(radius)}{RESET}")  

if __name__ == "__main__":
    getUserRadius = float(input("Submit radius? "))
    calculator_radius(getUserRadius)
'''


#area calculator func return

'''
def calculator_radius(radius):
    circumference = 2 * PI * radius
    areaCircle = PI * radius ** 2
    squareRoot= math.sqrt(radius)
    return circumference, areaCircle, squareRoot

if __name__ == "__main__":
    getUserRadius = float(input("Submit radius? "))
    circumference, areaCircle, squareRoot = calculator_radius(getUserRadius)
    print(f"Circumference = {YELLOW}{circumference}{RESET}")  
    print(f"Area of Circle = {GREEN}{areaCircle}{RESET}")  
    print(f"Square Root of Radius = {MAGENTA}{squareRoot}{RESET}") 
'''



# different calculations using one return func. 
'''
def twonumbas(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return sum, difference, product, quotient

if __name__ == "__main__":
    numberuno = float(input("What is first nummer?? "))
    numberdos = float(input(f"What is second nummer?? "))
    sum, difference, product, quotient = twonumbas(numberuno, numberdos) 
    print(f"sum = {YELLOW}{sum}{RESET}")
    print(f"difference = {RED}{difference}{RESET}")
    print(f"product = {BLUE}{product}{RESET}")
    print(f"quotient = {GREEN}{quotient}{RESET}")    
'''

#POSITIVE , NEG, OR ZERO?
'''
def isItZero(number):
    if number >= 1:
        return f"{GREEN}positive!{RESET}"
    elif number <= -1:
        return f"{RED}Negative!{RESET}"
    else:
        return f"{YELLOW}It is a Zero.{RESET}"

if __name__ == "__main__":
       numeropls = float(input("What is number?"))
       print(isItZero(numeropls))
'''


#GRADE CALCULATOR

'''
def gradeCalculator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


if __name__ == '__main__':
    gimmescore = int(input("gimme your score buddy. "))
    print(gradeCalculator(gimmescore))
'''





#traffic color program
'''
def trafficcolor(color):
    if color == 'red':
        return f"{RED}STOP{RESET}"
    elif color == 'yellow':
        return f"{YELLOW}Caution{RESET}"
    elif color == 'green':
        return f"{GREEN}Go{RESET}"
    else:
        return f"{CYAN}Invalid Color{RESET}"
    
if __name__ == "__main__":
    gimmecolor = input("Provide me a traffic light color?")
    print(trafficcolor(gimmecolor.lower()))    
'''



#name,age,grade,trafficcolor program
''''
def gradeCalculator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F" 

def trafficcolor(color):
    if color == 'red':
        return f"{RED}STOP{RESET}"
    elif color == 'yellow':
        return f"{YELLOW}Caution{RESET}"
    elif color == 'green':
        return f"{GREEN}Go{RESET}"
    else:
        return f"{CYAN}Invalid Color{RESET}"  

if __name__ == "__main__":
    username = input(f"What is your name? ")
    userage = input(f"How old are you? ")

    userscore = float(input(f"What is your exam score? "))
    usergrade = gradeCalculator(userscore)
    print(f"your score: {usergrade}")

    usercolor = input(f"Provide a traffic light color? ")
    usercolortraffic = trafficcolor(usercolor)
    print(f"color chosen: {usercolortraffic}")

    print(F"Hello {username.capitalize()}, you are {userage} and you got a {usergrade} and you chose {usercolortraffic} for a traffic light!")
'''

#SIMPLE MENU

'''
# simple formatting : 
def menu():
    print(f"{'Item':<10}{'Price':>6}")
    print(f"{'Apple':<10} ${1.50:>3.2f}")
    print(f"{'Banana':<10} ${0.75:>3.2f}")


if __name__ == "__main__":
    menu()    
    additem = input("What item would you like to add? ")
    addprice = float(input("What price would you like to add? "))
    print("\nUpdated Menu:")
    print(f"{'Item':<10}{'Price':>6}")
    print(f"{'Apple':<10} ${1.50:>3.2f}")
    print(f"{'Banana':<10} ${0.75:>3.2f}")
    print(f"{additem:<10} ${addprice:>3.2f}")
'''


## Call custom function of your own!  ( remove ''' and ## )
#if __name__ == "__main__":