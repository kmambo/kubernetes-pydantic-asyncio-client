# V1alpha3DeviceSelector

DeviceSelector must have exactly one field set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cel** | [**V1alpha3CELDeviceSelector**](V1alpha3CELDeviceSelector.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device_selector import V1alpha3DeviceSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceSelector from a JSON string
v1alpha3_device_selector_instance = V1alpha3DeviceSelector.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceSelector.to_json())

# convert the object into a dict
v1alpha3_device_selector_dict = v1alpha3_device_selector_instance.to_dict()
# create an instance of V1alpha3DeviceSelector from a dict
v1alpha3_device_selector_from_dict = V1alpha3DeviceSelector.from_dict(v1alpha3_device_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


