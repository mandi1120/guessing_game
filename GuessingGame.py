# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 07:59:30 2017

@author: Mandi
"""
import random

guessestaken =  0
secretnumber = random.randint(1,50)
print ("****** Guess my secret number in 7 attempts to win ******")
     
for guessestaken in range(1,8):

   print("Take a guess")
   guess = int(raw_input())
   
   if guess < secretnumber:
       print ("Guessed too low")
       
   elif guess > secretnumber:
       print ("Guessed too high")

   else:
       break
   
if guess == secretnumber:
    print("****** You guessed correctly in " + str(guessestaken) + " attempts. ******")
else:
    print("****** Game over, the number was " + str(secretnumber) + ". ******")



 """ While loop version

import random

guessestaken =  0
secretnumber = random.randint(1,50)
print ("****** Guess my secret number in 7 attempts to win ******")
     
while guessestaken < 8:
   print("Take a guess")
   guess = int(raw_input())
   
   guessestaken = guessestaken + 1
   
   if guess < secretnumber:
       print ("Guessed too low")
   elif guess > secretnumber:
       print ("Guessed too high")
   else: 
       break
   
if guess == secretnumber:
    print("****** You guessed correctly in " + str(guessestaken) + " attempts. ******")
else:
    print("****** Game over, the number was " + str(secretnumber) + ". ******")    

 """
    