# Μάθημα 12. Functions

'''Να κατασκευάσετε συνάρτηση isnum()
που δέχεται στην είσοδο μια συμβολοσειρά και
απαντάει αν είναι αποδεκτός αριθμός ή όχι.
'''

def isnum(n = ''):
    if not type(n) is str : 
        return False
    print(n)
    n = n.strip()
    if n.isdigit(): 
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".")<= 1 and isnum(n.replace(".", "")):
            return True
        else:
            return False
    else :
        return False

while True:
    n = input("n=")
    if n == '' : 
        break
    print(isnum(n))

# Μάθημα 12. Functions

'''12.3 Να κατασκευάσετε πρόγραμμα που ζητάει
διαδοχικά από τον χρήστη την ακτίνα σφαίρας
και υπολογίζει, καλώντας σχετικές συναρτήσεις
την επιφάνεια και τον όγκο της.
Τερματίζει με stop.
e = 4*pi*r**2
v = (4/3)*pi*r**3
'''
import math
pi = math.pi

def area(r):
    # συνάρτηση υπολογισμού επιφάνειας σφαίρας
    return 4*pi*r**2

def vol(r):
    # συνάρτηση υπολογισμού όγκου σφαίρας
    return (4/3)*pi*r**3
    
def isnum(n):
    # συνάρτηση που βρίσκει αν συμβολοσειρά είναι αριθμός
    if not type(n) is str :
        return False
    n = n.strip()
    if n.isdigit():
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".") == 1 and isnum(n.replace(".","")):
            return True
        else:
            return False
    else:
        return False

while True:
    r = input("R=")
    if r == 'stop' or r == '' : break
    if isnum(r):
        v = vol(float(r))
        e = area(float(r))
        print("Επιφάνεια={:1.2f}, Όγκος={:1.2f}".format(e,v))
    else:
        continue

'''12.3 Να κατασκευάσετε πρόγραμμα που καλεί συνάρτηση
που μετράει τα κεφαλαία και μικρά γράμματα σε μια φράση.
'''

def count_capital_small(s):
    count_capital = 0
    count_small = 0
    for c in s:
        if c.isalpha():
            if c.lower() == c :
                count_small += 1
            else :
                count_capital += 1
    return count_capital, count_small

st = input("φράση:")
print(count_capital_small(st))


'''12.4 Να κατασκευάσετε συνάρτηση που παίρνει στην
είσοδο μια λίστα και επιστρέφει τη λίστα με μοναδικά
στοιχεία.
'''
def list_set(li):
    # επιστρέφει τη λίστα χωρίς διπλά στοιχεία
    if not type(li) is list :
        return []
    li_new = []
    for i in li:
        if i not in li_new : li_new.append(i)
    return li_new

print(list_set([1,2,3,4,2,3,4,2,3,4]))


# Μάθημα 13: Functions
#Παράδειγμα:
# συνάρτηση που τυπώνει κείμενο με πλάτος width

def align_text(line, width):
    extra_spaces = width - len(line)
    sp = ' '
    if not sp in line : return line
    while extra_spaces > 0 :
        line = line.replace(sp, sp+' ', extra_spaces)
        extra_spaces = width - len(line)
        sp += ' '
    return line

def formatted_print(text, width=70, align = False):
    para = text.split('\n')
    to_print = ''
    for p in para:
        words = p.split()
        line = ''
        while len(words) > 0 :
            while len(words) > 0 and len(line + words[0]) < width :
                line = ' '.join([line, words.pop(0)]).strip()
            if align and len(words) > 0:
                line = align_text(line, width)
            to_print += line + '\n'
            line = ''
    return to_print

while True:
    text = input('κείμενο: ')
    if text == '': break
    width = int(input('πλάτος: '))
    print(formatted_print(text, width, True))

#test

st = '''Ούτως ωμίλησεν ο παπα-Φραγκούλης ο Σακελλάριος, αφού έκαμε την ευχαριστίαν του εξ οσπρίων και ελαιών οικογενειακού δείπνου, την εσπέραν της 23ης Δεκεμβρίου του έτους 186… Παρόντες ήσαν, πλην της παπαδιάς, των δυο αγάμων θυγατέρων και του δωδεκαετούς υιού, ο γείτονας ο Πανάγος ο μαραγκός, πεντηκοντούτης, οικογενειάρχης, αναβάς διά να είπη μίαν καλησπέραν και να πιή μίαν ρακιά, κατά το σύνηθες, εις το παπαδόσπιτο• κι η θειά το Μαλαμώ η Καναλάκαινα, μεμακρυσμένη συγγενής, ελθούσα διά να φέρη την προσφοράν της, χήρα εξηκοντούτις, ευλαβής, πρόθυμος να τρέχη εις όλας τάς λειτουργίας και να υπηρετή δωρεάν εις τους ναούς και τα εξωκκλήσια.

«Τ ακούσαμε κι ημείς, παπά» απήντησεν ο γείτονας ο Πανάγος, «έτσ είπανε».

«Τί είπανε; Είναι σίγουρο, σάς λέω» επανέλαβεν ο παπα-Φραγκούλης. «Οι βλοημένοι, δε θα βάλουν ποτέ γνώση. Επήγαν με τέτοιον καιρό να κατεβάσουν ξύλα, απάν απ” του Κουρουπή τα κατσάβραχα, στο Στοιβωτό, εκεί πού δεν μπορεί γίδι να πατήση. Καλά να τα παθαίνουν!»"
'''

print(st)
print('\n formatted text ................')
print(formatted_print(st, 50, True))
