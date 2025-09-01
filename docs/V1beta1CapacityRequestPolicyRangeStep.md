# V1beta1CapacityRequestPolicyRangeStep

Step defines the step size between valid capacity amounts within the range.  Max (if set) and requestPolicy.default must be a multiple of Step. Min + Step must be less than or equal to the capacity value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1beta1_capacity_request_policy_range_step import V1beta1CapacityRequestPolicyRangeStep

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CapacityRequestPolicyRangeStep from a JSON string
v1beta1_capacity_request_policy_range_step_instance = V1beta1CapacityRequestPolicyRangeStep.from_json(json)
# print the JSON string representation of the object
print(V1beta1CapacityRequestPolicyRangeStep.to_json())

# convert the object into a dict
v1beta1_capacity_request_policy_range_step_dict = v1beta1_capacity_request_policy_range_step_instance.to_dict()
# create an instance of V1beta1CapacityRequestPolicyRangeStep from a dict
v1beta1_capacity_request_policy_range_step_from_dict = V1beta1CapacityRequestPolicyRangeStep.from_dict(v1beta1_capacity_request_policy_range_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


