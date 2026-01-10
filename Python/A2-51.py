N,M=input().split(" ")
N=int(N)
M=int(M)
if(N<1 or N>10 or M<1 or M>20):
    print("Data Incorrect")
    exit()
s=[]
for i in range(N):
    x=list(map(int,input().split(" ")))
    s.append(x)
for j in range(N):
    print(f"Team {j+1}: Average = {sum(s[j])/M:.2f}, Max = {max(s[j])}")
print(f"Total Score of All Teams = {sum([sum(s[k]) for k in range(N)])}")