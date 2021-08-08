n = int(input("Enter the number "))
sp = n-1
st = 1
for i in range(n):
    for j in range(sp):
         print(" ",end = " ")
    for k in range(st):
         print("* ", end ="")
    print()
    sp-=1
    st+=2
r=n
sp=0
st=2*n-1
for b in range(r):
     for l in range(sp):
         print(" ", end=" ")
     for m in range(st):
         print("*",end=" ")
     sp+=1
     st-=2
     print()
    
