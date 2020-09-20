import json

from pprint import pprint
from configparser import ConfigParser

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import SubscriptionClient

# These are only imported for Type Hinting and Intellisense.
from azure.mgmt.resource.subscriptions.models import TenantCategory
from azure.mgmt.resource.subscriptions.models import TenantIdDescription

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

# Load the Auth File.
with open(file='config/credentials/azure_sigma_auth_sp.jsonc', mode='r') as auth_file:
    auth_dict = json.load(fp=auth_file)

# Retrieve the IDs and secret to use with ServicePrincipalCredentials
tenant_id = auth_dict['tenantId']
client_id = auth_dict['clientId']
client_secret = auth_dict['clientSecret']

# Grab our credentials.
credential = DefaultAzureCredential()

# Pass through the credential.
subscription_client = SubscriptionClient(
    credentials=credential
)

# Grab the Subscriptions Tenants.
for tenant_page in subscription_client.tenants.list():

    # Redfine this for Type Hinting.
    tenant: TenantIdDescription = tenant_page

    print(tenant.id)
    print(tenant.tenant_id)
    print(tenant.domains)
    print(tenant.country)

    # If you want a "dictionary", you need to explicitly say that.
    pprint(tenant.as_dict())

    # some objects will return other "objects".
    tenant_category: TenantCategory = tenant.tenant_category