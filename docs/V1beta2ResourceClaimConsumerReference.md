# V1beta2ResourceClaimConsumerReference

ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. | [optional] 
**name** | **str** | Name is the name of resource being referenced. | 
**resource** | **str** | Resource is the type of resource being referenced, for example \&quot;pods\&quot;. | 
**uid** | **str** | UID identifies exactly one incarnation of the resource. | 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_resource_claim_consumer_reference import V1beta2ResourceClaimConsumerReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2ResourceClaimConsumerReference from a JSON string
v1beta2_resource_claim_consumer_reference_instance = V1beta2ResourceClaimConsumerReference.from_json(json)
# print the JSON string representation of the object
print(V1beta2ResourceClaimConsumerReference.to_json())

# convert the object into a dict
v1beta2_resource_claim_consumer_reference_dict = v1beta2_resource_claim_consumer_reference_instance.to_dict()
# create an instance of V1beta2ResourceClaimConsumerReference from a dict
v1beta2_resource_claim_consumer_reference_from_dict = V1beta2ResourceClaimConsumerReference.from_dict(v1beta2_resource_claim_consumer_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


