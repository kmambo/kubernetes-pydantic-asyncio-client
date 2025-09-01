# V1beta1CapacityRequestPolicyRangeMin

Min specifies the minimum capacity allowed for a consumption request.  Min must be greater than or equal to zero, and less than or equal to the capacity value. requestPolicy.default must be more than or equal to the minimum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1beta1_capacity_request_policy_range_min import V1beta1CapacityRequestPolicyRangeMin

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CapacityRequestPolicyRangeMin from a JSON string
v1beta1_capacity_request_policy_range_min_instance = V1beta1CapacityRequestPolicyRangeMin.from_json(json)
# print the JSON string representation of the object
print(V1beta1CapacityRequestPolicyRangeMin.to_json())

# convert the object into a dict
v1beta1_capacity_request_policy_range_min_dict = v1beta1_capacity_request_policy_range_min_instance.to_dict()
# create an instance of V1beta1CapacityRequestPolicyRangeMin from a dict
v1beta1_capacity_request_policy_range_min_from_dict = V1beta1CapacityRequestPolicyRangeMin.from_dict(v1beta1_capacity_request_policy_range_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


