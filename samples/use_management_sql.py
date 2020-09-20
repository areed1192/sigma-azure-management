from pprint import pprint
from configparser import ConfigParser

from azure.mgmt.sql import SqlManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# These are only imported for Type Hinting and Intellisense.
from azure.mgmt.sql.models import Server
from azure.mgmt.sql.models import Database

# Initialize the Parser.
config = ConfigParser()

# Read the file.
try:
    config.read('config/config.ini')
except:
    config.read('configs/config.ini')

# Grab the Azure Credentials needed.
subscription_id = config.get('azure_credentials', 'azure_subscription_id')
tenant_id = config.get('azure_credentials', 'azure_tenant_id')
client_id = config.get('azure_credentials', 'azure_client_id')
client_secret = config.get('azure_credentials', 'azure_client_secret')

# Define the Credentials.
credential = ServicePrincipalCredentials(
    tenant=tenant_id,
    client_id=client_id,
    secret=client_secret
)

# Initialize the SQL Management Client.
sql_management_client = SqlManagementClient(
    credentials=credential,
    subscription_id=subscription_id
)

# Grab a server using the Resource Group Name.
server: Server = sql_management_client.servers.get(
    resource_group_name='sigma-coding-tutorials',
    server_name='trading-robot'
)
print(server.as_dict())

# Grab the master database from the `trading-robot` server.
database: Database = sql_management_client.databases.get(
    resource_group_name='sigma-coding-tutorials',
    server_name='trading-robot',
    database_name='master'
)
print(database.as_dict())
print(database.name)
print(database.id)
print(database.status)

# Create a new database called `financial-news` on the `trading-robot` server.
operation_result = sql_management_client.databases.create_or_update(
    resource_group_name='resource_group_test',
    server_name='trading-robot',
    database_name='financial-news',
    parameters={
        'location': 'eastus'
    }
)
print(operation_result.result())

# Delete a database from my server.
operation_result = sql_management_client.databases.delete(
    resource_group_name='resource_group_test',
    server_name='trading-robot',
    database_name='financial-news'
)
