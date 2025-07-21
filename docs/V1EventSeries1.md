# V1EventSeries1

EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of occurrences in this series up to the last heartbeat time | [optional] 
**last_observed_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_event_series1 import V1EventSeries1

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventSeries1 from a JSON string
v1_event_series1_instance = V1EventSeries1.from_json(json)
# print the JSON string representation of the object
print(V1EventSeries1.to_json())

# convert the object into a dict
v1_event_series1_dict = v1_event_series1_instance.to_dict()
# create an instance of V1EventSeries1 from a dict
v1_event_series1_from_dict = V1EventSeries1.from_dict(v1_event_series1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


