import random
qu = input("Do you wanna play? (say yes or no)").lower()
if qu == "yes":
    print("Welcome")
else:
    quit()

top = input("Enter top of range: ")
if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Choose a number above 0")
else:
    print("Use numbers ONLY")

ra = random.randint(0, top)
counter = 0
while True:
    que = int(input("Guess a number"))
    counter += 1
    if que == ra:
        print("Correct !!")
        break
    elif que > ra:
        print("Too High")
    else:
        print("Too Low")
complimentrand = 3
compliment = random.randint(0, complimentrand)
if compliment == 1:
    complimenthelp = "Nice!"
elif compliment == 2:
    complimenthelp = "Dang!"
elif compliment == 3:
    complimenthelp = "You cooked!"

print("You did it in", counter, "tries.", complimenthelp)
