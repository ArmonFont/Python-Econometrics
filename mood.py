mood = input("Are you in a 1. good mood, \n"
             "2. bad mood or 3. neutral?\n"
             " \n"
             "Enter the corresponding number:")

if mood == "1":
    mood == 5
elif mood =="2":
    mood==-5
else :
    mood == 0

mood = int(mood)
#print(mood)

energy = input("From 1 to 10, how much energy do you have?")

energy = int(energy)

energy = energy - 5

#print(energy)
life = energy + mood

if life>=2:
    print("high")
elif life <=-2:
    print("low")
else:
    print("neutral")





