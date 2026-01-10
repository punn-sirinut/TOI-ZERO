import itertools
N=int(input())
list_1=[]
for i in range(N):
    list_1.append(input().strip())
all_permutations=list(itertools.permutations(list_1))
for j in range(len(all_permutations)):
    for k in range(len(all_permutations[j])):print(all_permutations[j][k],end=" ")
    print()
print(len(all_permutations))