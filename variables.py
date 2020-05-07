x = float(input("δώσε χ = "))
y = 5 * x**3 + 4 * x**2 - 2 * x + 8
print("y = {:1.2f}".format(y))

epafes = {"Νίκος" : 111222, "Μαρία" : 333444}

# εισαγωγή νέας επαφής
print("\n Οι επαφές είναι: \n", epafes)
print ("\n Δώσε μια νέα επαφή: ")
name = input("Δώσε όνομα:")
tel = input("Δώσε αριθμό τηλεφώνου:")
epafes[name] = int(tel)
print("Οι επαφές είναι : \n", epafes)

# ταξινόμηση επαφών
epafes_list = list(epafes.items())
epafes_list.sort()
print("Η ταξινομημένη λίστα επαφών είναι:\n", epafes_list)

poem = '''
Εγώ μετράω τα ρέστα μου να βγάλω κι άλλο μήνα
ανοίγω και δε βλέπω ουρανό 
εσύ έχεις στο πιάτο σου ολόκληρη Αθήνα
ανοίγεις και χαζεύεις το κενό
'''

print(poem)

# αλφαβητική λίστα λέξεων

list_words = poem.split()
list_words.sort()
print(list_words)

# πλήθος λέξεων

print("Το πλήθος λέξεων είναι: {}".format(len(list_words)))

# πλήθος χαρακτήρων

poem = poem.replace(" ", "").replace("\n", "")
print("Το πλήθος γραμμάτων είναι: {}".format(len(poem)))

