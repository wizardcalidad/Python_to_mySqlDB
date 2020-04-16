import mysql.connector
from mysql.connector import Error

#define the connector function
def connect_fetch():
    ''' function to connect and fetch rows in a database '''

    #create a variable for the connector object
    conn = None 

    try:
        conn = mysql.connector.connect(host='localhost', database='movie_base', user='wizardcalidad', password='Olatunde8!', auth_plugin='mysql_native_password')
        print('Connecting to database server....!')
        if conn.is_connected:
            print('Connected to database server')

            #Select Query
            sql_select_query = "select * from Movie_Description"
            cursor = conn.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Total number of rows in movie_description is: ", cursor.rowcount)

            #print select output
            print("\nPrinting each Buyer record")
            for row in records:
                print("Movie Title : ", row[0])
                print("Actor FirstName: ", row[1])
                print("Actor LastName : ", row[2])
                print("Movie Time: ", row[3])
                print("Movie Year: ", row[4], '\n')


    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown')

#call the function we just created
connect_fetch()