# V1beta2DeviceTaint

The device this taint is attached to has the \"effect\" on any claim which does not tolerate the taint and, through the claim, to pods using the claim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | The effect of the taint on claims that do not tolerate the taint and through such claims on the pods using them. Valid effects are NoSchedule and NoExecute. PreferNoSchedule as used for nodes is not valid here. | 
**key** | **str** | The taint key to be applied to a device. Must be a label name. | 
**time_added** | **datetime** | TimeAdded represents the time at which the taint was added. Added automatically during create or update if not set. | [optional] 
**value** | **str** | The taint value corresponding to the taint key. Must be a label value. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_device_taint import V1beta2DeviceTaint

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceTaint from a JSON string
v1beta2_device_taint_instance = V1beta2DeviceTaint.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceTaint.to_json())

# convert the object into a dict
v1beta2_device_taint_dict = v1beta2_device_taint_instance.to_dict()
# create an instance of V1beta2DeviceTaint from a dict
v1beta2_device_taint_from_dict = V1beta2DeviceTaint.from_dict(v1beta2_device_taint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


