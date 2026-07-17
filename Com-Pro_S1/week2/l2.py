print(" *** Number Fun ***")
num = int(input(f"Enter a 3-digit number : "))

#Calculate
sq = (num ** 2)
fl = num * 0.25
bi = num & 0xFF
temp = int(bi)
res = f"{temp:08b}"

#Output
arr = "=>"

print(f"\nYou have entered {arr:>6} {num}")
print(f"Square {arr:>16} {sq:,}")
print(f"25% 3 decimal places {arr:>1} {fl:.3f}%")
print(f"Flipping {arr:>14} {str(num)[::-1]}")
print(f"Hexadecimal {arr:>11} {num:0x} or {num:0X}")
print(f"Binary {arr:>16} {num:0b}")
print(f"Binary right 8-digit {arr:>1} {res[:4]} {res[4:]}")
