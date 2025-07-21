# V1WebhookClientConfig1

WebhookClientConfig contains the information to make a TLS connection with the webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_bundle** | **bytearray** | caBundle is a PEM encoded CA bundle which will be used to validate the webhook&#39;s server certificate. If unspecified, system trust roots on the apiserver are used. | [optional] 
**service** | [**V1ServiceReference1**](V1ServiceReference1.md) | service is a reference to the service for this webhook. Either service or url must be specified.  If the webhook is running within the cluster, then you should use &#x60;service&#x60;. | [optional] 
**url** | **str** | url gives the location of the webhook, in standard URL form (&#x60;scheme://host:port/path&#x60;). Exactly one of &#x60;url&#x60; or &#x60;service&#x60; must be specified.  The &#x60;host&#x60; should not refer to a service running in the cluster; use the &#x60;service&#x60; field instead. The host might be resolved via external DNS in some apiservers (e.g., &#x60;kube-apiserver&#x60; cannot resolve in-cluster DNS as that would be a layering violation). &#x60;host&#x60; may also be an IP address.  Please note that using &#x60;localhost&#x60; or &#x60;127.0.0.1&#x60; as a &#x60;host&#x60; is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \&quot;https\&quot;; the URL must begin with \&quot;https://\&quot;.  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \&quot;user:password@\&quot; is not allowed. Fragments (\&quot;#...\&quot;) and query parameters (\&quot;?...\&quot;) are not allowed, either. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_webhook_client_config1 import V1WebhookClientConfig1

# TODO update the JSON string below
json = "{}"
# create an instance of V1WebhookClientConfig1 from a JSON string
v1_webhook_client_config1_instance = V1WebhookClientConfig1.from_json(json)
# print the JSON string representation of the object
print(V1WebhookClientConfig1.to_json())

# convert the object into a dict
v1_webhook_client_config1_dict = v1_webhook_client_config1_instance.to_dict()
# create an instance of V1WebhookClientConfig1 from a dict
v1_webhook_client_config1_from_dict = V1WebhookClientConfig1.from_dict(v1_webhook_client_config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


