# V1EmptyDirVolumeSourceSizeLimit

sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_empty_dir_volume_source_size_limit import V1EmptyDirVolumeSourceSizeLimit

# TODO update the JSON string below
json = "{}"
# create an instance of V1EmptyDirVolumeSourceSizeLimit from a JSON string
v1_empty_dir_volume_source_size_limit_instance = V1EmptyDirVolumeSourceSizeLimit.from_json(json)
# print the JSON string representation of the object
print(V1EmptyDirVolumeSourceSizeLimit.to_json())

# convert the object into a dict
v1_empty_dir_volume_source_size_limit_dict = v1_empty_dir_volume_source_size_limit_instance.to_dict()
# create an instance of V1EmptyDirVolumeSourceSizeLimit from a dict
v1_empty_dir_volume_source_size_limit_from_dict = V1EmptyDirVolumeSourceSizeLimit.from_dict(v1_empty_dir_volume_source_size_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


