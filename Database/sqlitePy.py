import sqlite3

dbconn = sqlite3.connect('./testdb.db')
cursor = dbconn.cursor()

try:
	cursor.execute("CREATE TABLE if not exists user(id INTEGER, name text, phone text, sex text)")
	cursor.execute("INSERT INTO user VALUES (1,'Kim','01045867847', 'M')")
	cursor.execute("INSERT INTO user VALUES (2,'Lee','01035532618', 'F')")
	cursor.executemany("INSERT INTO user VALUES(?,?,?,?)",\
		[(3,'Park','01032232332','M'),(4,'Choi','01043532297','F'),(5,'Hong','01023416757','M')])

	dbconn.commit()
except KeyboardInterrupt:
	dbconn.close()
