# V1EventSeries

EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in \"k8s.io/client-go/tools/events/event_broadcaster.go\" shows how this struct is updated on heartbeats and can guide customized reporter implementations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | count is the number of occurrences in this series up to the last heartbeat time. | [default to 0]
**last_observed_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | 

## Example

```python
from kubernetes_asyncio.models.v1_event_series import V1EventSeries

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventSeries from a JSON string
v1_event_series_instance = V1EventSeries.from_json(json)
# print the JSON string representation of the object
print(V1EventSeries.to_json())

# convert the object into a dict
v1_event_series_dict = v1_event_series_instance.to_dict()
# create an instance of V1EventSeries from a dict
v1_event_series_from_dict = V1EventSeries.from_dict(v1_event_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


