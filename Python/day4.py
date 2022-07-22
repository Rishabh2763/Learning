import random

# --------------------------------------random module-------------------------------------
a=int(input("enter staring no"))
b=int(input("enter ending no"))
num = a + random.random()* (b-a)
print(num)


#--------------------------------Banker roulette------------------------------------------
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num=random.randint(0,len(names)-1)
random_person= names[num]
print(f"{random_person} is going to buy the meal today!")


# --------------------------------Treasure Map--------------------------------------------

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n {row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
x = int(position[0])
y = int(position[1])
map[y-1][x-1]="X"
print(f"{row1}\n{row2}\n{row3}")

# ---------------------------------------Rock Paper Scissors Game-------------------------
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp=random.randint(0,2)
ans = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))



if ans == 0:
  print(rock)
  print("You Choose Rock")
  print("\n")
  if comp == 0:
    print(rock)
    print("Computer Choose Rock")
    print("Tie")
  elif comp == 1:
    print(paper)
    print("Computer Choose paper")
    print("You Loose")
  else:
    print(scissors)
    print("Computer Choose scissors")  
    print("You Win")  
elif ans == 1:
  print(paper)  
  print("You Choose Paper")
  print("\n")
  if comp == 0:
    print(rock)
    print("Computer Choose Rock")
    print("You Win")
  elif comp == 1:
    print(paper)
    print("Computer Choose paper")
    print("Tie")
  else:
    print(scissors)
    print("Computer Choose scissors")  
    print("You Loose")  
  
else:
  print(scissors)
  print("You Choose Scissors")
  print("\n")
  if comp == 0:
    print(rock)
    print("Computer Choose Rock")
    print("You Loose")
  elif comp == 1:
    print(paper)
    print("Computer Choose paper")
    print("You Win")
  else:
    print(scissors)
    print("Computer Choose scissors")  
    print("Tie")  
  

