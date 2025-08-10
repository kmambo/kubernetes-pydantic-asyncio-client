# V1beta1CounterValue

Value defines how much of a certain device counter is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1beta1_counter_value import V1beta1CounterValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CounterValue from a JSON string
v1beta1_counter_value_instance = V1beta1CounterValue.from_json(json)
# print the JSON string representation of the object
print(V1beta1CounterValue.to_json())

# convert the object into a dict
v1beta1_counter_value_dict = v1beta1_counter_value_instance.to_dict()
# create an instance of V1beta1CounterValue from a dict
v1beta1_counter_value_from_dict = V1beta1CounterValue.from_dict(v1beta1_counter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


