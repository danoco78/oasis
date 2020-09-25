import pyodbc

server = 'sqlsrv-ti-dev-01.database.windows.net'
database = 'oasis-sqldb'
username = 'powerapp'
password = 'c9ede8eb-ff2e-49bc-a62a-6aa2d30ea085'
#driver= '{ODBC Driver 17 for SQL Server}'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)