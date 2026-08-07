print(" *** Alphabet Sequence (a-z) ***")
raw = input("Enter character step length : ")

start_char, step_length, max_count = raw.split()
step_length = int(step_length)
max_count = int(max_count)

Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = ""

if start_char not in lowercase or start_char in Uppercase or step_length < 0 or max_count > 26:
    print("Invalid input !!!")

else:
    for i in range(len(lowercase)):
        start_index = None
        if start_char == lowercase[i] and max_count > 0:
            start_index = i
        
        if start_index != None:
            for j in range(max_count):
                next_index = (start_index + j * step_length) % 26
                if result == "":
                    result += lowercase[next_index]
                else:
                    result += '-' + lowercase[next_index]
    
    print(result)
    print("===== End of program =====")