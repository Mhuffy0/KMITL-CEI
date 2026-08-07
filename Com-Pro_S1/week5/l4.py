print(" *** Butterfly ***")
n = int(input("Input a positive integer : "))
if n <= 0:
    print("!!!Please enter positive number!!!")
    
else:
    print()
    # Upper part of the butterfly
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    
    # Lower part of the butterfly
    for i in range(n-1, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
        
    print()
print("===== End of program =====")