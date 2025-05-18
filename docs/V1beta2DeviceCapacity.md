# V1beta2DeviceCapacity

DeviceCapacity describes a quantity associated with a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value defines how much of a certain device capacity is available. | 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_device_capacity import V1beta2DeviceCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceCapacity from a JSON string
v1beta2_device_capacity_instance = V1beta2DeviceCapacity.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceCapacity.to_json())

# convert the object into a dict
v1beta2_device_capacity_dict = v1beta2_device_capacity_instance.to_dict()
# create an instance of V1beta2DeviceCapacity from a dict
v1beta2_device_capacity_from_dict = V1beta2DeviceCapacity.from_dict(v1beta2_device_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


