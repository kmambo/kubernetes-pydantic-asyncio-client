# V1alpha3Counter

Counter describes a quantity associated with a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value defines how much of a certain device counter is available. | 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_counter import V1alpha3Counter

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3Counter from a JSON string
v1alpha3_counter_instance = V1alpha3Counter.from_json(json)
# print the JSON string representation of the object
print(V1alpha3Counter.to_json())

# convert the object into a dict
v1alpha3_counter_dict = v1alpha3_counter_instance.to_dict()
# create an instance of V1alpha3Counter from a dict
v1alpha3_counter_from_dict = V1alpha3Counter.from_dict(v1alpha3_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


