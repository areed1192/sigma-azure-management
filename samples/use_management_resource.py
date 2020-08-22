from pprint import pprint
from configparser import ConfigParser

from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# These are only imported for Type Hinting and Intellisense.
from azure.mgmt.resource.resources.models import ResourceGroup
from azure.mgmt.resource.resources.models import GenericResourceExpanded

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Grab the Azure Credentials needed.
tenant_id = config.get('azure_credentials', 'azure_tenant_id')
client_id = config.get('azure_credentials', 'azure_client_id')
client_secret = config.get('azure_credentials', 'azure_client_secret')
subscription_id = config.get('azure_credentials', 'azure_subscription_id')

# Define the Credentials.
credential = ServicePrincipalCredentials(
    tenant=tenant_id,
    client_id=client_id,
    secret=client_secret
)

# Pass through the credential.
resource_management_client = ResourceManagementClient(
    credentials=credential,
    subscription_id=subscription_id
)

# Loop through each resource group that falls under the subscription.
for resource_group in resource_management_client.resource_groups.list():

    # Redfine this for Type Hinting.
    resource_group: ResourceGroup = resource_group

    print('')
    print(resource_group.id)
    print(resource_group.name)
    print(resource_group.managed_by)
    print('')

    pprint(resource_group.as_dict())
