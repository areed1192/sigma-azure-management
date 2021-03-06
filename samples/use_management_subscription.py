from pprint import pprint
from configparser import ConfigParser

from azure.mgmt.resource import SubscriptionClient

# Just as a note, this is really importing this...
from azure.common.credentials import ServicePrincipalCredentials

# From this...
# from msrestazure.azure_active_directory import ServicePrincipalCredentials

# These are only imported for Type Hinting and Intellisense.
from azure.mgmt.resource.subscriptions.models import TenantCategory
from azure.mgmt.resource.subscriptions.models import TenantIdDescription

# These are only imported for Type Hinting and Intellisense.
from azure.mgmt.resource.subscriptions.models import Subscription
from azure.mgmt.resource.subscriptions.models import SubscriptionPolicies


# Initialize the Parser.
config = ConfigParser()

# Read the file.
try:
    config.read('config/config.ini')
except:
    config.read('configs/config.ini')

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

# Pass through the credential.
subscription_client = SubscriptionClient(credential)

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

# Grab the Subscriptions.
for sub_page in subscription_client.subscriptions.list():

    # Redefine this for Type Hinting.
    subscription: Subscription = sub_page

    print(subscription.id)
    print(subscription.subscription_id)
    print(subscription.display_name)
    print(subscription.tenant_id)

    # Grab the Subscription Policies.
    subscription_policies: SubscriptionPolicies = subscription.subscription_policies

    print(subscription_policies.quota_id)
    print(subscription_policies.location_placement_id)
    print(subscription_policies.spending_limit)

    pprint(subscription.as_dict())
