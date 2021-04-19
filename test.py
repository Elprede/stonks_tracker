TABLES = {}

TABLES['T_stocks'] = (
    "CREATE TABLE `T_stocks` ("
    "   `id` int(11) NOT NULL,"
    "   `ticker_name` varchar(4) NOT NULL"
    "   PRIMARY KEY (`id`)"
    ")"
)


print(TABLES)