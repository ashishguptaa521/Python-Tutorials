has_high_income = True
has_good_credit = False
if has_good_credit and has_high_income :
    print("You're eligible for loan")
else:
    print("You aren't eligible for loan.")

    has_high_income = True
    has_good_credit = False
    if has_good_credit or has_high_income:
        print("You're eligible for loan")
    else:
        print("You aren't eligible for loan.")

has_high_income = True
has_criminal_background = False
if has_good_credit and not has_criminal_background :
    print("You're eligible for loan")
