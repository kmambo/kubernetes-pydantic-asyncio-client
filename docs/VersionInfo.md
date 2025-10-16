# VersionInfo

Info contains versioning information. how we'll want to distribute that information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **str** |  | [default to '']
**compiler** | **str** |  | [default to '']
**git_commit** | **str** |  | [default to '']
**git_tree_state** | **str** |  | [default to '']
**git_version** | **str** |  | [default to '']
**go_version** | **str** |  | [default to '']
**major** | **str** |  | [default to '']
**minor** | **str** |  | [default to '']
**platform** | **str** |  | [default to '']

## Example

```python
from kubernetes_asyncio_pydantic.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print(VersionInfo.to_json())

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_from_dict = VersionInfo.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


