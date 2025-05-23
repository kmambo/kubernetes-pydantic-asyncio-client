# V1DownwardAPIVolumeFile

DownwardAPIVolumeFile represents information to create the file containing the pod field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ref** | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) |  | [optional] 
**mode** | **int** | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**path** | **str** | Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the &#39;..&#39; path. Must be utf-8 encoded. The first item of the relative path must not start with &#39;..&#39; | 
**resource_field_ref** | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_downward_api_volume_file import V1DownwardAPIVolumeFile

# TODO update the JSON string below
json = "{}"
# create an instance of V1DownwardAPIVolumeFile from a JSON string
v1_downward_api_volume_file_instance = V1DownwardAPIVolumeFile.from_json(json)
# print the JSON string representation of the object
print(V1DownwardAPIVolumeFile.to_json())

# convert the object into a dict
v1_downward_api_volume_file_dict = v1_downward_api_volume_file_instance.to_dict()
# create an instance of V1DownwardAPIVolumeFile from a dict
v1_downward_api_volume_file_from_dict = V1DownwardAPIVolumeFile.from_dict(v1_downward_api_volume_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


