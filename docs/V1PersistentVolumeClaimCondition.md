# V1PersistentVolumeClaimCondition

PersistentVolumeClaimCondition contains details about state of pvc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | message is the human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | reason is a unique, this should be a short, machine understandable string that gives the reason for condition&#39;s last transition. If it reports \&quot;Resizing\&quot; that means the underlying persistent volume is being resized. | [optional] 
**status** | **str** |  | [default to '']
**type** | **str** |  | [default to '']

## Example

```python
from kubernetes_asyncio.models.v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimCondition from a JSON string
v1_persistent_volume_claim_condition_instance = V1PersistentVolumeClaimCondition.from_json(json)
# print the JSON string representation of the object
print(V1PersistentVolumeClaimCondition.to_json())

# convert the object into a dict
v1_persistent_volume_claim_condition_dict = v1_persistent_volume_claim_condition_instance.to_dict()
# create an instance of V1PersistentVolumeClaimCondition from a dict
v1_persistent_volume_claim_condition_from_dict = V1PersistentVolumeClaimCondition.from_dict(v1_persistent_volume_claim_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


