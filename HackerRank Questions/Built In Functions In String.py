"""
s = input()

print("True") if s.isalnum() else print("False")
print("True") if s.isalpha() else print("False")
print("True") if s.isdigit() else print("False")
print("True") if s.isupper() else print("False")
print("True") if s.islower() else print("False")


print(s.isalpha())
print(s.isalnum())
print(s.isdigit())
print(s.islower())
print(s.isupper())

#s = 'a'

#print(s.isupper())
#print 'abcD'.isalpha()
txt = "565543"

x = txt.isnumeric()

print(x)

"""
s = input()
print("True" if any(x.isalnum() for x in s) else "False")
print("True" if any(x.isalpha() for x in s) else "False")
print("True" if any(x.isdigit() for x in s) else "False")
print("True" if any(x.islower() for x in s) else "False")
print("True" if any(x.isupper() for x in s) else "False")
