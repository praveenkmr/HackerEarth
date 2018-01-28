n = int(input())
 
for _ in range(n):
    str = input()
    cnt = 0
    for ch in str:
        if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
            cnt +=1
    
    print(cnt)