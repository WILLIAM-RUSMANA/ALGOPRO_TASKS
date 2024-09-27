from random import random # incase of error reset game.txt to "0 0 0"
from math import floor   # don't Ctrl + C 

def display_stats(points, lives, level):    #prints out stats
    print(f"Points: {points}\nLives: {lives}\nLevel: {level}")
def instructions():   #print guide
    print("MATH GAME\n[play] to start a new game\n[stat] to print stats\n[quit] to quit game")

points, lives, level = 0,0,0    #Initialize variables here
with open("game.txt", "r") as file:   # get stats from game.txt
    points, lives, level = map(int, file.readline().split())  # make strs into ints

instructions()
play = True
while play:               # Loop till user enters close
    action = input(": ")
    if action == "play":
        correct = 0
        for i in range(5):
            x = floor(random()*100)
            y = floor(random()*100)
            ans = x+y
            print(f"({i+1}) {x} + {y} = ", end="") # display question
            user_ans = input()
            if user_ans.isdigit(): # check if input is a int
                user_ans = int(user_ans)
                if user_ans == ans:   # correct ans will increase point by 1
                    points += 1
                    correct +=1
                    print(f"No. {i+1} is correct (+1 points)")
                else:
                    print("Incorrect... you loss a point")
            else: # respond if input is not int
                print("Incorrect you loss a point")
                lives -= 1
        if correct >= 5: # rewards extra points if all answers are correct
            points += 5
            print("You got 5 extra points for aceing IT!!!")
        if lives <= 0:
            points = 0
        lives = 3  # regen back lives back to 3
        if points >= 15:
            level += 1
            points = 0
        with open("game.txt", "w") as file:
            file.write(f"{points} {lives} {level}")
        display_stats(points, lives, level)
        
    elif action == "stat":
        display_stats(points, lives, level)
    elif action == "close" or action == "quit": # end loop
        play = False
    else:
        print("inv input")
        instructions()
          

