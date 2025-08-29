# V1ResourceClaim1

ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata | [optional] 
**spec** | [**V1ResourceClaimSpec**](V1ResourceClaimSpec.md) | Spec describes what is being requested and how to configure it. The spec is immutable. | 
**status** | [**V1ResourceClaimStatus**](V1ResourceClaimStatus.md) | Status describes whether the claim is ready to use and what has been allocated. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_resource_claim1 import V1ResourceClaim1

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceClaim1 from a JSON string
v1_resource_claim1_instance = V1ResourceClaim1.from_json(json)
# print the JSON string representation of the object
print(V1ResourceClaim1.to_json())

# convert the object into a dict
v1_resource_claim1_dict = v1_resource_claim1_instance.to_dict()
# create an instance of V1ResourceClaim1 from a dict
v1_resource_claim1_from_dict = V1ResourceClaim1.from_dict(v1_resource_claim1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


