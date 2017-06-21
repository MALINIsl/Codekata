input_num = (input("The number "))
arm_num = 0
val = int(input_num)
while val > 0:
	reminder = val % 10
	arm_num += reminder ** 3
	val //= 10
if int(input_num) == arm_num:
	print input_num, 'is an armstrong number'
else:
    print input_num,  'is not an armstrong number'
