# V1beta2DeviceCapacity

DeviceCapacity describes a quantity associated with a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_policy** | [**V1beta2CapacityRequestPolicy**](V1beta2CapacityRequestPolicy.md) | RequestPolicy defines how this DeviceCapacity must be consumed when the device is allowed to be shared by multiple allocations.  The Device must have allowMultipleAllocations set to true in order to set a requestPolicy.  If unset, capacity requests are unconstrained: requests can consume any amount of capacity, as long as the total consumed across all allocations does not exceed the device&#39;s defined capacity. If request is also unset, default is the full capacity value. | [optional] 
**value** | [**V1beta1DeviceCapacityValue**](V1beta1DeviceCapacityValue.md) |  | 

## Example

```python
from kubernetes_asyncio.models.v1beta2_device_capacity import V1beta2DeviceCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceCapacity from a JSON string
v1beta2_device_capacity_instance = V1beta2DeviceCapacity.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceCapacity.to_json())

# convert the object into a dict
v1beta2_device_capacity_dict = v1beta2_device_capacity_instance.to_dict()
# create an instance of V1beta2DeviceCapacity from a dict
v1beta2_device_capacity_from_dict = V1beta2DeviceCapacity.from_dict(v1beta2_device_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


