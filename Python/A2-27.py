num=int(input())
list=[]
for i in range(num):
    list.append(int(input()))
list.sort()
print(list[-1])
print(list.count(list[-1]))