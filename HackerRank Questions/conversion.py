x = 17
print(oct(17).split("o")[1])
print(hex(17).split('x')[1])
print(bin(17).split('b')[1])

def print_formatted(number):
    # your code goes here
    w = len(str(bin(number).split('b')[1]))
    for i in range(1, number+1):
        print(
            str(i).rjust(w, ' '), 
            str(oct(i).split('o')[1].upper()).rjust(w, ' '), 
            str(hex(i).split('x')[1].upper()).rjust(w, ' '), 
            str(bin(i).split('b')[1]).rjust(w, ' ')
            )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)