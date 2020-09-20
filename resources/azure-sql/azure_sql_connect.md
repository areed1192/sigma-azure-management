# Connecting to an Azure SQL Database

## Method 1: PYODBC

```python
import pyodbc
import textwrap

# Create the Server String.
server = '{server}.database.windows.net,1433'.format(
    server="YOUR_SERVER_NAME"
)

# Set the Driver.
driver = '{ODBC Driver 17 for SQL Server}'

# Create the connection String.
connection_string = textwrap.dedent('''
        Driver={driver};
        Server={server};
        Database={database};
        Uid={username};
        Pwd={password};
        Encrypt=yes;
        TrustServerCertificate=no;
        Connection Timeout=30;
    '''.format(
        driver=driver,
        server=server,
        database="YOUR_DATABASE_NAME",
        username="YOUR_SERVER_USERNAME",
        password="YOUR_SERVER_PASSWORD"
    )
)

# Create a new connection.
cnxn = pyodbc.connect(connection_string)

# Create a cursor.
cursor = cnxn.cursor()
```
