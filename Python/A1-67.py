from decimal import Decimal, ROUND_HALF_UP
def round_half_up(n, decimals=0):
    multiplier = Decimal('10') ** -decimals
    return Decimal(str(n)).quantize(multiplier, rounding=ROUND_HALF_UP)
M=str(input())
if(M!="Y" and M!="N"):exit()
n=int(input())
total=0
for i in range(n):
    total+=float(input())
if(M=="Y"):print(round_half_up(0.95*total,2))
elif(M=="N" and total>=500):print(round_half_up(0.97*total,2))
else:print(round_half_up(total,2))