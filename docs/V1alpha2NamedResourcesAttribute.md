# V1alpha2NamedResourcesAttribute

NamedResourcesAttribute is a combination of an attribute name and its value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | **bool** | BoolValue is a true/false value. | [optional] 
**int** | **int** | IntValue is a 64-bit integer. | [optional] 
**int_slice** | [**V1alpha2NamedResourcesIntSlice**](V1alpha2NamedResourcesIntSlice.md) | IntSliceValue is an array of 64-bit integers. | [optional] 
**name** | **str** | Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain. | [default to '']
**quantity** | [**V1alpha2NamedResourcesAttributeQuantity**](V1alpha2NamedResourcesAttributeQuantity.md) |  | [optional] 
**string** | **str** | StringValue is a string. | [optional] 
**string_slice** | [**V1alpha2NamedResourcesStringSlice**](V1alpha2NamedResourcesStringSlice.md) | StringSliceValue is an array of strings. | [optional] 
**version** | **str** | VersionValue is a semantic version according to semver.org spec 2.0.0. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha2_named_resources_attribute import V1alpha2NamedResourcesAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesAttribute from a JSON string
v1alpha2_named_resources_attribute_instance = V1alpha2NamedResourcesAttribute.from_json(json)
# print the JSON string representation of the object
print(V1alpha2NamedResourcesAttribute.to_json())

# convert the object into a dict
v1alpha2_named_resources_attribute_dict = v1alpha2_named_resources_attribute_instance.to_dict()
# create an instance of V1alpha2NamedResourcesAttribute from a dict
v1alpha2_named_resources_attribute_from_dict = V1alpha2NamedResourcesAttribute.from_dict(v1alpha2_named_resources_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


