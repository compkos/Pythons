# Μάθημα 7: Δομή επιλογής  if

# Παραδειγμα 1
v = float(input("Βαθμός πτυχίου: "))
if v >= 5 and v <= 10:
    print("πέρασες")
    print("συγχαρητήρια!!")
elif v >= 0 and v < 5:
    print("κόπηκες")
    print("ξαναπροσπάθησε!!!")
else:
    print("έχει γίνει κάποιο λάθος ο βαθμός μεταξύ 0 και 10")

# Παραδειγμα 2
v = input("βαθμός :")
v = float(v)
if v >= 5 and v <= 10:
    print("πέρασες")
    print("συγχαρητήρια!!")
elif v < 5 and v >= 0:
    print("κόπηκες")
    print("ξαναπροσπάθησε!!!")
else:
    print("έχει γίνει κάποιο λάθος ο βαθμός μεταξύ 0 και 10")

# Παραδειγμα 3
name = input('Όνομα: ')
if name[0] == "Ν":
    print("Καλωσήρθες")


for i in [8,3,12]:
	print(i,end='_')

for i in ['μήλα', 'αχλάδια', 'πορτοκάλια']:
	if i[0] > 'ν': break
	print(i, end=' ')
else:
	print('τα φρούτα κάνουν καλό')

for item in sorted('σε γνωρίζω από την όψη'.split()):
	print(item[0], end=' ')

for i in sorted([12, 2, 3, 8, 7]):
	if i%3 == 0 : continue
	elif i%8 == 0 : break
	else: print(i, end=' ')
else:
	print('end of list')

d = {1: 'h', 2: 'e', 3: 'l', 4: 'l', 5: 'o'}
for i in sorted(d, key =d.get):
	print(d[i],end='')
else: print('world')


a = 5
if a < 3 or a > 6 : print('1')
else: print('2')

a=4
if a==0 or 3:
    print (a)
else:
    print (a+1)


n1 = 'Nikos'
n2 = 'Nikitas'
if n1 == n2 : print('1')
elif n1[:3] == n2[:3]: print('2')
elif n1[0] == n2[0]: print('3')
else : print('4')

a = 'a'
z = 'z'
if ord(a) == ord(z) : print ('1')
elif (ord(z) - ord(a)) <= 15 : print('2')
elif (ord(z) - ord(a)) <= 30 : print('3')
else: print('4')
