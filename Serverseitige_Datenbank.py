import pyodbc
server = 'tcp:data-matching.database.windows.net'
database = 'db_data'
username = 'markimenth'
password = 'pDwOK22bhKWAeOnKV24c'
driver = '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()