# AdmissionregistrationV1WebhookClientConfig

WebhookClientConfig contains the information to make a TLS connection with the webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_bundle** | **bytearray** | &#x60;caBundle&#x60; is a PEM encoded CA bundle which will be used to validate the webhook&#39;s server certificate. If unspecified, system trust roots on the apiserver are used. | [optional] 
**service** | [**AdmissionregistrationV1ServiceReference**](AdmissionregistrationV1ServiceReference.md) |  | [optional] 
**url** | **str** | &#x60;url&#x60; gives the location of the webhook, in standard URL form (&#x60;scheme://host:port/path&#x60;). Exactly one of &#x60;url&#x60; or &#x60;service&#x60; must be specified.  The &#x60;host&#x60; should not refer to a service running in the cluster; use the &#x60;service&#x60; field instead. The host might be resolved via external DNS in some apiservers (e.g., &#x60;kube-apiserver&#x60; cannot resolve in-cluster DNS as that would be a layering violation). &#x60;host&#x60; may also be an IP address.  Please note that using &#x60;localhost&#x60; or &#x60;127.0.0.1&#x60; as a &#x60;host&#x60; is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \&quot;https\&quot;; the URL must begin with \&quot;https://\&quot;.  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \&quot;user:password@\&quot; is not allowed. Fragments (\&quot;#...\&quot;) and query parameters (\&quot;?...\&quot;) are not allowed, either. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.admissionregistration_v1_webhook_client_config import AdmissionregistrationV1WebhookClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AdmissionregistrationV1WebhookClientConfig from a JSON string
admissionregistration_v1_webhook_client_config_instance = AdmissionregistrationV1WebhookClientConfig.from_json(json)
# print the JSON string representation of the object
print(AdmissionregistrationV1WebhookClientConfig.to_json())

# convert the object into a dict
admissionregistration_v1_webhook_client_config_dict = admissionregistration_v1_webhook_client_config_instance.to_dict()
# create an instance of AdmissionregistrationV1WebhookClientConfig from a dict
admissionregistration_v1_webhook_client_config_from_dict = AdmissionregistrationV1WebhookClientConfig.from_dict(admissionregistration_v1_webhook_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


