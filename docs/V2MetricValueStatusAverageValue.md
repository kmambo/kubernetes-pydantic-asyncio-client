# V2MetricValueStatusAverageValue

averageValue is the current value of the average of the metric across all relevant pods (as a quantity)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio_pydantic.models.v2_metric_value_status_average_value import V2MetricValueStatusAverageValue

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricValueStatusAverageValue from a JSON string
v2_metric_value_status_average_value_instance = V2MetricValueStatusAverageValue.from_json(json)
# print the JSON string representation of the object
print(V2MetricValueStatusAverageValue.to_json())

# convert the object into a dict
v2_metric_value_status_average_value_dict = v2_metric_value_status_average_value_instance.to_dict()
# create an instance of V2MetricValueStatusAverageValue from a dict
v2_metric_value_status_average_value_from_dict = V2MetricValueStatusAverageValue.from_dict(v2_metric_value_status_average_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


