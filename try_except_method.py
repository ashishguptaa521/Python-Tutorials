try:
    age = int(input("Age: "))
    income = 20000
    risks = income / age
    print(risks)
except ValueError:
    print("Please enter a numerical value.")
except ZeroDivisionError:
    print("Age cannot be 0.")