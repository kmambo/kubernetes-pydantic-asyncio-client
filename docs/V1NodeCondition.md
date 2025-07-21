# V1NodeCondition

NodeCondition contains condition information for a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_heartbeat_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | Human readable message indicating details about last transition. | [optional] 
**reason** | **str** | (brief) reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | [default to '']
**type** | **str** | Type of node condition. | [default to '']

## Example

```python
from kubernetes_asyncio.models.v1_node_condition import V1NodeCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeCondition from a JSON string
v1_node_condition_instance = V1NodeCondition.from_json(json)
# print the JSON string representation of the object
print(V1NodeCondition.to_json())

# convert the object into a dict
v1_node_condition_dict = v1_node_condition_instance.to_dict()
# create an instance of V1NodeCondition from a dict
v1_node_condition_from_dict = V1NodeCondition.from_dict(v1_node_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


