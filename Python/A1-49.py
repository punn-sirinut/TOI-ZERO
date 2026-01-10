N=input().strip()
if len(N)!=5:
    exit()
N=str(N)
n_1,n_2,n_3,n_4,n_5=N[0],N[1],N[2],N[3],N[4]
list_1=[]
if(int(n_1)>5):list_1.append(9)
elif(int(n_2)>5):list_1.append(10)
elif(int(n_3)>5):list_1.append(11)
elif(int(n_4)>5):list_1.append(12)
elif(int(n_5)>5):list_1.append(14)
else:list_1.append(13)
if(n_1==n_5 and n_2==n_4):
    if(int(n_1)+int(n_5)>5):list_1.append(1)
    elif(int(n_2)*int(n_4)>5):list_1.append(2)
    else:list_1.append(0)
else:
    if(int(n_5)!=0 and int(n_1)//int(n_5)>5):list_1.append(1)
    elif(int(n_2)-int(n_5)>5):list_1.append(2)
    else:list_1.append(0)
if(int(n_1)+int(n_2)+int(n_3)+int(n_4)+int(n_5)>25):list_1.append(1)
elif(int(n_1)*int(n_2)*int(n_3)*int(n_4)*int(n_5)>55):list_1.append(2)
else:list_1.append(0)
o=str(list_1[0])+str(list_1[1])+str(list_1[2])
print(int(o))