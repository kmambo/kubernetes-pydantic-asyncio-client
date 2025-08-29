# V1AllocationResult

AllocationResult contains attributes of an allocated resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_timestamp** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**devices** | [**V1DeviceAllocationResult**](V1DeviceAllocationResult.md) | Devices is the result of allocating devices. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) | NodeSelector defines where the allocated resources are available. If unset, they are available everywhere. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_allocation_result import V1AllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1AllocationResult from a JSON string
v1_allocation_result_instance = V1AllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1AllocationResult.to_json())

# convert the object into a dict
v1_allocation_result_dict = v1_allocation_result_instance.to_dict()
# create an instance of V1AllocationResult from a dict
v1_allocation_result_from_dict = V1AllocationResult.from_dict(v1_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


