print(" *** The number of distinct remainders ***")
raw = input("Enter a divisor / a sequence : ")

left, right = raw.split("/")
divisor = int(left)

remainders = []
#modulo each ele in right  by divisor and store 
# the distinct remainders in r list

for token in right.split():
    r = int(token) % divisor
    if r not in remainders:
        remainders.append(r)

print("Distinct remainders =", len(remainders))
print("===== End of program =====")
