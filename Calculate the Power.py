import math
 
def power(A, B):
    if B == 0:
        return 1
        
    temp = power(A,B//2)%1000000007
    
    if B%2 == 0:
        return (temp * temp) % 1000000007
    else:
        return (A * temp * temp) % 1000000007
    
A, B = [int(x) for x in input().split()]
ans = int(power(A,B))
print(ans)