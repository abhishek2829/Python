#Create a Dictionary and take input from the user and return the meaning of the word from the dictionary

d1={"abandon":"give up completely",
    "Immutable":"Something that cannot be changed",
    "Mutable":"Something that can be changed",
    "RPA":"Robotic Process Automation"}

print("Please Input Your word from the given Dictionary")
print(d1.keys())
inpword = input("Please Input Your word from the given Dictionary: ")
print(inpword)
outmeaning = d1[inpword]
print(d1[inpword])
print(outmeaning)
