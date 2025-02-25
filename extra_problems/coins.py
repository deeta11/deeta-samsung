coins=[1,2,5,10]
n=int(input("Enter price:"))
d={}
itr=len(coins)-1
while n>0:
    div=n//coins[itr]
    d.setdefault(coins[itr],div)
    n=n%coins[itr]
    itr=itr-1
for key,val in d.items():
    if val!=0:
        print(f"{key} : {val} coins")

