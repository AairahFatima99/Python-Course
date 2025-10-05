import random #importing module

playing = True #initialise
number = str(random.randint(10,20)) #random in-built function

print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 point!")
#iterate loop till the condition is true
while playing:
    guess = input("Give me your BEST GUESS! \n")
    if number == guess:
        print(" CONGRATS YOU WON THE GAME!!!")
        print("The number was",number)
        break

    else:
        print("Your guess isn't quite right, please try again. \n")