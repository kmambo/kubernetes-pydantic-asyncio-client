# V1IngressBackend

IngressBackend describes all endpoints for a given service and port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) | resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with \&quot;Service\&quot;. | [optional] 
**service** | [**V1IngressServiceBackend**](V1IngressServiceBackend.md) | service references a service as a backend. This is a mutually exclusive setting with \&quot;Resource\&quot;. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_ingress_backend import V1IngressBackend

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressBackend from a JSON string
v1_ingress_backend_instance = V1IngressBackend.from_json(json)
# print the JSON string representation of the object
print(V1IngressBackend.to_json())

# convert the object into a dict
v1_ingress_backend_dict = v1_ingress_backend_instance.to_dict()
# create an instance of V1IngressBackend from a dict
v1_ingress_backend_from_dict = V1IngressBackend.from_dict(v1_ingress_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


