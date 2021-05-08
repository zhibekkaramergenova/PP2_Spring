import psycopg2
con= psycopg2.connect("dbname=postgres user=postgres password=Karzhimerbek2002")
cur= con.cursor()
# cur.execute(""" 
# CREATE TABLE person(
# name varchar(255),
# surname varchar(255),
# id integer,
# student_points integer,
# joined_date date);

# """)

# cur.execute(""" 
# INSERT INTO person(name, surname, id, student_points, joined_date) VALUES('Zhibek','Kar', '2153','34','21.05.08')

# """)
# cur.execute(""" 
# INSERT INTO person(name, surname, id, student_points, joined_date) VALUES('Alish','Mad', '2145','120','21.05.08')

# """)
# cur.execute(""" 
# INSERT INTO person(name, surname, id, student_points, joined_date) VALUES('Baiko','Lesbek', '2155','160','21.05.08')

# """)

# cur.execute("""
# UPDATE person
#     SET student_points='200',
#     joined_date='21.05.09'
#     WHERE name='Zhibek';


# """)

cur.execute("""
DELETE FROM person
WHERE id='2155';
""")
cur.execute("""
SELECT*FROM person
""")
row = cur.fetchone()
while row is not None:
    print(row)
    row = cur.fetchone()


cur.close()
con.commit()
con.close()


