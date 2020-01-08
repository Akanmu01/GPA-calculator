a = int(input( "Enter score 1: "))
b = int(input( "Enter score 2: "))
c = int(input( "Enter score 3: "))
d = int(input( "Enter score 4: "))
e = int(input( "Enter score 5: "))
f = int(input( "Enter score 6: "))
g = int(input( "Enter score 7: "))
h = int(input( "Enter score 8: "))
i = int(input( "Enter score 9: "))
sum = a + b + c + d + e + f + g + h + i
avg = sum / 100;
score = avg / 2;

print(score)
print("GRADE: ")
if score >= 4.5 :
  print ("GOOD")
elif score <= 3.5  :
  print("FIRST CLASS UPPER")
elif score <= 3.0 :
  print("FIRST CLASS LOWER")
elif score <= 2.5 :
  print("SECOND CLASS HONOUR")
elif score >= 2.0 :
  print("SECOND CLASS DIVISION")
else:
  print("BAD RESULT")