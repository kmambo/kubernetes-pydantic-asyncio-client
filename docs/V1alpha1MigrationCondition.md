# V1alpha1MigrationCondition

Describes the state of a migration at a certain point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_update_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | [default to '']
**type** | **str** | Type of the condition. | [default to '']

## Example

```python
from kubernetes_asyncio.models.v1alpha1_migration_condition import V1alpha1MigrationCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1MigrationCondition from a JSON string
v1alpha1_migration_condition_instance = V1alpha1MigrationCondition.from_json(json)
# print the JSON string representation of the object
print(V1alpha1MigrationCondition.to_json())

# convert the object into a dict
v1alpha1_migration_condition_dict = v1alpha1_migration_condition_instance.to_dict()
# create an instance of V1alpha1MigrationCondition from a dict
v1alpha1_migration_condition_from_dict = V1alpha1MigrationCondition.from_dict(v1alpha1_migration_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


