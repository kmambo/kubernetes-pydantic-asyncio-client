# V1NetworkPolicy

NetworkPolicy describes what network traffic is allowed for a set of Pods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1NetworkPolicySpec**](V1NetworkPolicySpec.md) | spec represents the specification of the desired behavior for this NetworkPolicy. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_network_policy import V1NetworkPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicy from a JSON string
v1_network_policy_instance = V1NetworkPolicy.from_json(json)
# print the JSON string representation of the object
print(V1NetworkPolicy.to_json())

# convert the object into a dict
v1_network_policy_dict = v1_network_policy_instance.to_dict()
# create an instance of V1NetworkPolicy from a dict
v1_network_policy_from_dict = V1NetworkPolicy.from_dict(v1_network_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


