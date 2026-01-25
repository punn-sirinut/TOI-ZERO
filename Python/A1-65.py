x=input().split(" ")
list_1=[]
if len(x)!=5:
    exit(0)
for i in range(5):
    if len(str(x[i]))==4 and int(x[i][-1])!=0 and int(x[i][-2])!=0 and int(x[i][-3])!=0 and int(x[i][-4])!=0:
        list_1.append("#/+*")
    elif len(str(x[i]))==4 and int(x[i][-1])==0 and int(x[i][-2])!=0 and int(x[i][-3])!=0 and int(x[i][-4])!=0:
        list_1.append("#/+")
    elif len(str(x[i]))==4 and int(x[i][-1])==0 and int(x[i][-2])==0 and int(x[i][-3])!=0 and int(x[i][-4])!=0:
        list_1.append("#/")
    elif len(str(x[i]))==4 and int(x[i][-1])==0 and int(x[i][-2])==0 and int(x[i][-3])==0 and int(x[i][-4])!=0:
        list_1.append("#")
    elif len(str(x[i]))==3 and int(x[i][-1])!=0 and int(x[i][-2])!=0 and int(x[i][-3])!=0:
        list_1.append("/+*")
    elif len(str(x[i]))==3 and int(x[i][-1])==0 and int(x[i][-2])!=0 and int(x[i][-3])!=0:
        list_1.append("/+")
    elif len(str(x[i]))==3 and int(x[i][-1])==0 and int(x[i][-2])==0 and int(x[i][-3])!=0:
        list_1.append("/")
    elif len(str(x[i]))==2 and int(x[i][-1])!=0 and int(x[i][-2])!=0:
        list_1.append("+*")
    elif len(str(x[i]))==2 and int(x[i][-1])==0 and int(x[i][-2])!=0:
        list_1.append("+")
    elif len(str(x[i]))==1 and int(x[i][-1])!=0:
        list_1.append("*")
    elif len(str(x[i]))==1 and int(x[i][-1])==0:
        list_1.append("-")
for i in range(5):
    print(list_1[i],end="")