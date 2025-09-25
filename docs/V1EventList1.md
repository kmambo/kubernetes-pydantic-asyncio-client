# V1EventList1

EventList is a list of events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1Event1]**](V1Event1.md) | List of events | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) | Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_event_list1 import V1EventList1

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventList1 from a JSON string
v1_event_list1_instance = V1EventList1.from_json(json)
# print the JSON string representation of the object
print(V1EventList1.to_json())

# convert the object into a dict
v1_event_list1_dict = v1_event_list1_instance.to_dict()
# create an instance of V1EventList1 from a dict
v1_event_list1_from_dict = V1EventList1.from_dict(v1_event_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


