# V1beta2DeviceClassConfiguration

DeviceClassConfiguration is used in DeviceClass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque** | [**V1beta2OpaqueDeviceConfiguration**](V1beta2OpaqueDeviceConfiguration.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_device_class_configuration import V1beta2DeviceClassConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceClassConfiguration from a JSON string
v1beta2_device_class_configuration_instance = V1beta2DeviceClassConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceClassConfiguration.to_json())

# convert the object into a dict
v1beta2_device_class_configuration_dict = v1beta2_device_class_configuration_instance.to_dict()
# create an instance of V1beta2DeviceClassConfiguration from a dict
v1beta2_device_class_configuration_from_dict = V1beta2DeviceClassConfiguration.from_dict(v1beta2_device_class_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


