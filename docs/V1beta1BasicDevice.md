# V1beta1BasicDevice

BasicDevice defines one device instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Dict[str, V1beta1DeviceAttribute]**](V1beta1DeviceAttribute.md) | Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.  The maximum number of attributes and capacities combined is 32. | [optional] 
**capacity** | [**Dict[str, V1beta1DeviceCapacity]**](V1beta1DeviceCapacity.md) | Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.  The maximum number of attributes and capacities combined is 32. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta1_basic_device import V1beta1BasicDevice

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1BasicDevice from a JSON string
v1beta1_basic_device_instance = V1beta1BasicDevice.from_json(json)
# print the JSON string representation of the object
print(V1beta1BasicDevice.to_json())

# convert the object into a dict
v1beta1_basic_device_dict = v1beta1_basic_device_instance.to_dict()
# create an instance of V1beta1BasicDevice from a dict
v1beta1_basic_device_from_dict = V1beta1BasicDevice.from_dict(v1beta1_basic_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


