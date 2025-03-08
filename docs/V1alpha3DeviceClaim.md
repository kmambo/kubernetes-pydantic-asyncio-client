# V1alpha3DeviceClaim

DeviceClaim defines how to request devices with a ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[V1alpha3DeviceClaimConfiguration]**](V1alpha3DeviceClaimConfiguration.md) | This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim. | [optional] 
**constraints** | [**List[V1alpha3DeviceConstraint]**](V1alpha3DeviceConstraint.md) | These constraints must be satisfied by the set of devices that get allocated for the claim. | [optional] 
**requests** | [**List[V1alpha3DeviceRequest]**](V1alpha3DeviceRequest.md) | Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1alpha3_device_claim import V1alpha3DeviceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceClaim from a JSON string
v1alpha3_device_claim_instance = V1alpha3DeviceClaim.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceClaim.to_json())

# convert the object into a dict
v1alpha3_device_claim_dict = v1alpha3_device_claim_instance.to_dict()
# create an instance of V1alpha3DeviceClaim from a dict
v1alpha3_device_claim_from_dict = V1alpha3DeviceClaim.from_dict(v1alpha3_device_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


