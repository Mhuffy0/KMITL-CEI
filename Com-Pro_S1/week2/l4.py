print(" *** Distance *** ")
u,a,t = input("Enter Velocity Acceleration Time: ").split(',')

res = float(u) * float(t) + (float(a)*float(t)**2)/2
print(f"Your Distance = {res:.2f}")