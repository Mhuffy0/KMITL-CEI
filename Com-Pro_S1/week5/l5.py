print(" *** Alphabet Sequence (a-z) ***")
raw = input("Enter character step length : ")

start_char, step_length, max_count = raw.split()
step_length = int(step_length)
max_count = int(max_count)

A_CODE = ord('a')  # 97
Z_CODE = ord('z')  # 122

is_lowercase = len(start_char) == 1 and A_CODE <= ord(start_char) <= Z_CODE

if not is_lowercase or step_length < 0 or max_count > 26:
    print("Invalid input !!!")

else:
    start_index = ord(start_char) - A_CODE
    result = ""

    for j in range(max_count):
        next_index = (start_index + j * step_length) % 26
        if result == "":
            result += chr(A_CODE + next_index)
        else:
            result += '-' + chr(A_CODE + next_index)

    print(result)
    print("===== End of program =====")
