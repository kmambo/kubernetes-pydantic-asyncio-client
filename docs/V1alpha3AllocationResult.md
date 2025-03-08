# V1alpha3AllocationResult

AllocationResult contains attributes of an allocated resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**V1alpha3DeviceAllocationResult**](V1alpha3DeviceAllocationResult.md) |  | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_allocation_result import V1alpha3AllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3AllocationResult from a JSON string
v1alpha3_allocation_result_instance = V1alpha3AllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1alpha3AllocationResult.to_json())

# convert the object into a dict
v1alpha3_allocation_result_dict = v1alpha3_allocation_result_instance.to_dict()
# create an instance of V1alpha3AllocationResult from a dict
v1alpha3_allocation_result_from_dict = V1alpha3AllocationResult.from_dict(v1alpha3_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


