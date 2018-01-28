for _ in range(n):
    name1, name2 = input().split(" ")
    name1 = ''.join(sorted(name1))
    name2 = ''.join(sorted(name2))
    #print(name1, name2)
    if name1 == name2:
        print("YES")
    else:
        print("NO")