L=[]
n=int(input("Enter the number of elements : "))
for i in range(0,n):
    el=int(input("Enter the elements : "))
    L.append(el)
x=set(L)
L_final=list(x)
print("The final list (excluding all duplicate values) : ",L_final)
