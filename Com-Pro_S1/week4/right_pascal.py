num = int(input(">"))
ch = '*'
row = 1
col = num
while num > 0:
    print(f"{ch * row}")
    row += 1
    col -= 1
    
    if row == num:
        while row > 0:
            print(f"{ch * row}")
            row -= 1
    
    if row == 0:
        break