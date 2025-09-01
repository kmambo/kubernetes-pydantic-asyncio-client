# V1alpha3ResourceClaimSpec

ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | **str** | Controller is the name of the DRA driver that is meant to handle allocation of this claim. If empty, allocation is handled by the scheduler while scheduling a pod.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  This is an alpha field and requires enabling the DRAControlPlaneController feature gate. | [optional] 
**devices** | [**V1alpha3DeviceClaim**](V1alpha3DeviceClaim.md) | Devices defines how to request devices. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha3_resource_claim_spec import V1alpha3ResourceClaimSpec

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


