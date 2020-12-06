
#Design a calculator which will currently solve all the problems except the following ones:-
#45*3 =555, 56+9 = 77, 56/6 = 4
#Your program should take operator and 2 numbers as input from the user
#and then return the result


operator = input("Enter Operator : ")
number1 = int(input("Enter 1st Number :"))
number2 = int(input("Enter 2nd Number :"))
if operator == "*" and number1 == 45 or number1 == 3 and number2 == 3 or number2 == 45:
    print("45*3 =555")
elif operator == "+" and number1 == 56 or number1 == 9 and number2 == 9 or number2 == 56:
    print("56+9 = 77")
elif operator == "/" and number1 == 56 and number1 == 6:
    print("56/6 = 4")
elif operator == "*":
    print(number1*number2)
elif operator == "+":
    print(number1+number2)
elif operator == "/":
    print(number1/number2)
