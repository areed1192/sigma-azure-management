from pprint import pprint
from configparser import ConfigParser

from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

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

# Define the Compute Client.
compute_client = ComputeManagementClient(
    credentials=credential,
    subscription_id=subscription_id
)

# Define the Virtual Machine Parameters neededto create One.
VM_PARAMETERS = {
    'location': 'LOCATION',
    'os_profile': {
        'computer_name': 'VM_NAME',
        'admin_username': 'USERNAME',
        'admin_password': 'PASSWORD'
    },
    'hardware_profile': {
        'vm_size': 'Standard_DS1_v2'
    },
    'storage_profile': {
        'image_reference': {
            'publisher': 'Canonical',
            'offer': 'UbuntuServer',
            'sku': '16.04.0-LTS',
            'version': 'latest'
        },
    },
    'network_profile': {
        'network_interfaces': [{
            'id': 'NIC_ID',
        }]
    },
}

# Create a Virtual Machine.
creation_operation = compute_client.virtual_machines.create_or_update(
    resource_group_name='',
    vm_name='',
    parameters=VM_PARAMETERS
)
