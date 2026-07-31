print(" *** Pyramid-V ***")

h = int(input("Enter height : "))

i = 0
while i < h:
    s = " " * (h - i - 1)

    if i == h - 1:
        m = "_" * (2 * h - 2)
    else:
        m = "." * (2 * i)

    print(s + "/" + m + "\\")
    i += 1

print("===== End of program =====")