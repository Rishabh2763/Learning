
# ------------------------Love Score Calculator-------------------------------


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
fname=name1+name2
new_name=fname.lower()
first_digit=new_name.count("t")+new_name.count("r")+new_name.count("u")+new_name.count("e")
last_digit=new_name.count("l")+new_name.count("o")+new_name.count("v")+new_name.count("e")
Love_score=int(str(first_digit) + str(last_digit))

if Love_score <=10 or Love_score >=90:
  print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif Love_score > 40 and Love_score < 50:
    print(f"Your score is {Love_score}, you are alright together.")
else:
    print(f"Your score is {Love_score}.")


# ------------------------------Treasure island game--------------------------------------

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")


ans1=input("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\" \n")

if ans1=="left":
  print("You've come across a lake. There is an island in the middle of the lake.")
  ans2=input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n")
  if ans2=="wait":
    print("You arrive at island unharmed. There is a house with three doors. One red, one blue, one yellow.")
    ans3=input("which color do you choose? \n")
    if ans3=="red":
      print("It's a room full of fire. Game Over")
    elif ans3=="yellow":
      print("You found the treasure! You win!")
    else:
      print("You enter a room of beasts. Game Over.")  
  else:
    print("You get attacked by angry trout. Game Over.")  

else:
  print("You fell into a hole. Game Over.")


