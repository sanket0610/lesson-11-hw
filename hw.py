
n=int(input("Enter number"))
r=0
while n>0:
    re=n%10
    r=re + (r*10)
    n=int(n/10)
    print("Reverse is", r)