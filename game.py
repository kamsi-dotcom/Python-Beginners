print("Welcome to my guessing game.")
ran = range(1,11)
import random
no = random.randrange(1,11)
while True:
    for i in range(5):  
        guess = int(input("Pick a number between 1 and 10\n>>> "))
        if guess != no and guess not in ran:
            print("Number out of range.")
        elif guess != no:
            print("Wrong guess.Try again")
            if guess < no:
                print("Too low")
            elif guess > no:
                print("Too high")
        else:
            print("Congratulations you won.") 
            exit()
    print("Turn exhausted\nYou lose.")
    exit()
    continue