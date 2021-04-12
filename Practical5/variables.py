a=280502
b=190784
c=100321
d=abs(a-c)
print(d)
e=abs(a-b)
print(e)
if d<=e:
    print('d is not greater than e')
else:
    print('d is greater than e')
Xs = (True, False)
Ys = (True, False)
for X in Xs:
 for Y in Ys:
  Z=(X and not Y) or (Y and not X)
  W= X!=Y
  print(Z==W)
