name=input("enter ur name")
l=len(name)

print("Your name has",l,"characters")


print(3 * 3 + 3 / 3 - 3)
print(12 // 7) 
#  (floor division and modular divison are different)


# -------------------------------F-strings----------------------------------------------------


score=10
height=1.8
iswinning=True

print(f"Your score is {score} and height is {height} and winning is {iswinning}")
print("Your score is {} and height is {} and winning is {}".format(score, height, iswinning))



# ---------------------------day2 project -- tip calculator/---------------------------------------

print("Welcome to the tip calculator")


bill=float(input("what was the the total bill "))
tip=int(input("what percentage tip would you like to give "))
n=int(input("how many people to split the bill "))

total_pay=round(bill + bill* (tip / 100),2)
each_pay=round(total_pay / 7,2)
print("each person should pay {}$".format(each_pay))
