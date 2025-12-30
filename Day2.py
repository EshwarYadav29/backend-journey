
n=int(input("Enter an integer n:"))
for i in range(1,n+1):
  if (i>50):
    break
  if (i%3==0):
    continue
  print(i)



def grade(marks):
  if marks<40:
    return 'Fail'
  elif marks>=40 and marks<60:
   return 'Pass'
  elif marks>=60 and marks<80:
     return 'Good' 
  else:
     return 'Excellent'
  
for i in range(5):
  m=int(input("Enter marks:"))
  print("Grade:",grade(m))

  
names = []
count = 0

for i in range(5):
    x = input("Enter name: ")
    names.append(x)

    if x[0].lower() in 'aeiou':
        count += 1

print("Names starting with a vowel:", count)
