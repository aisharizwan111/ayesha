#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      TechhNo
#
# Created:     17/07/2022
# Copyright:   (c) TechhNo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("hello welcm to quiz ")
playing=print(input ("you want to play? "))
if playing =="yes":
    print("lets play the game")
score=0
answere=input("what is dbs? ")
if answere=="database managment system":
    print("correct")
    score+=1
else:
    print("inccorect :(")
answere=input("what is tms? ")
if answere =="transaction managment system":
    print("correct")
    score+=1
else:
    print("inccorect :(")
answere=input(" what is ddbs? ")
if answere =="double transaction  managment system":
    print("correct")
    score+=1
else:
    print("inccorect :(")
answere=input("what is mst? ")
if answere =="minor search tree":
    print("correct")
    score+=1
else:
    print("inccorect :(" )
print(" The correct answer " + str(score))
print(" The overall score  " + str((score/4)*100))