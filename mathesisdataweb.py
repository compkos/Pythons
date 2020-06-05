# Μάθημα 20. Ανάκτηση δεδομένων από το διαδίκτυο

import urllib.request
import urllib.error
import socket 
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context
# timeout : χρόνος αναμονής σε δευτερόλεπτα
timeout = 10
socket.setdefaulttimeout(timeout) 
# Η κλήση στο urllib.request.urlopen χρησιμοποιεί το timeout
# που ορίστηκε στη βιβλιοθήκη socket
 
req = urllib.request.Request('https://www.upatras.gr/el')
try: 
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
    with open("www_upatras_gr.html", "w", encoding = char_set) as p:
        p.write(html)
except urllib.error.HTTPError as e:
    print('Σφάλμα HTTP:', e.code)
except urllib.error.URLError as e:
    print('Αποτυχία σύνδεσης στον server')
    print('Αιτία: ', e)
else:
    print('Φορτώθηκε επιτυχώς η σελίδα')
# καλή πρακτική: ορισμός User Agent


my_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
url = 'https://www.google.gr/#q=python&*'
try:
    headers = {}
    headers['User-Agent'] = my_UA
    req = urllib.request.Request(url, headers = headers)
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
    with open("www_google_com_q_python.html", "w", encoding = char_set) as p:
        p.write(html)
except urllib.error.HTTPError as e:
    print('Σφάλμα HTTP:', e.code)
except urllib.error.URLError as e:
        print('Αποτυχία σύνδεσης στον server')
        print('Αιτία: ', e.reason)
else:
    print('τέλος προγράμματος')

# Άσκηση 20.1 Ανάκτηση μαθημάτων από ιστοσελίδα eudoxus.gr
url_dept = 'https://service.eudoxus.gr/public/departments/courses/3008/2016'

try:
    req = urllib.request.Request(url_dept)
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
except urllib.error.HTTPError as e:
    print('Σφάλμα HTTP:', e.code)
except urllib.error.URLError as e:
        print('Αποτυχία σύνδεσης στον server')
        print('Αιτία: ', e.reason)
else:
    h2_tags = re.findall(r"<h2\b[^>]*>(.*?)</h2>", html)
    count = 0
    for tag in h2_tags:
        code = re.findall(r"\[(.*?)\]", tag)
        if len(code)> 0 :
            code = code[0].strip()
            name = re.findall(r']:(.*)', tag)
            if len(name) > 0 : name = name[0].strip()
            else: name = ''
            print(code, name)
            count += 1
    print('Ανακτήθηκαν {} μαθήματα'.format(count))