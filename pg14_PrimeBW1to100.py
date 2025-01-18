# Write a program to print all prime numbers between 1 to 100.

for a in range(1, 101):
    b=0
    for i in range(2, a):
        if (a % i == 0):
            b=1
            break

    if(b==0):
            print(a)
