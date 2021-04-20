import mysql.connector
from mysql.connector import errorcode


def init_mysql_connection():
    try:
        connection = mysql.connector.connect(host='stockdb.cft6ypwybty9.ap-southeast-2.rds.amazonaws.com',
                                            database='T_stocktracker',
                                            user='admin',
                                            password='Pelangi$1103',
                                            autocommit=True)

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    return (db_Info, cursor)

def close_mysql_connection():
    if connection.is_connected():
        cursor.close()
    connection.close()
    print("MySQL connection is closed")


def create_table():
    ## CREATING TABLES ##

    TABLES = {}

    TABLES['T_stocks'] = (
        "CREATE TABLE `T_stocks` ("
        "   `id` int(11) NOT NULL AUTO_INCREMENT,"
        "   `hotcopper_tagid` int(11) NOT NULL,"
        "   `ticker_name` varchar(4) NOT NULL,"
        "   PRIMARY KEY (`id`)"
        ")"
    )

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

def drop_tables():
    # TABLES['T_stocks'] = (
    #     "DROP TABLE `T_stocks` "
    # )

    # for table_name in TABLES:
    #     table_description = TABLES[table_name]
    #     try:
    #         print("Creating table {}: ".format(table_name), end='')
    #         cursor.execute(table_description)
    #     except mysql.connector.Error as err:
    #         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
    #             print("already exists.")
    #         else:
    #             print(err.msg)
    #     else:
    #         print("OK")



# ## INSERT STUFF TO TABLES ##

# add_hotcopper_ticker = ("INSERT INTO T_stocks "
#                "(hotcopper_tagid, ticker_name) "
#                "VALUES (%s, %s)")

# data_hotcopper_ticker = [999, 'ASX']

# try:
#     print("INSERTING hotcopper ticker into T_stocks")
#     cursor.execute(add_hotcopper_ticker, data_hotcopper_ticker)

# except mysql.connector.Error as err:
#     print(err.msg)
# else:
#     print("SUCCESSFULLY ADDED")


query = ("SELECT * FROM T_stocks")
cursor.execute(query)
result = cursor.fetchall()

for x in result:
    print(x)

## CLOSE CONNECTION ##

