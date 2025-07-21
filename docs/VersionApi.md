# kubernetes_asyncio.VersionApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code**](VersionApi.md#get_code) | **GET** /version/ | 


# **get_code**
> VersionInfo get_code()

get the version information for this server

### Example


```python
import kubernetes_asyncio
from kubernetes_asyncio.models.version_info import VersionInfo
from kubernetes_asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes_asyncio.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with kubernetes_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_asyncio.VersionApi(api_client)

    try:
        api_response = await api_instance.get_code()
        print("The response of VersionApi->get_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->get_code: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

