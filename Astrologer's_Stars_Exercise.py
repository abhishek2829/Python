#Pattern Printing
# Input = Integer n
# Boolean = True or False #take input as 1(true) or 0(false
# true
# *
# **
# ***
# ****
#
# false
# ****
# ***
# **
# *
# x = input("enter number: ")
# value = bool(x)
# print(value)
# while(True) :
#     n = int(input("Enter any number between 4 to 10: "))
#     x = int(input("Enter value 0 or 1: "))
#     if n<=10 and n>=4 :       #and x == 0 or x == 1 :
#         if x == 0:
#             value = bool(x)
#             print(value)
#             while n > 0 :
#                 j = 1
#                 while j <= n:
#                     print("*", end = "")
#                     j = j + 1
#                 print("\n")
#                 n = n - 1
#         elif x == 1:
#             value = bool(x)
#             print(value)
#             while n > 0:
#                 j = 4
#                 while n <= j:
#                     print("*", end = "")
#                     j = j - 1
#                 print("\n")
#                 n = n - 1
#     else :
#         print("Try Again")
#         UserChoice = input("Do you want to Continue,please enter yes or no: ")
#         if UserChoice.upper() == "YES" :
#             print("Go Ahead and Repeat the Process Again")
#             continue
#         elif UserChoice.upper() == "NO":
#             print("Closing the Process Now")
#             break
#         else :
#             print("Wrong Input given,try again")

print("Pattern Printing")
num = int(input("Enter num how many rows you want : "))
print("Type 1 Or 0")
bool_val = int(input("1 for True or 0 for false: "))
new =bool(bool_val)
if new == True:
    for i in range(0,num+1):
        print("*"*i)
elif new == False:
    for i in range(num,0,-1):
        print("*"*i)




# print("How Many Row You Want To Print")
# one= int(input())
# print("Type 1 Or 0")
# two = int(input())
# new =bool(two)
# if new == True:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new ==False:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*", end="")
#         print()