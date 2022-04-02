from utils import find_max
list = []
num = int(input("numbers range:"))
for i in range(num):
    abc = input(("Enter numbers:"))
    list.append(abc)
print(find_max(list))
print(max(list))
