# kubernetes_asyncio_pydantic.OpenidApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_account_issuer_open_id_keyset**](OpenidApi.md#get_service_account_issuer_open_id_keyset) | **GET** /openid/v1/jwks/ | 


# **get_service_account_issuer_open_id_keyset**
> str get_service_account_issuer_open_id_keyset()

get service account issuer OpenID JSON Web Key Set (contains public token verification keys)

### Example


```python
import kubernetes_asyncio_pydantic
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
    api_instance = kubernetes_asyncio_pydantic.OpenidApi(api_client)

    try:
        api_response = await api_instance.get_service_account_issuer_open_id_keyset()
        print("The response of OpenidApi->get_service_account_issuer_open_id_keyset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenidApi->get_service_account_issuer_open_id_keyset: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwk-set+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

