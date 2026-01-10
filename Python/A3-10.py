N,K,T=input().split(" ")
N=int(N)
K=int(K)
T=int(T)
P=1
cnt=0
while True:
    cnt+=1
    P+=K
    P=P%N
    if(P==T):
        cnt+=1
        print(cnt)
        break
    if(P==1):
        print(cnt)
        break