print(" *** Maximum occurence ***")
raw = input("Enter numbers : ")

numbers = [int(x) for x in raw.split()]

counted = []

for n in numbers:
    if n == -1:
        break
    counted.append(n)

max_count = 0

for n in counted:
    count = 0
    for m in counted:
        if m == n:
            count += 1
    if count > max_count:
        max_count = count

max_occ = []

for n in counted:
    count = 0
    for m in counted:
        if m == n:
            count += 1
    if count == max_count and n not in max_occ:
        max_occ.append(n)

print(numbers)
print("Max count =", max_count)
print("Max occurence =", max_occ)
print("===== End of program =====")
