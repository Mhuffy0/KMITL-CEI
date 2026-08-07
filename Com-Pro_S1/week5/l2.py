print(" *** Maximum value ***")
raw = input("Enter some numbers : ")

#simple put raw string to list 
digit_list = [digit for digit in raw.split()]

#try convert to int
for i in range(len(digit_list)):
    try:
        digit_list[i] = int(digit_list[i])
    except ValueError:
        digit_list[i] = None
        
result = digit_list[0]

for i in digit_list:
    if i is None or i is -1:
        break
    
    elif result < i:
        result = i
        
    elif result > i:
        continue
    
    
print("Max value =", result)
print("===== End of program =====")