# V1beta2CapacityRequestPolicy

CapacityRequestPolicy defines how requests consume device capacity.  Must not set more than one ValidRequestValues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**V1beta1CapacityRequestPolicyDefault**](V1beta1CapacityRequestPolicyDefault.md) |  | [optional] 
**valid_range** | [**V1beta2CapacityRequestPolicyRange**](V1beta2CapacityRequestPolicyRange.md) | ValidRange defines an acceptable quantity value range in consuming requests.  If this field is set, Default must be defined and it must fall within the defined ValidRange.  If the requested amount does not fall within the defined range, the request violates the policy, and this device cannot be allocated.  If the request doesn&#39;t contain this capacity entry, Default value is used. | [optional] 
**valid_values** | [**List[V1PodSpecOverheadValue]**](V1PodSpecOverheadValue.md) | ValidValues defines a set of acceptable quantity values in consuming requests.  Must not contain more than 10 entries. Must be sorted in ascending order.  If this field is set, Default must be defined and it must be included in ValidValues list.  If the requested amount does not match any valid value but smaller than some valid values, the scheduler calculates the smallest valid value that is greater than or equal to the request. That is: min(ceil(requestedValue) ∈ validValues), where requestedValue ≤ max(validValues).  If the requested amount exceeds all valid values, the request violates the policy, and this device cannot be allocated. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1beta2_capacity_request_policy import V1beta2CapacityRequestPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2CapacityRequestPolicy from a JSON string
v1beta2_capacity_request_policy_instance = V1beta2CapacityRequestPolicy.from_json(json)
# print the JSON string representation of the object
print(V1beta2CapacityRequestPolicy.to_json())

# convert the object into a dict
v1beta2_capacity_request_policy_dict = v1beta2_capacity_request_policy_instance.to_dict()
# create an instance of V1beta2CapacityRequestPolicy from a dict
v1beta2_capacity_request_policy_from_dict = V1beta2CapacityRequestPolicy.from_dict(v1beta2_capacity_request_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


