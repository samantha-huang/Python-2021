import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ') #enter file name
if (len(fname) < 1): fname = 'mbox-short.txt' #if the length of the name is less than 1, default the file name to 'mbox-short.txt'
fh = open(fname) #open the file 
for line in fh: #loop through the lines in the file
    if not line.startswith('From: '): continue #only get the from lines
    pieces = line.split() #split the line
    email = pieces[1].split('@') #retrieve the email address
    org = email[1]
    #print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()