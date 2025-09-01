# V1beta1CapacityRequestPolicyDefault

Default specifies how much of this capacity is consumed by a request that does not contain an entry for it in DeviceRequest's Capacity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1beta1_capacity_request_policy_default import V1beta1CapacityRequestPolicyDefault

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CapacityRequestPolicyDefault from a JSON string
v1beta1_capacity_request_policy_default_instance = V1beta1CapacityRequestPolicyDefault.from_json(json)
# print the JSON string representation of the object
print(V1beta1CapacityRequestPolicyDefault.to_json())

# convert the object into a dict
v1beta1_capacity_request_policy_default_dict = v1beta1_capacity_request_policy_default_instance.to_dict()
# create an instance of V1beta1CapacityRequestPolicyDefault from a dict
v1beta1_capacity_request_policy_default_from_dict = V1beta1CapacityRequestPolicyDefault.from_dict(v1beta1_capacity_request_policy_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


