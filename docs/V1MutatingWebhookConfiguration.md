# V1MutatingWebhookConfiguration

MutatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and may change the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes_asyncio.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**webhooks** | [**List[V1MutatingWebhook]**](V1MutatingWebhook.md) | Webhooks is a list of webhooks and the affected resources and operations. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_mutating_webhook_configuration import V1MutatingWebhookConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1MutatingWebhookConfiguration from a JSON string
v1_mutating_webhook_configuration_instance = V1MutatingWebhookConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1MutatingWebhookConfiguration.to_json())

# convert the object into a dict
v1_mutating_webhook_configuration_dict = v1_mutating_webhook_configuration_instance.to_dict()
# create an instance of V1MutatingWebhookConfiguration from a dict
v1_mutating_webhook_configuration_from_dict = V1MutatingWebhookConfiguration.from_dict(v1_mutating_webhook_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


