# V1alpha3DeviceCounterConsumption

DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_set** | **str** | CounterSet defines the set from which the counters defined will be consumed. | 
**counters** | [**Dict[str, V1alpha3Counter]**](V1alpha3Counter.md) | Counters defines the Counter that will be consumed by the device.  The maximum number counters in a device is 32. In addition, the maximum number of all counters in all devices is 1024 (for example, 64 devices with 16 counters each). | 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device_counter_consumption import V1alpha3DeviceCounterConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceCounterConsumption from a JSON string
v1alpha3_device_counter_consumption_instance = V1alpha3DeviceCounterConsumption.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceCounterConsumption.to_json())

# convert the object into a dict
v1alpha3_device_counter_consumption_dict = v1alpha3_device_counter_consumption_instance.to_dict()
# create an instance of V1alpha3DeviceCounterConsumption from a dict
v1alpha3_device_counter_consumption_from_dict = V1alpha3DeviceCounterConsumption.from_dict(v1alpha3_device_counter_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


