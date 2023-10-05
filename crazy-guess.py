import random

mynumber = random.randint(1,100) 
yournumber = -1
guesses = 0   # storage for guesses

while yournumber != mynumber:
    yournumber = int(input("type in your number"))
    guesses = guesses + 1
    if yournumber > mynumber:
        print("your number is bigger") 
    else: 
        print("your number is smaller")
    
    print("try again")
    
print("You win the number is", mynumber, "you have used", guesses,"guesses")