list = [1,4,6,7,5,7,6,9]
list_2 = list.copy()
list.append(2)
print(list)
list.insert(2, 0)
print(list)
list.pop()
print(list)
list.remove(5)
print(list)
print(list.index(6))
print(list.count(7))
list.sort()
print(list)
list.reverse()
print(list)
print(list_2)
uniques = []
for numbers in list:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)
