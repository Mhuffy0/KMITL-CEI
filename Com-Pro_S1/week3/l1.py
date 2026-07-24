print(" *** Integer Property ***")
num = int(input("Enter a whole number : "))
x = "zero integer"

try:
    if num > 0:
        x = "positive integer"
    elif num < 0:
        x = "negative integer"
        
except num == 0:
    x = "zero integer"
    
if num < 0:
    mag = -num
elif num == 0:
    mag = 0
else:
    mag = num
    
parity = "Even" if mag % 2 == 0 else "Odd"

#output
print(f'{"type":>12} => {x}')
print(f'{"Magnitude":>12} => {mag}')
print(f'{"Parity":>12} => {parity}')
print("===== End of program =====")