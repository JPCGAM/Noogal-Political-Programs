import random
InitialPop = float(input("What is the initial population? "))
DaysSince = float(input("How many days has it been since the last election? "))
Cvalue = input("Chooce C value? ")
if Cvalue == "yes":
    c = float(input("Type c value, recomended value 0.99999 to 1.0001: "))
elif Cvalue == "random" or Cvalue =="r":
    c = random.uniform(0.99985,1.0002)
else:
    c = 1.0014
NewPop = round(InitialPop*c**(DaysSince),0)
print("The new population is", NewPop)