a=20528
b=190784
c=210310
d=abs(a-c)
print(d)
e=abs(a-b)
print(e)
print(d<=e)
Xs = (True, False)
Ys = (True, False)
for X in Xs:
 for Y in Ys:
  Z=(X and not Y) or (Y and not X)
  W= X!=Y
  print(Z==W)
