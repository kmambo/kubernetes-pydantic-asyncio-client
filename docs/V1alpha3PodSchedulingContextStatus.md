# V1alpha3PodSchedulingContextStatus

PodSchedulingContextStatus describes where resources for the Pod can be allocated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_claims** | [**List[V1alpha3ResourceClaimSchedulingStatus]**](V1alpha3ResourceClaimSchedulingStatus.md) | ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses \&quot;WaitForFirstConsumer\&quot; allocation mode. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha3_pod_scheduling_context_status import V1alpha3PodSchedulingContextStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3PodSchedulingContextStatus from a JSON string
v1alpha3_pod_scheduling_context_status_instance = V1alpha3PodSchedulingContextStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3PodSchedulingContextStatus.to_json())

# convert the object into a dict
v1alpha3_pod_scheduling_context_status_dict = v1alpha3_pod_scheduling_context_status_instance.to_dict()
# create an instance of V1alpha3PodSchedulingContextStatus from a dict
v1alpha3_pod_scheduling_context_status_from_dict = V1alpha3PodSchedulingContextStatus.from_dict(v1alpha3_pod_scheduling_context_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


