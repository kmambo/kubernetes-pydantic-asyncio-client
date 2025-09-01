# V1beta1CapacityRequestPolicyRangeMax

Max defines the upper limit for capacity that can be requested.  Max must be less than or equal to the capacity value. Min and requestPolicy.default must be less than or equal to the maximum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1beta1_capacity_request_policy_range_max import V1beta1CapacityRequestPolicyRangeMax

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CapacityRequestPolicyRangeMax from a JSON string
v1beta1_capacity_request_policy_range_max_instance = V1beta1CapacityRequestPolicyRangeMax.from_json(json)
# print the JSON string representation of the object
print(V1beta1CapacityRequestPolicyRangeMax.to_json())

# convert the object into a dict
v1beta1_capacity_request_policy_range_max_dict = v1beta1_capacity_request_policy_range_max_instance.to_dict()
# create an instance of V1beta1CapacityRequestPolicyRangeMax from a dict
v1beta1_capacity_request_policy_range_max_from_dict = V1beta1CapacityRequestPolicyRangeMax.from_dict(v1beta1_capacity_request_policy_range_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


