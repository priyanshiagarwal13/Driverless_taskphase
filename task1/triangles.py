n = int(input())
n1 = n
n2 = n - 1
i = 1
while i<=n1:
    j = 1
    while j<= i -1:
        print(' ',end ='')
        j +=1
    k = 1
    p = i
    while k <=n1 -i+1:
        print(p,end='')
        k+=1
        p +=1
    print()
    i+=1
    
y = 1
while y<=n2:
    j = 1
    while j<= n2 -y:
        print(' ',end ='')
        j +=1
    k = 1
    p = n2 -y +1
    while k <=y +1:
        print(p,end='')
        k+=1
        p+=1
    
    print()
    y +=1
    