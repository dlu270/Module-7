# Daniel Lu
# 9/12/20

# This function checks whether a number is in a given range (1,10).

number = int(input("What number would you like to check?: "))

if 0<number<11:
    print (number,"is in the range")
else:
    print (number, "is out of the range")