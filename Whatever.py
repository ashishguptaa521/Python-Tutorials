def function(list):
    n = len(list)
    list.sort(reverse=True)
    for x in list:
        for y in range(n):
            x += pow(10, n - y) * list[x]
    return x


length = int(input("Enter a value:"))
list = list(map(int, input("Enter numbers:").split(" ")))[:length]
print(function(list))