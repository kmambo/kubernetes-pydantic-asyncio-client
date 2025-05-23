# V1ListMeta

ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_continue** | **str** | continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message. | [optional] 
**remaining_item_count** | **int** | remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact. | [optional] 
**resource_version** | **str** | String that identifies the server&#39;s internal version of this object that can be used by kubernetes_asyncio.clients to determine when objects have changed. Value must be treated as opaque by kubernetes_asyncio.clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency | [optional] 
**self_link** | **str** | Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_list_meta import V1ListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListMeta from a JSON string
v1_list_meta_instance = V1ListMeta.from_json(json)
# print the JSON string representation of the object
print(V1ListMeta.to_json())

# convert the object into a dict
v1_list_meta_dict = v1_list_meta_instance.to_dict()
# create an instance of V1ListMeta from a dict
v1_list_meta_from_dict = V1ListMeta.from_dict(v1_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


