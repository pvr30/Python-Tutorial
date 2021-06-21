"""
s1 = {1, 2, 3, 5, 6}
s2 = {9, 8, 5, 6, 3, 2, 1, 4, 7}

print(s1.issubset(s2))
if s1.issubset(s2):
    print("True")
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
while n > 0:
    e1 = int(input())
    s1 = set(list(map(int, input().split())))
    e2 = int(input())
    s2 = set(list(map(int, input().split())))
    print(s1.issubset(s2))
    n = n - 1
    

