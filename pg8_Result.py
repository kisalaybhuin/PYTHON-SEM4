a=int(input("Marks in PP:"))
b=int(input("Marks in C:"))
c=int(input("Marks in DBMS:"))
d=int(input("Marks in FSISI:"))
e=int(input("Marks in LS:"))
t=a+b+c+d+e
print("....................")
print("Total : ", t)
p=(t*100)/500
print("Percentage : ",p)
if p>=90:
    print("Grade : S")
elif p<89 and p>=80:
    print("Grade : A")
elif p<79 and p>=70:
    print("Grade : B")
elif p<69 and p>=60:
    print("Grade : C")
elif p<59 and p>=50:
    print("Grade : D")
elif p<49 and p>=33:
    print("Grade : E")
else:
    print("Grade : F")
if p>=33 and a>33 and b>33 and c>33 and d>33 and e>33:
    print("Result : PASS")
else:
    print("Result : FAIL")
