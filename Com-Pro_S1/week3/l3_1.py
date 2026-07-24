print("============================================================")
print("                32-BIT NUMBER REPRESENTATION                ")
print("============================================================")

raw = input("Enter a number : ")

bits = 32                      
#const
sign_weight = 2 ** (bits - 1)   # 2^31 
full = 2 ** bits                # 2^32  2complement
allones = 2 ** bits - 1         # 2^32 - 1 patternfefeasfdage
maxval = 2 ** (bits - 1) - 1    # biggest signed val
minval = -(2 ** (bits - 1))     # smallest signed val


#datatype_cechker
isint = True
try:
    n = int(raw)
except ValueError:
    isint = False
    
isfloat = True
if isint == False:
    try:
        fnum = float(raw)
    except ValueError:
        isfloat = False
        
if isint:
    print("------------------------------------------------------------")
    print("INPUT INFORMATION")
    print("------------------------------------------------------------")
    
    print("Data type" + " " * 13 + ": Integer")
    print("Decimal value" + " " * 9 + ": " + str(n))

    #its magical raw 32 bit checker
    if n < -2147483648 or n > 2147483647:
        print("------------------------------------------------------------")
        print("ERROR")
        print("------------------------------------------------------------")
            
        print("The entered value is outside the range of a")
        print("32-bit signed integer.")
        print("Minimum value" + " " * 9 + ": -2147483648")
        print("Maximum value" + " " * 9 + ": 2147483647")
        
    else:
        #sign info
        if n < 0:
            mag = -n
            sign = "Negative"
            signbit = 1
        elif n == 0:
            mag = 0
            sign = "Zero"
            signbit = 0
        else:
            mag = n
            sign = "Positive"
            signbit = 0
            
        #sign print zone
        ##the " " * num is for spacing i lazy to put format kub"
        print("Sign" + " " * 18 + ": " + sign)
        print("Sign bit" + " " * 14 + ": " + str(signbit))
        print("Magnitude" + " " * 13 + ": " + str(mag))
        
        print("------------------------------------------------------------")
        print("               32-BIT BINARY REPRESENTATIONS                ")
        print("------------------------------------------------------------")
        print("Format: sign_bit_7bits_8bits_8bits_8bits\n")
        
        # unsigned 32 bit
        if n >= 0:
            usign_mag = n
            uones = n
            utwos = n
        else:
            usign_mag = sign_weight - n
            uones = allones + n
            utwos = full + n

        #2complement to bitchhunck (g1..g4)
        s = utwos // 2 ** (bits - 1)
        g1 = (utwos // 2 ** 24) % 2 ** 7
        g2 = (utwos // 2 ** 16) % 2 ** 8
        g3 = (utwos // 2 ** 8) % 2 ** 8
        g4 = utwos % 2 ** 8
        twos = f"{s:b}_{g1:07b}_{g2:08b}_{g3:08b}_{g4:08b}"

        if n == minval:
            print("pass")
        else:
            #copy paste the formula and change the usign
            s = usign_mag // 2 ** (bits - 1)
            g1 = (usign_mag // 2 ** 24) % 2 ** 7
            g2 = (usign_mag // 2 ** 16) % 2 ** 8
            g3 = (usign_mag // 2 ** 8) % 2 ** 8
            g4 = usign_mag % 2 ** 8
            smag = f"{s:b}_{g1:07b}_{g2:08b}_{g3:08b}_{g4:08b}"

            s = uones // 2 ** (bits - 1)
            g1 = (uones // 2 ** 24) % 2 ** 7
            g2 = (uones // 2 ** 16) % 2 ** 8
            g3 = (uones // 2 ** 8) % 2 ** 8
            g4 = uones % 2 ** 8
            ones = f"{s:b}_{g1:07b}_{g2:08b}_{g3:08b}_{g4:08b}"
            
            print(f"Sign-magnitude        : {smag}")
            print(f"One's complement      : {ones}")
            print(f"Two's complement      : {twos}")
            
elif isfloat:
    print("------------------------------------------------------------")
    print("INPUT INFORMATION")
    print("------------------------------------------------------------")
    
    print("Data type" + " " * 13 + ": Floating-point number")
    print("Value" + " " * 17 + ": " + str(raw))
    print("\nInteger representations are not applicable to this value.")
    
else:
    print("------------------------------------------------------------")
    print("INVALID INPUT")
    print("------------------------------------------------------------")
    
    print(f'"{raw}" is not a valid number.')
    
    
print("============================================================")
print("                       END OF PROGRAM                       ")
print("============================================================")