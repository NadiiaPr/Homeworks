n=int(input("Vvedit czyslo: "))
s=0
l=[]
while n:
  r=n%10
  n=n//10
  l.append (str (r)+"*10^"+str(s))
  s+=1
print("+".join(l[::-1]))
