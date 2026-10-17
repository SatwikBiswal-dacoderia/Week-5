a=set()
n=int(input("Enter the number of elements : "))
for i in range(0,n):
    el=int(input("Enter the elements : "))
    a.add(el)
l=len(a)
u=n-l
print("No of duplicates = ",u)