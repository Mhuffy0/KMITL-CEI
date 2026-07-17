print(" *** Transform to seconds ***")
h,m,s = input("Enter h m s : ").split()
h = int(h)
m = int(m)
s = int(s)


#hr to sec
res_m = m + (h*60)

#min to sec
res_s = s + (res_m*60)

res = f"{res_s:,}"
print(f"{h} hours {m} minutes {s} seconds = {res} seconds")