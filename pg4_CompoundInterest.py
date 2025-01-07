p=int(input("Enter Principal:"))
r=int(input("Enter Rate of interest:"))
t=int(input("Enter time in years:"))
ci = p * (1 + r / 100) ** t - p
print("Compound Interest is:",ci)



