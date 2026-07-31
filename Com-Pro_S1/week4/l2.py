print(f" *** Arithmetic Sequence ***")
raw = input("Enter 2 numbers : ")

m, x = raw.split(' ')
m = int(m)
x = int(x)

count = 0
while count < 11:
    char = str(m) + ' '
    m += x
    count += 1
    print(f"{char}", end='')
    
    if count == 10:
        break
    
print(f"\n===== End of program =====")