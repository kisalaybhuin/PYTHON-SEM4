def reverse_number(num):
    return int(str(num)[::-1])

a = int(input("Enter a number: "))
r= reverse_number(a)
print("The reversed number is :", r)
