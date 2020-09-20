import os

print("Azure Tenant ID is: {id}".format(id=os.environ['AZURE_TENANT_ID']))
print("Azure Client ID is: {id}".format(id=os.environ['AZURE_CLIENT_ID']))
print("Azure Client Secret is: {id}".format(id=os.environ['AZURE_CLIENT_SECRET']))
