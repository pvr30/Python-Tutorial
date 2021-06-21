"""
m = int(input())
set_1 = set(list(map(int, input().split(" "))))
n = int(input())
set_2 = set(list(map(int, input().split(" "))))

temp = set_1.symmetric_difference(set_2)
for t in sorted(temp):
    print(t)

"""

n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    choice = input()
    temp = choice.split(" ")
    if temp[0] == 'remove':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
    elif temp[0] == 'discard':
        if int(temp[1]) in s:
            s.discard(int(temp[1]))
    elif temp[0] == 'pop':
        s.pop()


print(len(s))
print(sum(s))