from pprint import pprint

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Initialize the Credentials.
default_credential = DefaultAzureCredential()

# Create a Secret Client.
secret_client = SecretClient(
    vault_url='https://sigma-key-vault.vault.azure.net/',
    credential=default_credential
)

# Set a Secret.
secret_client.set_secret(
    name='my-test-secret-sigma',
    value='hi there'
)

# Get a Secret.
my_secret = secret_client.get_secret(
    name='my-test-secret-sigma'
)

print(my_secret.value)
