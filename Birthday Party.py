T = int(input())
for _ in range(T):
    a, b = [int(x) for x in input().split()]
    if b%a == 0:
        print("Yes")
    else:
        print("No")