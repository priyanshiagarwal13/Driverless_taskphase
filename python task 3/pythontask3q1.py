import math

def min_hours(n, x):    
    if x >= n:
        return 1
    else:
        max_computers = x + 1
        total_hours = n // max_computers
        if n % max_computers != 0:
            total_hours += 1
        return total_hours
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, x = map(int, input().split())
        print(min_hours(n, x))
