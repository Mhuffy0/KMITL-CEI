bits = 32                       # change this and everything below follows
width = 60                      # width of the banner lines
col = 22                        # column where every " : " lines up

# --- constants that come only from the number of bits ---
sign_weight = 2 ** (bits - 1)   # 2^31  -> weight of the sign bit
full = 2 ** bits                # 2^32  -> used to build two's complement
allones = 2 ** bits - 1         # 2^32 - 1 -> the pattern 1111...1111
maxval = 2 ** (bits - 1) - 1    # biggest signed value
minval = -(2 ** (bits - 1))     # smallest signed value

title = str(bits) + "-BIT NUMBER REPRESENTATION"
lpad = (width - len(title)) // 2
print("=" * width)
print(" " * lpad + title + " " * (width - len(title) - lpad))
print("=" * width)

raw = input("Enter a number : ")

# --- decide the data type ---
isint = True
try:
    n = int(raw)
except ValueError:
    isint = False

isfloat = True
if not isint:
    try:
        fnum = float(raw)
    except ValueError:
        isfloat = False


if isint:
    print("-" * width)
    print("INPUT INFORMATION")
    print("-" * width)
    print("Data type" + " " * (col - len("Data type")) + ": Integer")
    print("Decimal value" + " " * (col - len("Decimal value")) + ": " + str(n))

    if n < minval or n > maxval:
        print("-" * width)
        print("ERROR")
        print("-" * width)
        print("The entered value is outside the range of a")
        print(str(bits) + "-bit signed integer.")
        print("Minimum value" + " " * (col - len("Minimum value")) + ": " + str(minval))
        print("Maximum value" + " " * (col - len("Maximum value")) + ": " + str(maxval))
    else:
        # --- sign information ---
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

        print("Sign" + " " * (col - len("Sign")) + ": " + sign)
        print("Sign bit" + " " * (col - len("Sign bit")) + ": " + str(signbit))
        print("Magnitude" + " " * (col - len("Magnitude")) + ": " + str(mag))

        header = str(bits) + "-BIT BINARY REPRESENTATIONS"
        hpad = (width - len(header)) // 2
        print("-" * width)
        print(" " * hpad + header + " " * (width - len(header) - hpad))
        print("-" * width)
        print("Format: sign_bit_7bits_8bits_8bits_8bits\n")

        # --- turn n into the positive integer whose bits ARE the pattern ---
        # for a positive number the pattern is just the number itself;
        # for a negative number each system needs a different conversion.
        if n >= 0:
            usm = n
            uones = n
            utwos = n
        else:
            usm = sign_weight - n     # sign bit + magnitude
            uones = allones + n       # invert the bits of the magnitude
            utwos = full + n          # 2^n - magnitude

        # two's complement always fits, so build it first
        s = utwos // 2 ** (bits - 1)      # the sign bit (top bit)
        g1 = (utwos // 2 ** 24) % 2 ** 7  # next 7 bits
        g2 = (utwos // 2 ** 16) % 2 ** 8  # next byte
        g3 = (utwos // 2 ** 8) % 2 ** 8   # next byte
        g4 = utwos % 2 ** 8               # last byte
        twos = f"{s:b}_{g1:07b}_{g2:08b}_{g3:08b}_{g4:08b}"

        if n == minval:
            # the smallest value has no sign-magnitude / one's complement form
            smag = "not representable in " + str(bits) + "-bit sign-magnitude"
            ones = "not representable in " + str(bits) + "-bit one’s complement"
        else:
            s = usm // 2 ** (bits - 1)
            g1 = (usm // 2 ** 24) % 2 ** 7
            g2 = (usm // 2 ** 16) % 2 ** 8
            g3 = (usm // 2 ** 8) % 2 ** 8
            g4 = usm % 2 ** 8
            smag = f"{s:b}_{g1:07b}_{g2:08b}_{g3:08b}_{g4:08b}"

            s = uones // 2 ** (bits - 1)
            g1 = (uones // 2 ** 24) % 2 ** 7
            g2 = (uones // 2 ** 16) % 2 ** 8
            g3 = (uones // 2 ** 8) % 2 ** 8
            g4 = uones % 2 ** 8
            ones = f"{s:b}_{g1:07b}_{g2:08b}_{g3:08b}_{g4:08b}"

        print("Sign-magnitude" + " " * (col - len("Sign-magnitude")) + ": " + smag)
        print("One’s complement" + " " * (col - len("One’s complement")) + ": " + ones)
        print("Two’s complement" + " " * (col - len("Two’s complement")) + ": " + twos)

elif isfloat:
    print("-" * width)
    print("INPUT INFORMATION")
    print("-" * width)
    print("Data type" + " " * (col - len("Data type")) + ": Floating-point number")
    print("Value" + " " * (col - len("Value")) + ": " + raw)
    print()
    print("Integer representations are not applicable to this value.")

else:
    print("-" * width)
    print("INVALID INPUT")
    print("-" * width)
    print('"' + raw + '" is not a valid number.')

end = "END OF PROGRAM"
epad = (width - len(end)) // 2
print("=" * width)
print(" " * epad + end + " " * (width - len(end) - epad))
print("=" * width)
