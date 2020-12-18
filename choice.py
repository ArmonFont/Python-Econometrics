import sys

# risk neutral or risk averse
q1 = input("Youre given $100 and you have the option to keep it or bet it for $200. \n"
           "There is a 50% chance of you losing it. Enter 'keep or 'bet' for what you would choose.")

if q1 == "keep":
    print("keep")
    x = .5
elif q1 == "bet":
    print("bet")
    x = 1
else:
    print("invalid input, please try again")
    sys.exit()

print(x)

# risk loving or risk neutral
q2 = input("Imagine that you received 1 million dollars from a rich uncle \n"
           "You have two choices: \n"
           "1. Enter a contest to turn the 1 million to 5 million \n"
           "2. Keep the 1 million in a hedge fund that guarentees you a 50k return \n"
           " in 1 year \n"
           "There is a 10% you will win with option 1 and a 90% that you will reduce\n"
           "your money by half \n"
           "Enter '1' or '2'")
q2 = int(q2)
if q2 == 1:
    print("1")
    y = 1.5
elif q2 == 2:
    print("2")
    y = 1
else:
    print("invalid input, please try again")
    sys.exit()

# risk averse or risk loving

q3 = input("You have 2 choices \n"
           "You can either:"
           "1. Bet $1000 on a game where there is a 60% chance to triple your money \n "
           "2. Bet $1000 on a game where there is a 5% chance to 10X your money\n"
           "Enter '1' or '2' ")

q3 = int(q3)
if q3 == 1:
    print("1")
    z = .5
elif q3 == 2:
    print("2")
    z = 1.5
else:
    print("invalid input, please try again")
    sys.exit()

avg = (x + y + z) / 3

print("Your basic utility function of income is: U(I)=I^" + str(round(avg,2)))

print("\n")

if avg > 1:
    print("You are risk loving")
elif avg < 1:
    print("You are risk averse")
else:
    print("You are risk neutral")
