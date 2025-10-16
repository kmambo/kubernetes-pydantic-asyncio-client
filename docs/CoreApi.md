# kubernetes_asyncio_pydantic.CoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_versions**](CoreApi.md#get_api_versions) | **GET** /api/ | 


# **get_api_versions**
> V1APIVersions get_api_versions()

get available API versions

### Example


```python
import kubernetes_asyncio_pydantic
from kubernetes_asyncio_pydantic.models.v1_api_versions import V1APIVersions
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
    api_instance = kubernetes_asyncio_pydantic.CoreApi(api_client)

    try:
        api_response = await api_instance.get_api_versions()
        print("The response of CoreApi->get_api_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_api_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1APIVersions**](V1APIVersions.md)

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

