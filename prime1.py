while True:
	num = input("The number ")
	number = int(num)
  	for i in range(2, number):
			if number % i == 0:
				print("is not a prime number.\n")
		else:
			print("is a prime number.\n")
