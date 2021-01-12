ONKAT=[]
CODES=[]
TIMH=[]
Order=[]

i=0
while i < 3:
  x=int(input("Δώσε αριθμό  καταστήματος :"))
  y=1
  stocks=[]
  while y!=0:
    y=int(input("Δώσε αριθμό είδους (0 έξοδο) :"))
    if int(y)>0 :
      stocks.append(y)

  Order.append([x,stocks])
  i += 1
print(Order)
print(Order[0][1])

c=int(input("Δώσε τιμή"))
print(Order[0][1].index(c))


for i in range(5):
  x=input("Δώσε όνομα " + str(i+1) + " ου καταστήματος :")
  ONKAT.append(x)

for i in range(5):
  CODES.append([])
  for j in range(2):
    x=input("Δώσε είδος " + str(i+1) + " ου καταστήματος :")
    CODES[i].append(int(x))
print(CODES)

for i in range(10):
  TIMH.append([])
  for j in range(2):
    x=input("Δώσε είδος " + str(i+1) + " ου καταστήματος :")
    TIMH[i].append(int(x))
print(TIMH)












