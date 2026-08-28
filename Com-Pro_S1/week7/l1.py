print(" *** Sum odd / Subtract even ***")
raw = input("Enter numbers : ")

total = 0

for token in raw.split():
    number = int(token)

    if number == -1:
        break

    if number % 2 != 0:
        total += number
    else:
        total -= number

digits = str(total)
result = ""
count = 0

for i in range(len(digits) - 1, -1, -1):
    result = digits[i] + result
    count += 1
    if count % 3 == 0 and i > 0:
        result = "," + result

print("Sum is", result)
print("===== End of program =====")
