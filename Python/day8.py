import math
# ----------------------------greet()---------------------
def greet(name,location):
  print("Hewwoh",name)
  print("Good Mornings",name)
  print("Meeeooow..........","you are in",location)

greet(location="Virginia",name="Rishabh")



# -------------------------------------Paint Area Calculator----------------------------------
def paint_calc(height,width,cover):
  number_of_cans=(height*width)/cover
  total_cans=math.ceil(number_of_cans)
  print(f"You'll need {total_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# -------------------------------------Prime Number Checker----------------------------------
def prime_checker(number):
  count=0
  for i in range(1,number+1):
    if number%i==0:
      count+=1
  
  
  if count<3:
    print("It's a prime number.")
  else:
    print("It's not a prime number")  
    


n = int(input("Check this number: "))
prime_checker(number=n)

