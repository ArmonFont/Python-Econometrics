
wealth = input("what is your weekly income?")

utility= input("What is your utility function? (use x)")

str(utility)

utility = utility.replace("^", "**")
utility = utility.replace("x", wealth)

utility = eval(utility)
wealth = int(wealth)

if utility > wealth:
    print("You are risk loving!")
elif utility == wealth:
    print("You are risk neutral")
elif utility < wealth:
    print("You are risk averse!")
else:
    print("hmm something went wrong, please re-try")

print("Your utility is " + str(utility))







