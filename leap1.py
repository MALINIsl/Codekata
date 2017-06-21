a= int(raw_input("The entered year "))
if a % 4 ==0 and a % 400 ==0 and a % 100 !=0:
print(a, " is Leap year")
else:
print(a, " is NOT a leap year")
