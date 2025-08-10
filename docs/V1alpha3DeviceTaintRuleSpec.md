# V1alpha3DeviceTaintRuleSpec

DeviceTaintRuleSpec specifies the selector and one taint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_selector** | [**V1alpha3DeviceTaintSelector**](V1alpha3DeviceTaintSelector.md) | DeviceSelector defines which device(s) the taint is applied to. All selector criteria must be satified for a device to match. The empty selector matches all devices. Without a selector, no devices are matches. | [optional] 
**taint** | [**V1alpha3DeviceTaint**](V1alpha3DeviceTaint.md) | The taint that gets applied to matching devices. | 

## Example

```python
from kubernetes_asyncio.models.v1alpha3_device_taint_rule_spec import V1alpha3DeviceTaintRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceTaintRuleSpec from a JSON string
v1alpha3_device_taint_rule_spec_instance = V1alpha3DeviceTaintRuleSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceTaintRuleSpec.to_json())

# convert the object into a dict
v1alpha3_device_taint_rule_spec_dict = v1alpha3_device_taint_rule_spec_instance.to_dict()
# create an instance of V1alpha3DeviceTaintRuleSpec from a dict
v1alpha3_device_taint_rule_spec_from_dict = V1alpha3DeviceTaintRuleSpec.from_dict(v1alpha3_device_taint_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


