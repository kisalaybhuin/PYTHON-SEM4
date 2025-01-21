# Write a program to print factorial number using function

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

a=int(input("Enter Number:"))
print(f"Factorial of {a} is {factorial(a)}")
