x=1
y=50
Sum=0
for number in range(x, 50 + 1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Sum=Sum+number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number,Sum))        