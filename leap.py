year=int(input())
if(year%100==0 and year%400==0):
    leap=False
elif(year%4==0):
    leap=True
else:
    leap=False
print(leap)        