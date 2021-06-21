# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    n1 = int(input())
    while n1 > 0:
        choice = input().split()
        if choice[0] == 'intersection_update':
            s1 = set(map(int, input().split()))
            s.intersection_update(s1)
        elif choice[0] == 'update':
            s2 = set(map(int, input().split()))
            s.update(s2)
        elif choice[0] == 'symmetric_difference_update':
            s3 = set(map(int, input().split()))
            s.symmetric_difference_update(s3)
        elif choice[0] == 'difference_update':
            s4 = set(map(int, input().split()))
            s.difference_update(s4)
        n1 = n1 - 1
        
print(sum(s))
          
    