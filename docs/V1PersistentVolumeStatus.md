# V1PersistentVolumeStatus

PersistentVolumeStatus is the current status of a persistent volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_phase_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | message is a human-readable message indicating details about why the volume is in this state. | [optional] 
**phase** | **str** | phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase | [optional] 
**reason** | **str** | reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_persistent_volume_status import V1PersistentVolumeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeStatus from a JSON string
v1_persistent_volume_status_instance = V1PersistentVolumeStatus.from_json(json)
# print the JSON string representation of the object
print(V1PersistentVolumeStatus.to_json())

# convert the object into a dict
v1_persistent_volume_status_dict = v1_persistent_volume_status_instance.to_dict()
# create an instance of V1PersistentVolumeStatus from a dict
v1_persistent_volume_status_from_dict = V1PersistentVolumeStatus.from_dict(v1_persistent_volume_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


