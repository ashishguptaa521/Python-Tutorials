#Convert a person's entered weight into kilos or pounds.
def lb_to_kg( weight):
    print(f"Your weight in kg is {weight * 0.453592} .")
def kg_to_lb(weight):
    print(f"Your weight in pound is {weight / 0.453592} .")

weight = int(input("Enter your weight:"))
print(lb_to_kg(weight))
