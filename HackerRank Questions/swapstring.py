"""
def swap_case(s):
    temp = ''
    for str in s:
        if ord(str) >= 65 and ord(str) <= 91:
            temp += str.lower()
        elif ord(str)>=97 and ord(str)<=123:
            temp += str.upper()
        else:
            temp += str
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    #swap_case(s)

#print(input().upper())


#print(ord('a'))



# Spliting And Joining A String

def split_and_join(line):
    # write your code here
    temp = line.split(" ")
    return "-".join(temp)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


"""

string = "abcdefght"
print(string[6:])
#print(string[:5]+'h'+string[6:])


def mutate_string(string, position, character):
    temp = string[:position] + character + string[position+1:]
    return temp

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)