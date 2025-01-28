#Write a program to print armstrong of user input number using UDF

def armstrong(n):
    og=n
    rev=0
    temp=0
    while(n!=0):
        temp=n%10
        rev=rev+(temp**3)
        n//=10

    if (rev==og):
        print('It is armstrong')
    else:
        print('It is not armstrong')
    return rev

n=int(input('Enter a number : '))
a=armstrong(n)
