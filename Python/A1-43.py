base=int(input())
bonus=int(input())
days=int(input())
if(days>3):score=(base+bonus)*1.5
else:score=base+bonus
print(int(score))
if(score>=1500):code=5
elif(score>=1000):code=4
elif(score>=500):code=3
elif(score>=200):code=2
else:code=1
print(code)
if(code==5 and days>=7):print(99)
elif(code==4 and bonus>300):print(88)
else:print(0)