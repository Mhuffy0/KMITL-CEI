print(" *** Transform second ***")

raw = input("Enter seconds : ")
valid = True

try:
    sec = int(raw)
except ValueError:
    valid = False

if not valid:
    print(f"! ! ! please enter a whole number ==> {raw}")
    print(f"This number ({raw}) is not VALID !!!")
    print("===== End of program =====")
    
if sec < 0:
    print(f"This number ({raw}) is not VALID !!!")
    print("===== End of program =====")    
else:
    result = f"{sec:,} seconds ==> "

#divide the sec with each convertor to prevent the remian sec bug
    wk = sec // 604800
    sec = sec % 604800
    d = sec // 86400
    sec = sec % 86400
    hr = sec // 3600
    sec = sec % 3600
    m = sec // 60
    sec = sec % 60

    if wk== 1:
        result += f"{wk} week "
    elif wk > 1:
        result += f"{wk} weeks "
        
    if d == 1:
        result += f"{d} day "
    elif d > 1:
        result += f"{d} days "
        
    if hr == 1:
        result += f"{hr} hour "
    elif hr > 1:
        result += f"{hr} hours "
        
    if m == 1:
        result += f"{m} minute "
    elif m > 1:
        result += f"{m} minutes "
    
    if sec == 1:
        result += f"{sec} second "
    elif sec > 1:
        result += f"{sec} seconds "

    print(result)
    print("===== End of program =====")


