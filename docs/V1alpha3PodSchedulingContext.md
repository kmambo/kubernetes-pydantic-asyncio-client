# V1alpha3PodSchedulingContext

PodSchedulingContext objects hold information that is needed to schedule a Pod with ResourceClaims that use \"WaitForFirstConsumer\" allocation mode.  This is an alpha type and requires enabling the DRAControlPlaneController feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata | [optional] 
**spec** | [**V1alpha3PodSchedulingContextSpec**](V1alpha3PodSchedulingContextSpec.md) | Spec describes where resources for the Pod are needed. | 
**status** | [**V1alpha3PodSchedulingContextStatus**](V1alpha3PodSchedulingContextStatus.md) | Status describes where resources for the Pod can be allocated. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha3_pod_scheduling_context import V1alpha3PodSchedulingContext

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3PodSchedulingContext from a JSON string
v1alpha3_pod_scheduling_context_instance = V1alpha3PodSchedulingContext.from_json(json)
# print the JSON string representation of the object
print(V1alpha3PodSchedulingContext.to_json())

# convert the object into a dict
v1alpha3_pod_scheduling_context_dict = v1alpha3_pod_scheduling_context_instance.to_dict()
# create an instance of V1alpha3PodSchedulingContext from a dict
v1alpha3_pod_scheduling_context_from_dict = V1alpha3PodSchedulingContext.from_dict(v1alpha3_pod_scheduling_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


