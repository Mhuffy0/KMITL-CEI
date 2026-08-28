print(" *** Pyramid-III ***")

A_CODE = ord('a')  # ASCII code of 'a' = 97

rows = int(input("Enter height : "))
offset = 0  

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    for j in range(2 * i - 1):
        print(chr(A_CODE + offset), end="")
        offset = (offset + 1) % 26 

    print()  # Move to the next row
print("===== End of program =====")
