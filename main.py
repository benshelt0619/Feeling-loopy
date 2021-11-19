#Examples 1a and 1b
"""for i in range(2, 15, 3):
  print (i)"""

"""counter=-1
while counter<14:
  counter+=3
  print(counter)"""



#Example 2
"""value = int(input("Enter number up to 100: "))
for i in range(0,value):
  value+=i
print(value)"""



#Example 3
"""high_score = 0
total_score = 0
for i in range(3):
  my_score = int(input("Enter number: " ))
  while my_score > 300 or my_score < 0:
    print("Invalid, Try again")
    my_score = int(input("Enter number: " ))
  total_score += my_score
if my_score > high_score:
    high_score=my_score
print()
print("The 3 game total is: ", total_score)
print("Your high score is: ", high_score)"""



#Example 4
"""import random
hitpoints=100
decision=("y")
damage=0
while hitpoints > 0 and decision != ("n"):
  decision=input("Intitate another round? (y/n) ")
  if decision==("y"):
    damage=random.randint(0,100)
    hitpoints-=damage
    print()
    print("You took", damage, "damage!")
    print("Your current HP is", hitpoints)
    print()
  else:
    print()
    print("Invalid input, please try again!")
    print()
  if decision==("n") or hitpoints <= 0:
    print("Game Over!")"""



#Example 5
"""for loop1 in range(1,4):
  print("No homework tonight, please")
  for loop1 in range(loop1):
    print(", please")"""



"""#Example 6
import random
score=0
correct = True
while correct:
  flip = random.randint(0,1)
  guess = int(input("Heads/Tails? (h=1/t=0) "))
  if flip == guess:
    print("CORRECT!")
    print()
    score+=1
    print("Score = ",score)
    print()
  if flip != guess:
    print("WRONG!")
    print()
    print("Score = ", score)
    correct = False"""
