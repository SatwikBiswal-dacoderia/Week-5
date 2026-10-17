a=set()
n1=int(input("Enter the number of elements of the first set : "))
print("For the first set : ")
for i in range(0,n1):
    el=int(input("Enter the elements of the set : "))
    a.add(el)
print("Set 1 : ",a)
b=set()
n2=int(input("Enter the number of elements of the second set : "))
print("For the second set : ")
for i in range(0,n2):
    el=int(input("Enter the elements of the set : "))
    b.add(el)
print("Set 2 : ",b)
c=(a|b)
print(a," U ",b," = ",c)

    