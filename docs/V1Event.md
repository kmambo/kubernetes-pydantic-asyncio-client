# V1Event

Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters. | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**deprecated_count** | **int** | deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type. | [optional] 
**deprecated_first_timestamp** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**deprecated_last_timestamp** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**deprecated_source** | [**V1EventSource**](V1EventSource.md) | deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type. | [optional] 
**event_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**note** | **str** | note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB. | [optional] 
**reason** | **str** | reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters. | [optional] 
**regarding** | [**V1ObjectReference**](V1ObjectReference.md) | regarding contains the object this Event is about. In most cases it&#39;s an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object. | [optional] 
**related** | [**V1ObjectReference**](V1ObjectReference.md) | related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object. | [optional] 
**reporting_controller** | **str** | reportingController is the name of the controller that emitted this Event, e.g. &#x60;kubernetes.io/kubelet&#x60;. This field cannot be empty for new Events. | [optional] 
**reporting_instance** | **str** | reportingInstance is the ID of the controller instance, e.g. &#x60;kubelet-xyzf&#x60;. This field cannot be empty for new Events and it can have at most 128 characters. | [optional] 
**series** | [**V1EventSeries**](V1EventSeries.md) | series is data about the Event series this event represents or nil if it&#39;s a singleton Event. | [optional] 
**type** | **str** | type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_event import V1Event

# TODO update the JSON string below
json = "{}"
# create an instance of V1Event from a JSON string
v1_event_instance = V1Event.from_json(json)
# print the JSON string representation of the object
print(V1Event.to_json())

# convert the object into a dict
v1_event_dict = v1_event_instance.to_dict()
# create an instance of V1Event from a dict
v1_event_from_dict = V1Event.from_dict(v1_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


