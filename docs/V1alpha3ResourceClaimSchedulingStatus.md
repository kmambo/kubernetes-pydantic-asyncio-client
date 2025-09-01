# V1alpha3ResourceClaimSchedulingStatus

ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with \"WaitForFirstConsumer\" allocation mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name matches the pod.spec.resourceClaims[*].Name field. | [default to '']
**unsuitable_nodes** | **List[str]** | UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha3_resource_claim_scheduling_status import V1alpha3ResourceClaimSchedulingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourceClaimSchedulingStatus from a JSON string
v1alpha3_resource_claim_scheduling_status_instance = V1alpha3ResourceClaimSchedulingStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourceClaimSchedulingStatus.to_json())

# convert the object into a dict
v1alpha3_resource_claim_scheduling_status_dict = v1alpha3_resource_claim_scheduling_status_instance.to_dict()
# create an instance of V1alpha3ResourceClaimSchedulingStatus from a dict
v1alpha3_resource_claim_scheduling_status_from_dict = V1alpha3ResourceClaimSchedulingStatus.from_dict(v1alpha3_resource_claim_scheduling_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


