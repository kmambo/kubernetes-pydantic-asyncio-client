# V1DeploymentCondition

DeploymentCondition describes the state of a deployment at a certain point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**last_update_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | [default to '']
**type** | **str** | Type of deployment condition. | [default to '']

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_deployment_condition import V1DeploymentCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeploymentCondition from a JSON string
v1_deployment_condition_instance = V1DeploymentCondition.from_json(json)
# print the JSON string representation of the object
print(V1DeploymentCondition.to_json())

# convert the object into a dict
v1_deployment_condition_dict = v1_deployment_condition_instance.to_dict()
# create an instance of V1DeploymentCondition from a dict
v1_deployment_condition_from_dict = V1DeploymentCondition.from_dict(v1_deployment_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


