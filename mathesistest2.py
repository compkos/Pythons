a=3
if a==0 or 1:
    print (a)
else:
    print (a+1)

print('')

b=1
a = 2
while a >= 0:
    a = a - 1
    b = b + a
print (b)


for i in [2, 1]:
    for j in [1, 3]:
        if i + j > 3: break
        print (i + j, end = ' ')
    print (i - 1, end = ' ')
print (i - 1, end = ' ')

print('')



x=5
while x > 0:
    x=x+1
    if x < 7: continue
    if x > 9: break
    print (x, end = ' ')

print('')

for u in range(5):
        if u%3==1: pass
        else: print (u//2, end = ' ')

print('')

c=[x for x in range(10) if x%3 == 1]
print(c)

print('')

print([x for x in range(15) if x % 7 > 4 ])

print('')
for i in range(10, 2, -2):
	print(i+1, end = ' ')
	if i == 9 : break

d = {1:'γ', 2:'ε', 3:'ι', 4:'α'}
for i in sorted(d, key =d.get):
	print(d[i],end='')
else: print(' σας')