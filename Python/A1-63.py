seats=int(input())
while True:
    try:
        age,n=map(int,input().split())
    except EOFError:
        break
    if(age<15):
        print(-1)
        continue
    if(n>seats):
        print(-2)
        break
    price=150
    if(15<=age<=22):
        price=120
    elif(age>=60):
        price=75
    total=price*n
    seats-=n
    print(total, seats)
    if(seats == 0):break