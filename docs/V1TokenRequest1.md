# V1TokenRequest1

TokenRequest requests a token for a given service account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1TokenRequestSpec**](V1TokenRequestSpec.md) | Spec holds information about the request being evaluated | 
**status** | [**V1TokenRequestStatus**](V1TokenRequestStatus.md) | Status is filled in by the server and indicates whether the token can be authenticated. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_token_request1 import V1TokenRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenRequest1 from a JSON string
v1_token_request1_instance = V1TokenRequest1.from_json(json)
# print the JSON string representation of the object
print(V1TokenRequest1.to_json())

# convert the object into a dict
v1_token_request1_dict = v1_token_request1_instance.to_dict()
# create an instance of V1TokenRequest1 from a dict
v1_token_request1_from_dict = V1TokenRequest1.from_dict(v1_token_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


