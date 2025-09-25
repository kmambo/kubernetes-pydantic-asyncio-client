# V1ResourceFieldSelectorDivisor

Specifies the output format of the exposed resources, defaults to \"1\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_resource_field_selector_divisor import V1ResourceFieldSelectorDivisor

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceFieldSelectorDivisor from a JSON string
v1_resource_field_selector_divisor_instance = V1ResourceFieldSelectorDivisor.from_json(json)
# print the JSON string representation of the object
print(V1ResourceFieldSelectorDivisor.to_json())

# convert the object into a dict
v1_resource_field_selector_divisor_dict = v1_resource_field_selector_divisor_instance.to_dict()
# create an instance of V1ResourceFieldSelectorDivisor from a dict
v1_resource_field_selector_divisor_from_dict = V1ResourceFieldSelectorDivisor.from_dict(v1_resource_field_selector_divisor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


