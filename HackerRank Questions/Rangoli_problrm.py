def print_rangoli(size):
    # your code goes here
    s=""
    for i in range(size):
        s+=chr(97+i)
    s= s[::-1]

    for j in range(0,n):
        print('-'.join((s[0:(j+1)]+ s[0:j][::-1]).center(2*n-1, '-')))

    for k in range((n-1),0,-1):
        print('-'.join((s[0:(k-1)] + s[0:k][::-1]).center(2*n-1, '-')))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)