# Μάθημα 17.2: Αρχεία

with open('vouna.txt', 'r', encoding = 'utf-8') as f :
    vouna = []
    for vouno in f:
        vouno = vouno.split('\t')
        name = vouno[0]
        height = vouno[1]
        vouna.append((name,height))
for v in vouna:
    print(v)

max_height = 0
for v in vouna:
    if int(v[1]) > max_height: max_height = int(v[1])
print('Το ψηλότερο βουνό έχει ύψος', max_height)

with open('vouna2.txt', 'w', encoding='utf-8') as f:
    for v in vouna:
        to_file = 'Το όρος {} έχει ύψος {} μέτρα. '.format(v[0],v[1])
        v_height = int(v[1])
        if v_height == max_height:
            to_file += "Είναι το ψηλότερο ελληνικό βουνό."
        else :
            diff = max_height - v_height
            to_file += "Είναι {} μ. χαμηλότερο.".format(diff)
        f.write(to_file)

import calendar
while True:
    year = input("Έτος(enter για έξοδο) :")
    if year == '':
        break
    try:
        year = int(year)
    except ValueError:
        continue
    my_year = calendar.calendar(year)
    my_year = my_year.replace("Mo Tu We Th Fr Sa Su", "Δε Τρ Τε Πε Πα Σα Κυ")
    en_gr = {}
    filename = str(year)+'.txt'
    with open(filename, "w", encoding="utf-8") as newfile:
        with open("months.csv", "r", encoding="utf-8") as months_file:
            for line in months_file:
                new_line = line.strip()
                new_line = new_line.split(",")
                en_m = new_line[0]
                gr_m = new_line[1]
                en_gr [en_m] = gr_m
                my_year = my_year.replace(en_m, gr_m)
    my_year.replace(str(year), "Hμερολόγιο του "+ str(year))
    print(my_year)
    with open(str(year)+".txt", "w", encoding="utf-8") as f:
        f.write(my_year)