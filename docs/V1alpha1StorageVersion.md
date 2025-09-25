# V1alpha1StorageVersion

Storage version of a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | The name is &lt;group&gt;.&lt;resource&gt;. | [optional] 
**spec** | **object** | Spec is an empty spec. It is here to comply with Kubernetes API style. | 
**status** | [**V1alpha1StorageVersionStatus**](V1alpha1StorageVersionStatus.md) | API server instances report the version they can decode and the version they encode objects to when persisting objects in the backend. | 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1alpha1_storage_version import V1alpha1StorageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersion from a JSON string
v1alpha1_storage_version_instance = V1alpha1StorageVersion.from_json(json)
# print the JSON string representation of the object
print(V1alpha1StorageVersion.to_json())

# convert the object into a dict
v1alpha1_storage_version_dict = v1alpha1_storage_version_instance.to_dict()
# create an instance of V1alpha1StorageVersion from a dict
v1alpha1_storage_version_from_dict = V1alpha1StorageVersion.from_dict(v1alpha1_storage_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


