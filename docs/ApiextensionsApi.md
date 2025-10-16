# kubernetes_asyncio_pydantic.ApiextensionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_group**](ApiextensionsApi.md#get_api_group) | **GET** /apis/apiextensions.k8s.io/ | 


# **get_api_group**
> V1APIGroup get_api_group()

get information of a group

### Example


```python
import kubernetes_asyncio_pydantic
from kubernetes_asyncio_pydantic.models.v1_api_group import V1APIGroup
from kubernetes_asyncio_pydantic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes_asyncio_pydantic.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with kubernetes_asyncio_pydantic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_asyncio_pydantic.ApiextensionsApi(api_client)

    try:
        api_response = await api_instance.get_api_group()
        print("The response of ApiextensionsApi->get_api_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiextensionsApi->get_api_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1APIGroup**](V1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.kubernetes.protobuf, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

