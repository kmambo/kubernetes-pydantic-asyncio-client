# V1ServiceReference2

ServiceReference holds a reference to Service.legacy.k8s.io

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the service | [optional] 
**namespace** | **str** | Namespace is the namespace of the service | [optional] 
**port** | **int** | If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_service_reference2 import V1ServiceReference2

# TODO update the JSON string below
json = "{}"
# create an instance of V1ServiceReference2 from a JSON string
v1_service_reference2_instance = V1ServiceReference2.from_json(json)
# print the JSON string representation of the object
print(V1ServiceReference2.to_json())

# convert the object into a dict
v1_service_reference2_dict = v1_service_reference2_instance.to_dict()
# create an instance of V1ServiceReference2 from a dict
v1_service_reference2_from_dict = V1ServiceReference2.from_dict(v1_service_reference2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


