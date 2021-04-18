
import pyodbc
server = 'tcp:data-matching.database.windows.net'
database = 'db_data'
username = 'markimenth'
password = 'pDwOK22bhKWAeOnKV24c'
driver = '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

#cursor.execute("SELECT TOP 2 * FROM TEST_DATA")
#cursor.execute("SELECT * FROM SYSOBJECTS WHERE xtype = 'U'")
#cursor.execute("SELECT DB_NAME()")
#cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")

#SELECT * FROM INFORMATION_SCHEMA.TABLES

# db_list = []
# counter = 0
# for x in cursor:
#     print('x')
#     db_list.append(x)
#
#
#
# print(db_list)


def get_column_information_db():
    column_information_list = []
    cursor.execute("select "
                   "TABLE_CATALOG, "
                   "TABLE_NAME, "
                   "COLUMN_NAME, "
                   "ORDINAL_POSITION, "
                   "IS_NULLABLE, "
                   "DATA_TYPE, "
                   "CHARACTER_MAXIMUM_LENGTH, "
                   "NUMERIC_SCALE, "
                   "DATETIME_PRECISION "
                   "FROM "
                   "INFORMATION_SCHEMA.COLUMNS "
                   "WHERE "
                   "TABLE_SCHEMA = 'dbo'")
    for x in cursor:
        column_information_list.append(x)
    return column_information_list


database_metadata_column_list = get_column_information_db()


def get_database_name():
    global database_metadata_column_list

    for x in database_metadata_column_list:
        print(x[0])


get_database_name()

