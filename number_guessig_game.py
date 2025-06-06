import random

top_of_range =input("Type a number :")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <=0:
        print("Please a type a number larger than zero next time.")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses += 1
    use_guess = input("Make a guess : ")
    if use_guess.isdigit():
        use_guess=int(use_guess)
    else:
        print("Please type a number next time")
        continue
    if use_guess == random_number:
        print("You got it ! ")
        break
    elif use_guess > random_number:
        print("your are above the number !")
    else:
        print("Your are below the number !")

print("You got it in ",guesses," guesses")


