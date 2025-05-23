# V1PriorityClass

PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**description** | **str** | description is an arbitrary string that usually provides guidelines on when this priority class should be used. | [optional] 
**global_default** | **bool** | globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as &#x60;globalDefault&#x60;. However, if more than one PriorityClasses exists with their &#x60;globalDefault&#x60; field set to true, the smallest value of such global default PriorityClasses will be used as the default priority. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes_asyncio.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**preemption_policy** | **str** | preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. | [optional] 
**value** | **int** | value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec. | 

## Example

```python
from kubernetes_asyncio.client.models.v1_priority_class import V1PriorityClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1PriorityClass from a JSON string
v1_priority_class_instance = V1PriorityClass.from_json(json)
# print the JSON string representation of the object
print(V1PriorityClass.to_json())

# convert the object into a dict
v1_priority_class_dict = v1_priority_class_instance.to_dict()
# create an instance of V1PriorityClass from a dict
v1_priority_class_from_dict = V1PriorityClass.from_dict(v1_priority_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


