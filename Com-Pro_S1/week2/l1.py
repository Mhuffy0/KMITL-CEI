line1 = " *** Get input as string ***"
line2 = "Enter a name : "

print(f"{line1:^10}")
name = input(f"{line2:^8}")
print(f"Hello  {name:>4}")
print(f"{name:^4}",f"{name:^4}",f"{name:^4}",f"{name:^4}",f"{name:^4}", sep='-')