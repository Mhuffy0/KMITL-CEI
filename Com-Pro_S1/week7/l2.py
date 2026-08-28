print(" *** Reverse Odd ***")
raw = input("Enter integers : ")
numbers = [int(x) for x in raw.split()]

odds = [n for n in numbers if n % 2 != 0]

swapped = []
last = len(odds) - 1

for n in numbers:
    if n % 2 != 0:
        swapped.append(odds[last])
        last -= 1
    else:
        swapped.append(n)

print(numbers)
print(swapped)
print("===== End of program =====")