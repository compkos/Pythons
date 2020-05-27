import os
import os.path
count = 0
for (r,d,f) in os.walk(os.getcwd()):
    count += 1
print("a =", count)
while True:
    dir =input('Αρχικός φάκελος:')
    if dir == '': break
    if os.path.isdir(dir):
        count_files = 0
        for r,d,f in os.walk(dir):
            level = r.replace(dir, '').count(os.sep)
            print(level*'\t',r)
            for fi in f:
                if fi[0] not in '.~':
                    print((level+1)*'\t',fi)
                    count_files += 1
    print('βρέθηκαν {} αρχεία'.format(count_files))  
while True:
    dir =input('Αρχικός φάκελος:')
    if dir == '': break
    if os.path.isdir(dir):
        file_types= {}
        file_size= {}
        for r,d,f in os.walk(dir):
            for fi in f:
                if fi[0] not in '.~':
                    # τύπος αρχείου
                    f_parts = fi.split('.')
                    if len(f_parts) > 1:
                        f_type = f_parts[-1]
                        file_types[f_type] = file_types.get(f_type, 0) +1
                        # μέγεθος αρχείου
                        full_f_name = os.path.join(r,fi)
                        size = os.path.getsize(full_f_name)
                        file_size[f_type] = file_size.get(f_type, 0) + size
        for t in file_types:
            print(t,'\t\t', file_types[t])
        print(50*'*')
        total_size = sum(file_size.values())
        print("Συνολικό μέγεθος:", total_size)
        for t in file_size:
            percent = 100*file_size[t]/total_size
            print('{}\t\t{}\t\t{:5.2f}%'.format(t, file_size[t], percent))
