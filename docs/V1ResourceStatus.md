# V1ResourceStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the resource. Must be unique within the pod and match one of the resources from the pod spec. | [default to '']
**resources** | [**List[V1ResourceHealth]**](V1ResourceHealth.md) | List of unique Resources health. Each element in the list contains an unique resource ID and resource health. At a minimum, ResourceID must uniquely identify the Resource allocated to the Pod on the Node for the lifetime of a Pod. See ResourceID type for it&#39;s definition. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_resource_status import V1ResourceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceStatus from a JSON string
v1_resource_status_instance = V1ResourceStatus.from_json(json)
# print the JSON string representation of the object
print(V1ResourceStatus.to_json())

# convert the object into a dict
v1_resource_status_dict = v1_resource_status_instance.to_dict()
# create an instance of V1ResourceStatus from a dict
v1_resource_status_from_dict = V1ResourceStatus.from_dict(v1_resource_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


