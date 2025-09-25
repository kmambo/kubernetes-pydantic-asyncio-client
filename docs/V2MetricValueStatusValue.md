# V2MetricValueStatusValue

value is the current value of the metric (as a quantity).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio_pydantic.models.v2_metric_value_status_value import V2MetricValueStatusValue

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricValueStatusValue from a JSON string
v2_metric_value_status_value_instance = V2MetricValueStatusValue.from_json(json)
# print the JSON string representation of the object
print(V2MetricValueStatusValue.to_json())

# convert the object into a dict
v2_metric_value_status_value_dict = v2_metric_value_status_value_instance.to_dict()
# create an instance of V2MetricValueStatusValue from a dict
v2_metric_value_status_value_from_dict = V2MetricValueStatusValue.from_dict(v2_metric_value_status_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


