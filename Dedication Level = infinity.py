n = int(input())
 
max_hours = []
d = {}
for _ in range(n):
    name, hours =input().split(" ")
    hours = int(hours)
    max_hours.append(hours)
    d[hours] = name
 
max_hours.sort(reverse=True)
for i in range(3):
    print(d[max_hours[i]])