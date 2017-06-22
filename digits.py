n=int(raw_input(""))
count = 0
if n == 0:
    count += 1
while n > 0 or n < 0:
    if n < 0:
        n = -1*n
    count += 1
    n = n/10
print "The count of the digits are:",count
