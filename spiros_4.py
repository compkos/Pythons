gr=['Α','Β','Γ','Δ','Ε']
a=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
for i in range(0,5):
  k=i
  for j in range(0,5):
    a[i][j]=gr[k]
    if k<4:
      k=k+1
    else:
      k=0  
print(a)
print()

import numpy as np
b = np.empty((5, 5),dtype='U10')
for i in range(0,5):
  k=i
  for j in range(0,5):
    b[i][j]=gr[k]
    if k<4:
      k=k+1
    else:
      k=0  
print(b)


c = np.empty((14, 10),dtype='U10')
theseis=140
for i in range(0,14):
  for j in range(0,10):
    c[i][j]='Ε'
seira = int(input("Δώσε σειρά :"))
thesi = int(input("Δώσε θέση : "))
while seira !=-1 and theseis!=0:
  if c[seira,thesi]=='Ε':
    c[seira,thesi]='Κ'
    theseis=theseis-1
  else:
    print(f'Η θέση {seira},{thesi} δεν είναι ελεύθερη')
  seira = int(input("Δώσε σειρά :"))
  thesi = int(input("Δώσε θέση : "))

print(c)
eisitiria=140-theseis
print(f'Το πλήθος των εισιτηρίων που δόθηκαν είναι : {eisitiria}')

d = np.empty((14, 2), dtype="int")
for i in range(0,14):
  kenes=0
  for j in range(0,10):
    if c[i,j]=='Ε':
      kenes=kenes+1
  d[i][0]=i
  d[i][1]=kenes
print(d)

n = 14
for i in range(n-1): 
  for j in range(0, n-i-1): 
    if d[j][1] < d[j+1][1] : 
      d[j][1], d[j+1][1] = d[j+1][1], d[j][1]
      d[j][0], d[j+1][0] = d[j+1][0], d[j][0]

print(d)



