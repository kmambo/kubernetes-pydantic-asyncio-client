# V1ServiceReference

ServiceReference holds a reference to Service.legacy.k8s.io

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &#x60;name&#x60; is the name of the service. Required | [default to '']
**namespace** | **str** | &#x60;namespace&#x60; is the namespace of the service. Required | [default to '']
**path** | **str** | &#x60;path&#x60; is an optional URL path which will be sent in any request to this service. | [optional] 
**port** | **int** | If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_service_reference import V1ServiceReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1ServiceReference from a JSON string
v1_service_reference_instance = V1ServiceReference.from_json(json)
# print the JSON string representation of the object
print(V1ServiceReference.to_json())

# convert the object into a dict
v1_service_reference_dict = v1_service_reference_instance.to_dict()
# create an instance of V1ServiceReference from a dict
v1_service_reference_from_dict = V1ServiceReference.from_dict(v1_service_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


