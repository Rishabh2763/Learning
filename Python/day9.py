# ----------------------------------Grading Program----------------------------------
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}
for key in student_scores:
  print (key)
  marks=student_scores[key]
  print(f"Their marks is {marks}")
  if marks > 90:
    marks="Outstanding"
  elif marks >80:
    student_grades[key]="Exceeded expectations"
  elif marks >70:
    student_grades[key]="Acceptable" 
  else:
    student_grades[key]="Fail"     

print(student_grades)


# ---------------------------------interactive coding exercise--------------------------
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_name,times_visited,cities_visited):
  travel_log.append({
        "country": country_name,
        "visits": times_visited,
        "cities": cities_visited

  })
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# --------------------------------Blind auction--------------------------------------------
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
data={}
ans=True
while ans:
  name=input("what is your name. ")
  bid=int(input("what is your bid: $")) 
  data[name]=bid
  their_ans=input("Are there any more bidders? Type 'yes' or 'no' ")
  if their_ans == "no":
    ans=False
  # else:
  #   clear()   --- dont know how to clear terminal in vscode
max_bidder=max(data,key=data.get)
max_bid=data[max(data,key=data.get)]
print("winner is",max_bidder,"with a bid of",max_bid,"$")
print("goodbye")












