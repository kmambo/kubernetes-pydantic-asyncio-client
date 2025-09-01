# V1beta2CapacityRequestPolicyRange

CapacityRequestPolicyRange defines a valid range for consumable capacity values.    - If the requested amount is less than Min, it is rounded up to the Min value.   - If Step is set and the requested amount is between Min and Max but not aligned with Step,     it will be rounded up to the next value equal to Min + (n * Step).   - If Step is not set, the requested amount is used as-is if it falls within the range Min to Max (if set).   - If the requested or rounded amount exceeds Max (if set), the request does not satisfy the policy,     and the device cannot be allocated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | [**V1beta1CapacityRequestPolicyRangeMax**](V1beta1CapacityRequestPolicyRangeMax.md) |  | [optional] 
**min** | [**V1beta1CapacityRequestPolicyRangeMin**](V1beta1CapacityRequestPolicyRangeMin.md) |  | 
**step** | [**V1beta1CapacityRequestPolicyRangeStep**](V1beta1CapacityRequestPolicyRangeStep.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1beta2_capacity_request_policy_range import V1beta2CapacityRequestPolicyRange

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2CapacityRequestPolicyRange from a JSON string
v1beta2_capacity_request_policy_range_instance = V1beta2CapacityRequestPolicyRange.from_json(json)
# print the JSON string representation of the object
print(V1beta2CapacityRequestPolicyRange.to_json())

# convert the object into a dict
v1beta2_capacity_request_policy_range_dict = v1beta2_capacity_request_policy_range_instance.to_dict()
# create an instance of V1beta2CapacityRequestPolicyRange from a dict
v1beta2_capacity_request_policy_range_from_dict = V1beta2CapacityRequestPolicyRange.from_dict(v1beta2_capacity_request_policy_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


