#Write a Python Program to create a function which accepts 3
#arguments. (2 numbers and one arithmetic operator). Display
#answer accordingly

def arith(n1,n2,op):
    if op=="+":
        return n1+n2
    if op=="-":
        return n1-n2
    if op=="*":
        return n1*n2
    if op=="/":
        return n1/n2

num1=int(input('Enter 1st number : '))
num2=int(input('Enter 2nd number : '))
operator= input('Input Operator : ')

print(arith(num1,num2,operator))
