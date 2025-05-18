# V1beta2DeviceAttribute

DeviceAttribute must have exactly one field set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | **bool** | BoolValue is a true/false value. | [optional] 
**int** | **int** | IntValue is a number. | [optional] 
**string** | **str** | StringValue is a string. Must not be longer than 64 characters. | [optional] 
**version** | **str** | VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_device_attribute import V1beta2DeviceAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceAttribute from a JSON string
v1beta2_device_attribute_instance = V1beta2DeviceAttribute.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceAttribute.to_json())

# convert the object into a dict
v1beta2_device_attribute_dict = v1beta2_device_attribute_instance.to_dict()
# create an instance of V1beta2DeviceAttribute from a dict
v1beta2_device_attribute_from_dict = V1beta2DeviceAttribute.from_dict(v1beta2_device_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


