# V1alpha3ResourceClaimSpec

ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**V1alpha3DeviceClaim**](V1alpha3DeviceClaim.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_resource_claim_spec import V1alpha3ResourceClaimSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourceClaimSpec from a JSON string
v1alpha3_resource_claim_spec_instance = V1alpha3ResourceClaimSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourceClaimSpec.to_json())

# convert the object into a dict
v1alpha3_resource_claim_spec_dict = v1alpha3_resource_claim_spec_instance.to_dict()
# create an instance of V1alpha3ResourceClaimSpec from a dict
v1alpha3_resource_claim_spec_from_dict = V1alpha3ResourceClaimSpec.from_dict(v1alpha3_resource_claim_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


