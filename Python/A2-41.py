N=int(input())
print(bin(N).replace("0b",""))
print(oct(N).replace("0o",""))
print(hex(N).replace("0x","").upper())