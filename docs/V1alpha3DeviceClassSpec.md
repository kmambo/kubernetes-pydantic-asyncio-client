# V1alpha3DeviceClassSpec

DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[V1alpha3DeviceClassConfiguration]**](V1alpha3DeviceClassConfiguration.md) | Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim. | [optional] 
**selectors** | [**List[V1alpha3DeviceSelector]**](V1alpha3DeviceSelector.md) | Each selector must be satisfied by a device which is claimed via this class. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device_class_spec import V1alpha3DeviceClassSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceClassSpec from a JSON string
v1alpha3_device_class_spec_instance = V1alpha3DeviceClassSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceClassSpec.to_json())

# convert the object into a dict
v1alpha3_device_class_spec_dict = v1alpha3_device_class_spec_instance.to_dict()
# create an instance of V1alpha3DeviceClassSpec from a dict
v1alpha3_device_class_spec_from_dict = V1alpha3DeviceClassSpec.from_dict(v1alpha3_device_class_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


