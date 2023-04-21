x=int(input("Vvedit czyslo: "))
for i in range(1,x//2+1):
  if not x%i:
    print(i, end=" ")
print(x)
