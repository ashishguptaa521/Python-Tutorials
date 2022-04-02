

name = input("Enter your name :  ")
x = len(name)
if x <= 3:
    print("Please enter a VALID NAME MORE THAN 3 CHARACTERS.")
elif x > 3 and x <= 50:
    print("Name is ACCEPTED.")
else:
    print("A name must be BETWEEN 3 & 50 CHARACTERS.")

temp = int(input("Enter today's temperature:"))
if temp>= 30:
    print("It's a hot day.")
elif temp <= 30 and temp > 10:
    print("It's a good day.")
elif temp <= 30 :
    print("It's a cold day!")