print("*********** Fibo / Caesar **************")
print("*           a0 a1 n for Fibo           *")
print("*          word  n for Caesar          *")
print("****************************************")

x = input("Enter something : ").split()

if len(x) == 3:
    a0 = int(x[0])
    a1 = int(x[1])
    n = int(x[2])

    print(str(a0), end="")
    print(", " + str(a1), end="")

    c = 2
    #start with 2 cuz first 2 index is input
    while c < n:
        t = a0 + a1
        print(", " + str(t), end="")
        a0 = a1
        a1 = t
        c += 1
        
        if c >= n :
            print('')
else:
    front = x[0]
    back = int(x[1])
    result = ""
    i = 0
    while i < len(front):
        result += chr(ord(front[i]) + back)
        i += 1
    print(front + " => " + result)

print("===== End of program =====")