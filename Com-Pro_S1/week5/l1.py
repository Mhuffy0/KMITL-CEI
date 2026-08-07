alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(" *** Encoding (for) ***")
word, num = input("Enter a word and a number: ").split()
num = int(num)
result = ''
step = 0

#Err Check
if num < 1 or num > 26:
    print("Number must be between 1-26")
else:
    #lowercase transform
    temp = ""
    for char in word:
        # Check if the character is lowercase
        if 97 <= ord(char) <= 122:
            temp += chr(ord(char) - 32)
        else:
            temp += char
        

    #decoding
    for i in temp:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                step = (j - num) % 26
                result += alphabet[step]

    print(result)
print("===== End of program =====")