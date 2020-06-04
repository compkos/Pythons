
# Μάθημα 19: Regular Expressions
# 19.2 Παράδειγμα: Ψάχνουμε παραμύθια
import re
import numpy as np
tonoi = ('αά', 'εέ', 'ηή', 'ιί', 'οό', 'ύυ', 'ωώ')
tw = 'Trivizas_works.txt'
try:
    with open(tw, 'r', encoding = 'utf-8') as f:
        works = f.read()
    for line in works.split('\n'):
        print(line)
except IOError as e:
    print(e)
while True:
    phrase = input('Δώσε λέξη-κλειδί:')
    if phrase == '': break
    n_phrase = ''
    for c in phrase:
        char = c
        for t in tonoi:
            if c in t: char = '['+t+']'
        n_phrase += char
    print(n_phrase)
    pattern = '.*'+n_phrase+'.*'
    w =re.findall(pattern, works, re.I)
    for work in w:
        print(work)


# 19.3 Παράδειγμα: Αναζήτηση σε html
'''
Να βρείτε αν υπάρχει email στη σελίδα.
Να βρείτε το περιεχόμενο της ετικέτας <title>.
Να βρείτε το περιεχόμενο των ετικετών <h2> της σελίδας αυτής.
'''

with open('upatras.html', 'r', encoding = 'utf-8') as f:
    html = f.read()

#print(html)

email_pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'

print('Αναζήτηση email στην ιστοσελίδα')
found = re.findall(email_pattern, html, re.I)
found = list(set(found))
for f in found :print('\t\t', f)

while True:
    tag = input('Δώσε ετικέτα:')
    if tag == '': break
    tag_pattern = r'<'+tag+r'\b[^>]*>(.*?)</'+tag+r'>'
    found = re.findall(tag_pattern, html, re.I)
    found = list(set(found))
    for f in found :print('\t\t', f)
