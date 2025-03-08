# V1alpha3Device

Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**V1alpha3BasicDevice**](V1alpha3BasicDevice.md) |  | [optional] 
**name** | **str** | Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label. | 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device import V1alpha3Device

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3Device from a JSON string
v1alpha3_device_instance = V1alpha3Device.from_json(json)
# print the JSON string representation of the object
print(V1alpha3Device.to_json())

# convert the object into a dict
v1alpha3_device_dict = v1alpha3_device_instance.to_dict()
# create an instance of V1alpha3Device from a dict
v1alpha3_device_from_dict = V1alpha3Device.from_dict(v1alpha3_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


