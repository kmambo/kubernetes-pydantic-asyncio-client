# V1Scale

Scale represents a scaling request for a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. | [optional] 
**spec** | [**V1ScaleSpec**](V1ScaleSpec.md) | spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. | [optional] 
**status** | [**V1ScaleStatus**](V1ScaleStatus.md) | status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_scale import V1Scale

# TODO update the JSON string below
json = "{}"
# create an instance of V1Scale from a JSON string
v1_scale_instance = V1Scale.from_json(json)
# print the JSON string representation of the object
print(V1Scale.to_json())

# convert the object into a dict
v1_scale_dict = v1_scale_instance.to_dict()
# create an instance of V1Scale from a dict
v1_scale_from_dict = V1Scale.from_dict(v1_scale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


