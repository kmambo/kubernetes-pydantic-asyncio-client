# V1beta1DeviceRequest

DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices.  A DeviceClassName is currently required. Clients must check that it is indeed set. It's absence indicates that something changed in a way that is not supported by the client yet, in which case it must refuse to handle the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_access** | **bool** | AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device.  They ignore all ordinary claims to the device with respect to access modes and any resource allocations.  This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled. | [optional] 
**allocation_mode** | **str** | AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:  - ExactCount: This request is for a specific number of devices.   This is the default. The exact number is provided in the   count field.  - All: This request is for all of the matching devices in a pool.   Allocation will fail if some devices are already allocated,   unless adminAccess is requested.  If AlloctionMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes. | [optional] 
**count** | **int** | Count is used only when the count mode is \&quot;ExactCount\&quot;. Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. | [optional] 
**device_class_name** | **str** | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.  A class is required. Which classes are available depends on the cluster.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. | [default to '']
**name** | **str** | Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.  Must be a DNS label. | [default to '']
**selectors** | [**List[V1beta1DeviceSelector]**](V1beta1DeviceSelector.md) | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1beta1_device_request import V1beta1DeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DeviceRequest from a JSON string
v1beta1_device_request_instance = V1beta1DeviceRequest.from_json(json)
# print the JSON string representation of the object
print(V1beta1DeviceRequest.to_json())

# convert the object into a dict
v1beta1_device_request_dict = v1beta1_device_request_instance.to_dict()
# create an instance of V1beta1DeviceRequest from a dict
v1beta1_device_request_from_dict = V1beta1DeviceRequest.from_dict(v1beta1_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


