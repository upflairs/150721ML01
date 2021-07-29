import sqlite3
#db = sqlite3.connect(r'd:/mydb.sqlite')
db = sqlite3.connect('mydb.sqlite')

db.execute('create table if not exists Students (id int, name varchar(20), email varchar(100), mobile varchar(12))')


##db.execute('insert into Students (id, name, email, mobile) values (2,"rahul","rahul@gmail.com","8888777666"),\
##(3,"anjali","anjali@gmail.com","8888777666")')
##db.commit()

##db.execute('update Students set email="anajli@yahoo.com" where id=3')
##db.commit()

db.execute('delete from Students where mobile="8888777666"')
db.commit()

r = db.execute('select * from Students').fetchall()
print(r)

print(db.execute('select name from Students').fetchall())



db.close()
