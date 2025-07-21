# V1TokenRequest

TokenRequest contains parameters of a service account token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | audience is the intended audience of the token in \&quot;TokenRequestSpec\&quot;. It will default to the audiences of kube apiserver. | [default to '']
**expiration_seconds** | **int** | expirationSeconds is the duration of validity of the token in \&quot;TokenRequestSpec\&quot;. It has the same default value of \&quot;ExpirationSeconds\&quot; in \&quot;TokenRequestSpec\&quot;. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_token_request import V1TokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenRequest from a JSON string
v1_token_request_instance = V1TokenRequest.from_json(json)
# print the JSON string representation of the object
print(V1TokenRequest.to_json())

# convert the object into a dict
v1_token_request_dict = v1_token_request_instance.to_dict()
# create an instance of V1TokenRequest from a dict
v1_token_request_from_dict = V1TokenRequest.from_dict(v1_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


