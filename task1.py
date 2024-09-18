import random
import math


print('"NUMBER GUESSING GAMEEEEE!!!"')
print("Enter your number ", end= "")
loop = True
my_num = int(math.floor((random.random() * 100)+1))


while loop:
    player_num = int(input(": "))
    print(my_num)
    if my_num == player_num:
        print(f"Yay we picked the same number, {my_num}")
        loop = False
    elif player_num > my_num:
        print("Try a smaller number")
    elif player_num < my_num:
        print("Try a bigger number")
    else:
        print("Not sure what that was please input a number")
