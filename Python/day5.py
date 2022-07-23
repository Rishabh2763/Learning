import random


# --------------------------------Avg Height----------------------------------------------

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height=0

for height in student_heights:
  total_height+=height
print(total_height)    

total_students=0
for students in student_heights:
  total_students+=1

avg_height = total_height/total_students
print(round(avg_height))

# --------------------------------------Max Score-----------------------------------------



student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 90 87 78 99 87
max_score=0
for score in student_scores:
  if score > max_score:
    max_score=score
  

print(f"The highest score is {max_score}")

# -----------------------------------Adding even numbers----------------------------------
sum=0
for num in range(1,101):
  if num % 2 == 0:
    sum += num
print(sum)

#-----------------------------Fizz Buzz game-----------------------------------------------

for i in range(1,101):
  if i % 3 == 0:
    if i % 5==0:
      print("FizzBuzz")
    else:
      print("Fizz")  
  elif i % 5 ==0:
    print("Buzz")
  else:
    print(i)  


# ------------------------------Password generator-----------------------------------


#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all=[letters, numbers, symbols]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password=""
cycle= random.randint(0,2)

for i in range(0, nr_letters):
  password= password + random.choice(letters)
print(password)  


for i in range(0,nr_numbers):
  password= password + random.choice(numbers)
print(password)   


for i in range(0, nr_symbols):
  password= password + random.choice(symbols)
print(password)  

result = random.sample(password, len(password))
real_password = "".join(result)
print(f"Your password is: {real_password}")



