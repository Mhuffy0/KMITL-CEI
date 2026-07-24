print(" *** Water Supply Calculator ***")
usage = int(input("Total usage : "))
pay = 0.00

if usage < 0:
    exit()

#Billllllllll
if usage > 5000:
    pay += (usage - 5000) * 21
    usage = 5000
if usage > 1000:
    pay += (usage - 1000) * 20
    usage = 1000
if usage > 500:
    pay += (usage - 500) * 18
    usage = 500
if usage > 100:
    pay += (usage - 100) * 15
    usage = 100
if usage > 50:
    pay += (usage - 50) * 12
    usage = 50
if usage > 10:
    pay += (usage - 10) * 10
    usage = 10
pay += usage * 5

print(f"Total Amount = {pay:,.2f} baht")
print("===== End of program =====")