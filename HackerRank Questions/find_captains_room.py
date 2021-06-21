
"""
from collections import Counter

l1 = [1,5,6,7,8,9,1,5,6,8]
c = Counter(l1)
for i in c:
    print(c[i])

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
group_list = list(map(int, input().split()))

c = Counter(group_list)

for i in c:
    if c[i] == 1:
        print(i)

        