# V1JobCondition

JobCondition describes current state of a job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | Human readable message indicating details about last transition. | [optional] 
**reason** | **str** | (brief) reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | [default to '']
**type** | **str** | Type of job condition, Complete or Failed. | [default to '']

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_job_condition import V1JobCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1JobCondition from a JSON string
v1_job_condition_instance = V1JobCondition.from_json(json)
# print the JSON string representation of the object
print(V1JobCondition.to_json())

# convert the object into a dict
v1_job_condition_dict = v1_job_condition_instance.to_dict()
# create an instance of V1JobCondition from a dict
v1_job_condition_from_dict = V1JobCondition.from_dict(v1_job_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


