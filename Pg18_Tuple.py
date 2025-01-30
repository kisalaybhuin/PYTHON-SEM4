#Write a program which accepts a sequence of comma-separated
#numbers from console and generate a list and a tuple which
#contains every number.

n=input('Enter comma-separated numbers : ')
lst=n.split(',')
tup=tuple(lst)

print(lst)
print(tup)
