import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# create table
c.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')

# insert a row of data
c.execute('INSERT INTO stocks VALUES (\'2006-01-05\', \'BUY\', \'RHAT\', 100, 35.14)')

# save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been commited or they will be lost.
conn.close()
