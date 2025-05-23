# kubernetes_asyncio.client.ApiregistrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_group**](ApiregistrationApi.md#get_api_group) | **GET** /apis/apiregistration.k8s.io/ | 


# **get_api_group**
> V1APIGroup get_api_group()

get information of a group

### Example

* Api Key Authentication (BearerToken):

```python
import kubernetes_asyncio.client
from kubernetes_asyncio.client.models.v1_api_group import V1APIGroup
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes_asyncio.client.Configuration(
    host = "http://localhost"
)

# The kubernetes_asyncio.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API kubernetes_asyncio.client
async with kubernetes_asyncio.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_asyncio.client.ApiregistrationApi(api_client)

    try:
        api_response = await api_instance.get_api_group()
        print("The response of ApiregistrationApi->get_api_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiregistrationApi->get_api_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1APIGroup**](V1APIGroup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

