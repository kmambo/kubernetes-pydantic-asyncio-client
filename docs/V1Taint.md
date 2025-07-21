# V1Taint

The node this Taint is attached to has the \"effect\" on any pod that does not tolerate the Taint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. | [default to '']
**key** | **str** | Required. The taint key to be applied to a node. | [default to '']
**time_added** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**value** | **str** | The taint value corresponding to the taint key. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_taint import V1Taint

# TODO update the JSON string below
json = "{}"
# create an instance of V1Taint from a JSON string
v1_taint_instance = V1Taint.from_json(json)
# print the JSON string representation of the object
print(V1Taint.to_json())

# convert the object into a dict
v1_taint_dict = v1_taint_instance.to_dict()
# create an instance of V1Taint from a dict
v1_taint_from_dict = V1Taint.from_dict(v1_taint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


