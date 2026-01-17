N=int(input())
A=int(input())
t=N*A
if(N==0 or A==0):print("No teaching")
elif(t//60!=0 and t%60==0):print(f"{t//60} hours")
elif(t//60==0 and t%60!=0):print(f"{t%60} minute")
else:print(f"{t//60} hours {t%60} minute")