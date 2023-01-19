
def frequency(n, x):
    count = 0
     
    for i in range(n):
        if i == x: count += 1
    return count
lst = []
x = input("Enter your value of x: ")
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) 
      
print(lst)
print(frequency(n, x))
b = input("Enter your value: ")
if (frequency(n,x) > b):
    print(frequency(n,x))
