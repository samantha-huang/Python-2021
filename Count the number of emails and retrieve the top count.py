import sqlite3 #Import sqlite3 library

conn = sqlite3.connect('emaildb.sqlite') #create a connection 
cur = conn.cursor() #cursor is a handle that open and send sql command to the cursor and receive a response.

cur.execute('DROP TABLE IF EXISTS Counts') #drop table if the table exists

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''') #run create statment to create table

fname = input('Enter file name: ') #enter file name
if (len(fname) < 1): fname = '/Users/yushanhuang/Desktop/Python Program Backup/mbox-short.txt' #if the length of the name is less than 1, default the file name to 'mbox-short.txt'
fh = open(fname) #open the file 
for line in fh: #loop through the lines in the file
    if not line.startswith('From: '): continue #only get the from lines
    pieces = line.split() #split the line
    email = pieces[1] #retrieve the email address
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) #get count from db 
    row = cur.fetchone() #fetch the first row
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'select SUBSTR(email,INSTR(email, \'@\') + 1),sum(count) as total FROM Counts group by SUBSTR(email,INSTR(email, \'@\') + 1) order by sum(count) desc limit 1'

for row in cur.execute(sqlstr): #execute the sql
    print(str(row[0]), str(row[1]))

cur.close()