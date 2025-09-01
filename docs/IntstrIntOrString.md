# IntstrIntOrString

IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.intstr_int_or_string import IntstrIntOrString

# TODO update the JSON string below
json = "{}"
# create an instance of IntstrIntOrString from a JSON string
intstr_int_or_string_instance = IntstrIntOrString.from_json(json)
# print the JSON string representation of the object
print(IntstrIntOrString.to_json())

# convert the object into a dict
intstr_int_or_string_dict = intstr_int_or_string_instance.to_dict()
# create an instance of IntstrIntOrString from a dict
intstr_int_or_string_from_dict = IntstrIntOrString.from_dict(intstr_int_or_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


