# V1beta2DeviceConstraint

DeviceConstraint must have exactly one field set besides Requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_attribute** | **str** | MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.  For example, if you specified \&quot;dra.example.com/numa\&quot; (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn&#39;t, then it also will not be chosen.  Must include the domain qualifier. | [optional] 
**requests** | **List[str]** | Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.  References to subrequests must include the name of the main request and may include the subrequest using the format &lt;main request&gt;[/&lt;subrequest&gt;]. If just the main request is given, the constraint applies to all subrequests. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1beta2_device_constraint import V1beta2DeviceConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceConstraint from a JSON string
v1beta2_device_constraint_instance = V1beta2DeviceConstraint.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceConstraint.to_json())

# convert the object into a dict
v1beta2_device_constraint_dict = v1beta2_device_constraint_instance.to_dict()
# create an instance of V1beta2DeviceConstraint from a dict
v1beta2_device_constraint_from_dict = V1beta2DeviceConstraint.from_dict(v1beta2_device_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


