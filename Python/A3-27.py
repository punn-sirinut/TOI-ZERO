import copy
r,c=input().split(" ")
r,c=int(r),int(c)
list_1=[]
for i in range(r):
    s=input().split(" ")
    list_1.append(s)
list_2=copy.deepcopy(list_1)
for j in range(r-1):
    for k in range(c):
        if(list_1[j][k]=="*"):
            del list_2[j+1][k]
            list_2[j+1].insert(k,"*")
for l in range(r):
    for m in range(c):
        print(list_2[l][m],end=" ")
    print()