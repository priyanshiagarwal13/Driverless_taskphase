n=int(input("Number of rows: "))

m = list(range(1, n+1))
n = list(range(2, n+1))
q = list(reversed(n))

for i in q:
    y=n-i
    z=(2*i)-1
    for j in range(y):
        print(" ",end="")
    for j in range(z,0,-1):
        print(j,end="")
    print()

for i in m:
    y=n-i
    z=(2*i)-1
    for j in range(y):
        print(" ",end="")
    for j in range(z,0,-1):
        print(j,end="")
    print()
    
