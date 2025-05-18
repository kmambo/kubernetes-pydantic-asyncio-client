# V1beta2AllocationResult

AllocationResult contains attributes of an allocated resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**V1beta2DeviceAllocationResult**](V1beta2DeviceAllocationResult.md) |  | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_allocation_result import V1beta2AllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2AllocationResult from a JSON string
v1beta2_allocation_result_instance = V1beta2AllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1beta2AllocationResult.to_json())

# convert the object into a dict
v1beta2_allocation_result_dict = v1beta2_allocation_result_instance.to_dict()
# create an instance of V1beta2AllocationResult from a dict
v1beta2_allocation_result_from_dict = V1beta2AllocationResult.from_dict(v1beta2_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


