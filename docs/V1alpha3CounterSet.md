# V1alpha3CounterSet

CounterSet defines a named set of counters that are available to be used by devices defined in the ResourceSlice.  The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**Dict[str, V1alpha3Counter]**](V1alpha3Counter.md) | Counters defines the counters that will be consumed by the device. The name of each counter must be unique in that set and must be a DNS label.  To ensure this uniqueness, capacities defined by the vendor must be listed without the driver name as domain prefix in their name. All others must be listed with their domain prefix.  The maximum number of counters is 32. | 
**name** | **str** | CounterSet is the name of the set from which the counters defined will be consumed. | 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_counter_set import V1alpha3CounterSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3CounterSet from a JSON string
v1alpha3_counter_set_instance = V1alpha3CounterSet.from_json(json)
# print the JSON string representation of the object
print(V1alpha3CounterSet.to_json())

# convert the object into a dict
v1alpha3_counter_set_dict = v1alpha3_counter_set_instance.to_dict()
# create an instance of V1alpha3CounterSet from a dict
v1alpha3_counter_set_from_dict = V1alpha3CounterSet.from_dict(v1alpha3_counter_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


