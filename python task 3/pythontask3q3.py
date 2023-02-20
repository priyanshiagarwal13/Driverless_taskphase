class bit:
    def binary(self, n: int) -> int:
        mod=100000000 +7
        size=0
        m=0
        for i in range(1,n+1):
            if(i&(i-1)==0):
                size+=1
            m=((m<<size)%mod +i)%mod
        return m
n=int(input("Enter number: "))
x = bit()
print(x.binary(n))





