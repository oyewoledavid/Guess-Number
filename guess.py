my_number = 69

user_guess = int(input("Enter your guess "))
if user_guess == int(user_guess):
    print("This is a number")
else:
    print("This is not a number")

if user_guess == my_number:
    print("You are correct")
elif user_guess < my_number:
    print("This is a bit low, go higher")
elif user_guess > my_number:
    print("This is too high, go lower")
else:
    print("Invalid Option")