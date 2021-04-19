import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='stockdb.cft6ypwybty9.ap-southeast-2.rds.amazonaws.com',
                                         database='T_stocktracker',
                                         user='admin',
                                         password='Pelangi$1103')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

TABLES = {}

TABLES['T_stocks'] = (
    "CREATE TABLE `T_stocks` ("
    "   `id` int(11) NOT NULL,"
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


if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")