print(" *** Min Max Avg ***")
a, b, c = input("Enter 3 numbers : ").split()
a, b, c = float(a), float(b), float(c)

#hardcoded sort ;>
min, mid, max = a, b, c

if a > b:
    if a > c:
        max = a
        if b > c:
            mid = b
            min = c
        else:
            mid = c
            min = b
    else:
        max = c
        mid = a
        min = b
if b > a:
    if b > c:
        max = b
        if a > c:
            mid = a
            min = c
        else:
            mid = c
            min = a
    else:
        max = c
        mid = b
        min = a

Avg = (min + mid + max) / 3

print(f"min, mid, max ==> {min}, {mid}, {max}")
print(f"Average ==> {Avg:.2f}")