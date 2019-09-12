import random

secret = int(input("Please think of a number between 0 and 100!"))

n = random.randint(0,100)
low = 0
high = 100

while n != secret:

    print("Is your secret number " + str(n) + "?")

    option = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if option == 'h':
        high = n
    elif option == 'l':
        low = n
    elif option == 'c':
        print("Game over. Your secret number was:", n)
    else:
        print("Invalid option, try again")
    n = random.randint(low,high)



low = 0
high = 100
ans = int((high + low) / 2)
guess = False
print('Please think of a number between 0 and 100!')
while guess != True:

    print("Is your secret number " + str(ans) + "?")

    option = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if option == 'h':
        high = ans
    elif option == 'l':
        low = ans
    elif option == 'c':
        print("Game over. Your secret number was:", ans)
        guess = True
    else:
        print("Invalid option, try again")
    ans = int((high + low) / 2)

