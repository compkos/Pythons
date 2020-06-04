
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

# Μάθημα 19: Regular Expressions
# 19.4 Παράδειγμα: Τα ελληνικά βουνά, έκδοση 2
'''
Στο παράδειγμα της ενότητας 17 (αρχεία), είχαμε επεξεργαστεί το
αρχείο vouna.txt χρησιμοποιώντας μεθόδους συμβολοσειρών.
Να επεκτείνετε την άσκηση ώστε να περιλάβετε τη γεωγραφική περιοχή
κάθε βουνού, χρησιμοποιώντας regular expressions.
'''
with open('vouna.txt', 'r', encoding = 'utf-8') as f :
    vouna = []
    for vouno in f:
        vouno = vouno.split('\t')
        name = vouno[0]
        height = vouno[1]
        region = vouno[2]
        vouna.append((name,height, region))
for v in vouna:
    print(v)

max_height = 0
for v in vouna:
    if int(v[1]) > max_height: max_height = int(v[1])
print('Το ψηλότερο βουνό έχει ύψος', max_height)
to_file = ''
with open('vouna2.txt', 'w', encoding='utf-8') as f:
    for v in vouna:
        #region = re.sub(r'\([^)]*\)', '', v[2]).split(',')
        region = re.sub(r" ?\([^)]+\)", '', v[2]).split(',')
        print(region)
        to_file += 'Το όρος {} έχει ύψος {} μέτρα. '.format(v[0],v[1])
        v_height = int(v[1])
        if v_height == max_height:
            to_file += "Είναι το ψηλότερο ελληνικό βουνό,"
        else :
            diff = max_height - v_height
            to_file += "Είναι {} μ. χαμηλότερο,".format(diff)
        ## Προσθήκη αναφοράς στην περιοχή
        to_file += " και βρίσκεται στη "
        for r in region:
            r_name = r.rstrip()
            if r_name[-1] == 'ς' : r_name = r_name[:-1]
            if region.index(r) == 0 : kai = ' '+r_name
            else: kai = ' και στη '+ r_name
            to_file += kai
        to_file += '.'
    print(to_file)
    f.write(to_file)
