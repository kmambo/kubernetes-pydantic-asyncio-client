# V1alpha3ResourceClaim

ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes_asyncio.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha3ResourceClaimSpec**](V1alpha3ResourceClaimSpec.md) |  | 
**status** | [**V1alpha3ResourceClaimStatus**](V1alpha3ResourceClaimStatus.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_resource_claim import V1alpha3ResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourceClaim from a JSON string
v1alpha3_resource_claim_instance = V1alpha3ResourceClaim.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourceClaim.to_json())

# convert the object into a dict
v1alpha3_resource_claim_dict = v1alpha3_resource_claim_instance.to_dict()
# create an instance of V1alpha3ResourceClaim from a dict
v1alpha3_resource_claim_from_dict = V1alpha3ResourceClaim.from_dict(v1alpha3_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


