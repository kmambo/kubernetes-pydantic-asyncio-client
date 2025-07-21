# V2MetricTargetValue

value is the target value of the metric (as a quantity).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v2_metric_target_value import V2MetricTargetValue

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricTargetValue from a JSON string
v2_metric_target_value_instance = V2MetricTargetValue.from_json(json)
# print the JSON string representation of the object
print(V2MetricTargetValue.to_json())

# convert the object into a dict
v2_metric_target_value_dict = v2_metric_target_value_instance.to_dict()
# create an instance of V2MetricTargetValue from a dict
v2_metric_target_value_from_dict = V2MetricTargetValue.from_dict(v2_metric_target_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


