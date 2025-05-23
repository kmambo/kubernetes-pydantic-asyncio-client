# V1ExecAction

ExecAction describes a \"run in container\" action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **List[str]** | Command is the command line to execute inside the container, the working directory for the command  is root (&#39;/&#39;) in the container&#39;s filesystem. The command is simply exec&#39;d, it is not run inside a shell, so traditional shell instructions (&#39;|&#39;, etc) won&#39;t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_exec_action import V1ExecAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExecAction from a JSON string
v1_exec_action_instance = V1ExecAction.from_json(json)
# print the JSON string representation of the object
print(V1ExecAction.to_json())

# convert the object into a dict
v1_exec_action_dict = v1_exec_action_instance.to_dict()
# create an instance of V1ExecAction from a dict
v1_exec_action_from_dict = V1ExecAction.from_dict(v1_exec_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


