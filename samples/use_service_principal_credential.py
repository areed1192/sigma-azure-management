from pprint import pprint
from configparser import ConfigParser

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource.subscriptions import models as sub_models

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Grab the Azure Credentials needed.
tenant_id = config.get('azure_credentials', 'azure_tenant_id')
client_id = config.get('azure_credentials', 'azure_client_id')
client_secret = config.get('azure_credentials', 'azure_client_secret')

# Define the Credentials.
credential = ServicePrincipalCredentials(
    tenant=tenant_id,
    client_id=client_id,
    secret=client_secret
)

# You can grab the Token.
pprint(credential.token)

# Construct Auth.
pprint(credential.construct_auth())

# Grab the Headers.
pprint(credential.header)

# Grab the Store Key.
pprint(credential.store_key)

# Grab the Client Secret.
pprint(credential.secret)

# Grab the Header Scheme.
pprint(credential.scheme)

# You can refresh a Session.
credential.refresh_session()

# You can Sign a Session.
credential.signed_session()
