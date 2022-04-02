phone = input("Phone number : ")
converter = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
    "11": "Eleven"
}
output = ""
for i in phone:
    output += converter.get(i, "!") + " "

print(f"Your number is : {output}")
print(converter.items())
converter.pop("11")
print(converter.items())

