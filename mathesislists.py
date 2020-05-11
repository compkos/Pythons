# Μάθημα 10: List comprehension

# Παράδειγμα 1
# Να βρείτε τους αριθμούς που είναι πολλαπλάσια του 2
# και πολλαπλάσια του 3 από το 1 ως το 20

# λύση με for

n = []
for i in range(1,21):
    if i%2 == 0 and i%3 == 0 :
        n.append(i)
print(n)

# λύση με list comprehension

n = [ x for x in range(1,21) if x%2 == 0 and x%3 == 0 ]
print(n)


# Παράδειγμα 2.
#Έστω λίστα L = [5,8,12,7] Να δημιουργήσετε νέα λίστα με
#στοιχεία τα μέλη της L που είναι περιττοί αριθμοί αυξημένοι κατά 10.

# λύση με for

L = [5,8,12,7]
L1 = []
for i in L :
    if i%2 == 1 :
        L1.append(i+10)
L = L1
print(L)

# λύση με list comprehension

L = [5,8,12,7]
L = [x+10 for x in L if x%2 == 1]
print(L)


# Παράδειγμα 3.
# Έστω s1 = "αβγ” και s2 = "χψω" να δημιουργή-σετε λίστα με όλους
# τους συνδυασμούς των χαρακτήρων του s1 με αυτούς του s2.  

s1 = "αβγ"
s2 = "χψω"
# λύση με for
res = []
for x in s1:
    for y in s2:
        res.append(x + y)
print(res)

#λύση με list comprehension
res = [x + y for x in s1 for y in s2]
print(res)


print([x for x in range(5) if x%2 == 0])

l = [x+3 for x in range(100) if x%50 > 47]
print(l)

l = [ x for x in range(1,31) if x%2 == 0 and x%5 == 0]
print(l)

poem='''
Σὲ γνωρίζω ἀπὸ τὴν κόψι
τοῦ σπαθιοῦ τὴν τρομερή,
σὲ γνωρίζω ἀπὸ τὴν ὄψι,
ποὺ μὲ βιὰ μετράει τὴν γῆ.
'''
l = [x[0] for x in poem.split() if x[0] == x[0].upper()]
print(l)

# Μάθημα 10: List comprehension

# Παράδειγα 1
# Να δημιουργήσετε μια λίστα με τα
# αρχικά γράμματα όλων των λέξεων της πρώτης στροφής
# του εθνικού μας ύμνου.


ymnos = '''
Σὲ γνωρίζω ἀπὸ τὴν κόψι
τοῦ σπαθιοῦ τὴν τρομερή,
σὲ γνωρίζω ἀπὸ τὴν ὄψι,
ποὺ μὲ βιὰ μετράει τὴν γῆ.
'''

first = [ (x[0], ord(x[0])) for x in ymnos.split() ]
print(first)