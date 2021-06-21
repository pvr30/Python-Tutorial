"""if __name__ == '__main__':
    n = int(input().strip())
    print(n)

print(__name__) """
"""
n = int(input())

for i in range(1, n+1):
    print(i, end='') """

"""
The end=' ' is just to say that you 
want a space after the end of the statement instead of a new line character. 
"""
"""
1 1 1 2

[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]

Output:

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

"""


x = int(input())
y = int(input())
z = int(input())
n = int(input())


print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c != n])


"""
"""
n = int(input())
#arr = map(int, input().split())

#print(type(arr))

array = []

for i in range(n+1):
    t = int(input())
    array.append(t)

for i in array:
    if i == n:
        print(i)
"""

n=int(input())
a=map(int,input().strip().split(" "))
a=list(a)
mx1=a[0]
mn=a[0]
for i in a:
    if(i>mx1):
        mx1=i
    if(i<mn):
        mn=i
mx2=mn
for i in a :
    if(i>mx2 and i<mx1):
        mx2=i
print(mx2)