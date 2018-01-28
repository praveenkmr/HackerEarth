from sys import stdin
 
for num in stdin:
    print(bin(int(num)).count("1"))