for i in range(10):
	if i%2 == 0: continue
	elif i%7 == 0: break
	else: print(i, end= ' ')
else:
	print('end')

print('')

for i in range(3, 12, 4):
	print(i+5, end=' ')
else:
	print('end')  


print('')
for i in range(8, 2, -2):
	print(i+1, end = ' ')
	if i == 9 : break

print('')

x=0
for i in range (0,5):
    x+=i
print (x)

x = 0
while x <= 5 : 
	print(x, end = ' ')
	x += 1