import mysql.connector
from mysql.connector import Error

def connect_insert():
    ''' function to connect and insert a row in a database  '''

    #create a connection variable
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost', database='movie_base', user='wizardcalidad', password='Olatunde8!', auth_plugin='mysql_native_password')
        print('Connecting to database')
        if conn.is_connected:
            print('Connected to the database')
            db_cursor = conn.cursor()

            #create a variable to contain the sql query to be excecuted
            sql = "INSERT INTO Movie_Description (MovieTitle, ActorFirstName, ActorLastName, MovieTime, MovieYear) VALUES (%s, %s, %s, %s, %s)"
           
           #create a list variable to contain all the values we want to insert into the database
            val = [
                    ('Witches of East End', 'Ayemobola', 'SatGuruMaTolu', 1700, 2003),
                    ('Witches of East End', 'Ovuefe', 'MongoDB', 1700, 2003),
                    ('Witches of East End', 'Victor', 'StubbornChild', 1700 ,2003),
                    ('Witches of East End', 'Ample', 'BabaJoshua', 1700, 2003),
                    ('Witches of East End', 'Pastor', 'SeniorBlessing', 1700, 2003)
                ]

            #execute the query using the executemany function    
            db_cursor.executemany(sql, val)

            #commit to the database
            conn.commit()

            #print a success message
            print(db_cursor.rowcount, "rows was inserted.")
            
            #close the cursor
            db_cursor.close
            
    except Error as e:
        print('Connection failed due to the following :', e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
            print('Disconnected from database')

#call the function we just created
connect_insert()

