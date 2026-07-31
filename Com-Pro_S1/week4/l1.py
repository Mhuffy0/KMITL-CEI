print(" *** Odd integer summation from 1 to n ***")
raw = input("Enter an integer(n) : ")
try :
    raw = int(raw)
except ValueError:
    print(f"{raw} ==> Invalid input !!! ")
    print("===== End of program =====")
    exit()
    
    
sum = 0
start = 0
char = '' if raw > 0 else '0'

while raw > 0:
    while raw > start:
        if start % 2 != 0: #if odd
            sum += start
            if char == '':
                char += str(start)
            else :
                char += '+' + str(start)
        start += 1
    
    if start == raw:
        if raw % 2 != 0:
            sum += raw
            if char == '':
                char += str(start)
            else :
                char += '+' + str(start)
        break

print(f"Summation => {char} = {sum}")
print(f"===== End of program =====")