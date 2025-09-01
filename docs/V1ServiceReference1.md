# V1ServiceReference1

ServiceReference holds a reference to Service.legacy.k8s.io

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the service. Required | [default to '']
**namespace** | **str** | namespace is the namespace of the service. Required | [default to '']
**path** | **str** | path is an optional URL path at which the webhook will be contacted. | [optional] 
**port** | **int** | port is an optional service port at which the webhook will be contacted. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_service_reference1 import V1ServiceReference1

# TODO update the JSON string below
json = "{}"
# create an instance of V1ServiceReference1 from a JSON string
v1_service_reference1_instance = V1ServiceReference1.from_json(json)
# print the JSON string representation of the object
print(V1ServiceReference1.to_json())

# convert the object into a dict
v1_service_reference1_dict = v1_service_reference1_instance.to_dict()
# create an instance of V1ServiceReference1 from a dict
v1_service_reference1_from_dict = V1ServiceReference1.from_dict(v1_service_reference1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


