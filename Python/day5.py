


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




