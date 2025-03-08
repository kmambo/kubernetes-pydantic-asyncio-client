# V1alpha3DeviceSubRequest

DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.  DeviceSubRequest is similar to Request, but doesn't expose the AdminAccess or FirstAvailable fields, as those can only be set on the top-level request. AdminAccess is not supported for requests with a prioritized list, and recursive FirstAvailable fields are not supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_mode** | **str** | AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:  - ExactCount: This request is for a specific number of devices.   This is the default. The exact number is provided in the   count field.  - All: This request is for all of the matching devices in a pool.   Allocation will fail if some devices are already allocated,   unless adminAccess is requested.  If AlloctionMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes. | [optional] 
**count** | **int** | Count is used only when the count mode is \&quot;ExactCount\&quot;. Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. | [optional] 
**device_class_name** | **str** | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this subrequest.  A class is required. Which classes are available depends on the cluster.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. | 
**name** | **str** | Name can be used to reference this subrequest in the list of constraints or the list of configurations for the claim. References must use the format &lt;main request&gt;/&lt;subrequest&gt;.  Must be a DNS label. | 
**selectors** | [**List[V1alpha3DeviceSelector]**](V1alpha3DeviceSelector.md) | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device_sub_request import V1alpha3DeviceSubRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceSubRequest from a JSON string
v1alpha3_device_sub_request_instance = V1alpha3DeviceSubRequest.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceSubRequest.to_json())

# convert the object into a dict
v1alpha3_device_sub_request_dict = v1alpha3_device_sub_request_instance.to_dict()
# create an instance of V1alpha3DeviceSubRequest from a dict
v1alpha3_device_sub_request_from_dict = V1alpha3DeviceSubRequest.from_dict(v1alpha3_device_sub_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


