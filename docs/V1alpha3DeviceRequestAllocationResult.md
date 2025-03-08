# V1alpha3DeviceRequestAllocationResult

DeviceRequestAllocationResult contains the allocation result for one request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_access** | **bool** | AdminAccess indicates that this device was allocated for administrative access. See the corresponding request field for a definition of mode.  This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled. | [optional] 
**device** | **str** | Device references one device instance via its name in the driver&#39;s resource pool. It must be a DNS label. | 
**driver** | **str** | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. | 
**pool** | **str** | This name together with the driver name and the device name field identify which device was allocated (&#x60;&lt;driver name&gt;/&lt;pool name&gt;/&lt;device name&gt;&#x60;).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes. | 
**request** | **str** | Request is the name of the request in the claim which caused this device to be allocated. If it references a subrequest in the firstAvailable list on a DeviceRequest, this field must include both the name of the main request and the subrequest using the format &lt;main request&gt;/&lt;subrequest&gt;.  Multiple devices may have been allocated per request. | 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device_request_allocation_result import V1alpha3DeviceRequestAllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceRequestAllocationResult from a JSON string
v1alpha3_device_request_allocation_result_instance = V1alpha3DeviceRequestAllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceRequestAllocationResult.to_json())

# convert the object into a dict
v1alpha3_device_request_allocation_result_dict = v1alpha3_device_request_allocation_result_instance.to_dict()
# create an instance of V1alpha3DeviceRequestAllocationResult from a dict
v1alpha3_device_request_allocation_result_from_dict = V1alpha3DeviceRequestAllocationResult.from_dict(v1alpha3_device_request_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


