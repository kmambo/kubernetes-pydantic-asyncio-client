# V1beta1AllocatedDeviceStatus

AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | Conditions contains the latest observation of the device&#39;s state. If the device has been configured according to the class and claim config references, the &#x60;Ready&#x60; condition should be True.  Must not contain more than 8 entries. | [optional] 
**data** | **object** | Data contains arbitrary driver-specific data.  The length of the raw data must be smaller or equal to 10 Ki. | [optional] 
**device** | **str** | Device references one device instance via its name in the driver&#39;s resource pool. It must be a DNS label. | 
**driver** | **str** | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. | 
**network_data** | [**V1beta1NetworkDeviceData**](V1beta1NetworkDeviceData.md) |  | [optional] 
**pool** | **str** | This name together with the driver name and the device name field identify which device was allocated (&#x60;&lt;driver name&gt;/&lt;pool name&gt;/&lt;device name&gt;&#x60;).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes. | 

## Example

```python
from kubernetes_asyncio.client.models.v1beta1_allocated_device_status import V1beta1AllocatedDeviceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AllocatedDeviceStatus from a JSON string
v1beta1_allocated_device_status_instance = V1beta1AllocatedDeviceStatus.from_json(json)
# print the JSON string representation of the object
print(V1beta1AllocatedDeviceStatus.to_json())

# convert the object into a dict
v1beta1_allocated_device_status_dict = v1beta1_allocated_device_status_instance.to_dict()
# create an instance of V1beta1AllocatedDeviceStatus from a dict
v1beta1_allocated_device_status_from_dict = V1beta1AllocatedDeviceStatus.from_dict(v1beta1_allocated_device_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


