# V2HPAScalingRulesTolerance

tolerance is the tolerance on the ratio between the current and desired metric value under which no updates are made to the desired number of replicas (e.g. 0.01 for 1%). Must be greater than or equal to zero. If not set, the default cluster-wide tolerance is applied (by default 10%).  For example, if autoscaling is configured with a memory consumption target of 100Mi, and scale-down and scale-up tolerances of 5% and 1% respectively, scaling will be triggered when the actual consumption falls below 95Mi or exceeds 101Mi.  This is an alpha field and requires enabling the HPAConfigurableTolerance feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio_pydantic.models.v2_hpa_scaling_rules_tolerance import V2HPAScalingRulesTolerance

# TODO update the JSON string below
json = "{}"
# create an instance of V2HPAScalingRulesTolerance from a JSON string
v2_hpa_scaling_rules_tolerance_instance = V2HPAScalingRulesTolerance.from_json(json)
# print the JSON string representation of the object
print(V2HPAScalingRulesTolerance.to_json())

# convert the object into a dict
v2_hpa_scaling_rules_tolerance_dict = v2_hpa_scaling_rules_tolerance_instance.to_dict()
# create an instance of V2HPAScalingRulesTolerance from a dict
v2_hpa_scaling_rules_tolerance_from_dict = V2HPAScalingRulesTolerance.from_dict(v2_hpa_scaling_rules_tolerance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


