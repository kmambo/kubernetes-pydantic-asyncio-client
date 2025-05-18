# V1beta2NetworkDeviceData

NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_address** | **str** | HardwareAddress represents the hardware address (e.g. MAC Address) of the device&#39;s network interface.  Must not be longer than 128 characters. | [optional] 
**interface_name** | **str** | InterfaceName specifies the name of the network interface associated with the allocated device. This might be the name of a physical or virtual network interface being configured in the pod.  Must not be longer than 256 characters. | [optional] 
**ips** | **List[str]** | IPs lists the network addresses assigned to the device&#39;s network interface. This can include both IPv4 and IPv6 addresses. The IPs are in the CIDR notation, which includes both the address and the associated subnet mask. e.g.: \&quot;192.0.2.5/24\&quot; for IPv4 and \&quot;2001:db8::5/64\&quot; for IPv6. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_network_device_data import V1beta2NetworkDeviceData

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2NetworkDeviceData from a JSON string
v1beta2_network_device_data_instance = V1beta2NetworkDeviceData.from_json(json)
# print the JSON string representation of the object
print(V1beta2NetworkDeviceData.to_json())

# convert the object into a dict
v1beta2_network_device_data_dict = v1beta2_network_device_data_instance.to_dict()
# create an instance of V1beta2NetworkDeviceData from a dict
v1beta2_network_device_data_from_dict = V1beta2NetworkDeviceData.from_dict(v1beta2_network_device_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


