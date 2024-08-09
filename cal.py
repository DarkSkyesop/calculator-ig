#CALCULATOR
def basic_calculator():
    try:
        val1 = float(input("Enter value 1: "))
        oper = input("Enter the operation you want to perform(+, -, *, /): ")
        val2 = float(input("Enter value 2: "))


        if oper == "+":
            print(val1, "+", val2, "=", val1 + val2)
        elif oper == "-":
            print(val1, "-", val2, "=", val1 - val2)
        elif oper == "*":
            print(val1, "x", val2, "=", val1 * val2)
        elif oper == "/":
            if val2 != 0:
                print(val1, "/", val2, "=", val1 / val2)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Call the calculator function
basic_calculator()


def restartcalc():
    while True:
        try:
            restart = (input("to use calculator again; enter 'again', to stop the program from running; enter 'stop': "))

            if restart == "again" or "AGAIN" or "Again":
                print("running the program again..")
                basic_calculator()

            elif restart == "stop" or "STOP" or "Stop":
                print("Thank you! Program stopped.")
            
            else:
                print("kindly only enter either 'stop' or 'again'.")
                
        except(ValueError):
            print("Error: Invalid Input.")
            restartcalc()

restartcalc()


#uff, tried my best i know its not that good but made it outta what i've learnt till now and now im going insane so i wont even try to add another operator for more than 2 digits coz uh.. yeah i cant get my brain to work anymore