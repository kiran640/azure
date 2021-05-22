import os

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

subscription_id = 'aa'
credentials = ServicePrincipalCredentials(
    client_id='aa',
    secret='aa-',
    tenant='aa'
)
client = ResourceManagementClient(credentials, subscription_id)

for item in client.resource_groups.list(): #######################for resouce group list
    print(item)
for item in client.resource_groups.list_resources(GROUP_NAME):####################for resouces within group
    print(item)
