# V1EmptyDirVolumeSource

Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium** | **str** | medium represents what type of storage medium should back this directory. The default is \&quot;\&quot; which means to use the node&#39;s default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir | [optional] 
**size_limit** | [**V1EmptyDirVolumeSourceSizeLimit**](V1EmptyDirVolumeSourceSizeLimit.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_empty_dir_volume_source import V1EmptyDirVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1EmptyDirVolumeSource from a JSON string
v1_empty_dir_volume_source_instance = V1EmptyDirVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1EmptyDirVolumeSource.to_json())

# convert the object into a dict
v1_empty_dir_volume_source_dict = v1_empty_dir_volume_source_instance.to_dict()
# create an instance of V1EmptyDirVolumeSource from a dict
v1_empty_dir_volume_source_from_dict = V1EmptyDirVolumeSource.from_dict(v1_empty_dir_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


