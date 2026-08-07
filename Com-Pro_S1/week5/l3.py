print(" *** Pyramid-III ***")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rows = int(input("Enter height : "))
current_text = alphabet[0]  # Start with 'a'

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    
    for j in range(2 * i - 1):
        print(current_text, end="")
        
        #check current_text index
        for k in range(len(alphabet)):
            if current_text == alphabet[k]:
                current_text = alphabet[(k + 1) % 26]
                break
    
    print()  # Move to the next row
print("===== End of program =====")