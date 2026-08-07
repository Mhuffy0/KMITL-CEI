print(" *** Maximum value ***")
raw = input("Enter some numbers : ")
stopped = False

digit_list = raw.split()
max_value = None

for digit in digit_list:
    if digit == "stop":
        stopped = True
        break
    try:
        num = int(digit)
        if num == -1:
            stopped = True
            break
        
        if max_value is None or num > max_value:
            max_value = num
    except ValueError:
        continue


if stopped or max_value is not None:
    print(f"Max value = {max_value}")
else:
    print("Max value = None")

print("===== End of program =====")