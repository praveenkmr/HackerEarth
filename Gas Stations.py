n, x = [int(x) for x in input().split()]
 
l = [int(x) for x in input().split()]
 
cnt = 0
total = 0
 
for item in l:
    total += item
    cnt += 1
    if total > x:
        break
    
print(cnt)
    