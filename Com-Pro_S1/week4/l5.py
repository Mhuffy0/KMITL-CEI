print(f" *** Perpendicular Bisector ***")
raw = input("Enter x1 y1 x2 y2 : ")

x1, y1, x2, y2 = raw.split()
print(f'({x1},{y1}) ==> ({x2},{y2})')
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

if x1 == x2 and y1 == y2:
    print("Identical points.")
else:
    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    C = x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2
    
    if B >= 0:
        s = f"{A}x + {B}y"
    else:
        s = f"{A}x - {-B}y"

    if C >= 0:
        s += f" + {C}"
    else:
        s += f" - {-C}"

    print(f"f1 ==> {s} = 0")
    
    
    #negative check
    a, b, c = A, B, C
    if a <0 :
        a = -a
    if b < 0 : 
        b = -b
    if c < 0:
        c = -c
        
    #find gcd
    g = a 
    if b > g:
        g = b
    if c > g:
        g = c
        
    while g > 1:
        if a % g == 0 and b % g == 0 and c % g == 0:
            break
        g -=1
        
    if g > 1:
        A = A // g
        B = B // g
        C = C // g

    if B >= 0:
        s = f"{A}x + {B}y"
    else:
        s = f"{A}x - {-B}y"

    if C >= 0:
        s += f" + {C}"
    else:
        s += f" - {-C}"

    print(f"f2 ==> {s} = 0")
    #equation formatting
    if A < 0 or (A == 0 and B < 0):
            A = -A
            B = -B
            C = -C
    
    out = ''
    if A != 0:
        if A == 1:
            out = 'x'
        elif A == -1:
            out = '-x'
        else:
            out = str(A) + 'x'
            
    
    if B != 0:
        if out == '': #check for if out still empty
            if B == 1:
                out = 'y'
            elif B == -1:
                out = '-y'
            else:
                out = str(B) + 'y'
        else:
            if B > 0:
                if B == 1:
                    out += " + y"
                else:
                    out += " + " + str(B) + "y"
            else:
                if B == -1:
                    out += " - y"
                else:
                    out += " - " + str(-B) + "y"

    if C != 0:
        if out == "":
            out = str(C)
        else:
            if C > 0:
                out += " + " + str(C)
            else:
                out += " - " + str(-C)

    print(f"f3 ==> {out} = 0")

print("===== End of program =====")