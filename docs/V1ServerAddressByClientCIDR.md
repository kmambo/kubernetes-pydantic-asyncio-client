# V1ServerAddressByClientCIDR

ServerAddressByClientCIDR helps the kubernetes_asyncio.client to determine the server address that they should use, depending on the kubernetes_asyncio.clientCIDR that they match.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes_asyncio.client_cidr** | **str** | The CIDR with which kubernetes_asyncio.clients can match their IP to figure out the server address that they should use. | 
**server_address** | **str** | Address of this server, suitable for a kubernetes_asyncio.client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. | 

## Example

```python
from kubernetes_asyncio.client.models.v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR

# TODO update the JSON string below
json = "{}"
# create an instance of V1ServerAddressByClientCIDR from a JSON string
v1_server_address_by_client_cidr_instance = V1ServerAddressByClientCIDR.from_json(json)
# print the JSON string representation of the object
print(V1ServerAddressByClientCIDR.to_json())

# convert the object into a dict
v1_server_address_by_client_cidr_dict = v1_server_address_by_client_cidr_instance.to_dict()
# create an instance of V1ServerAddressByClientCIDR from a dict
v1_server_address_by_client_cidr_from_dict = V1ServerAddressByClientCIDR.from_dict(v1_server_address_by_client_cidr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


