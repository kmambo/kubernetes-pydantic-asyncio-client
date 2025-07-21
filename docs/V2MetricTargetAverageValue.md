# V2MetricTargetAverageValue

averageValue is the target value of the average of the metric across all relevant pods (as a quantity)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v2_metric_target_average_value import V2MetricTargetAverageValue

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricTargetAverageValue from a JSON string
v2_metric_target_average_value_instance = V2MetricTargetAverageValue.from_json(json)
# print the JSON string representation of the object
print(V2MetricTargetAverageValue.to_json())

# convert the object into a dict
v2_metric_target_average_value_dict = v2_metric_target_average_value_instance.to_dict()
# create an instance of V2MetricTargetAverageValue from a dict
v2_metric_target_average_value_from_dict = V2MetricTargetAverageValue.from_dict(v2_metric_target_average_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


