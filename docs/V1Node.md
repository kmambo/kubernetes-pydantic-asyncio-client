# V1Node

Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1NodeSpec**](V1NodeSpec.md) | Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 
**status** | [**V1NodeStatus**](V1NodeStatus.md) | Most recently observed status of the node. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_node import V1Node

# TODO update the JSON string below
json = "{}"
# create an instance of V1Node from a JSON string
v1_node_instance = V1Node.from_json(json)
# print the JSON string representation of the object
print(V1Node.to_json())

# convert the object into a dict
v1_node_dict = v1_node_instance.to_dict()
# create an instance of V1Node from a dict
v1_node_from_dict = V1Node.from_dict(v1_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


