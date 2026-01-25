from decimal import Decimal, ROUND_HALF_UP
def round_half_up(n, decimals=0):
    multiplier = Decimal('10') ** -decimals
    return Decimal(str(n)).quantize(multiplier, rounding=ROUND_HALF_UP)
row=int(input())
spr=int(input())
for i in range(int(round_half_up(row/2,0))):
    for j in range(spr):
        print("A",end=" ")
    print()
for i in range(int(row - round_half_up(row/2,0))):
    for j in range(spr):
        print("K",end=" ")
    print()