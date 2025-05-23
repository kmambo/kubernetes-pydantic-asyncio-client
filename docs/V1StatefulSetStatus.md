# V1StatefulSetStatus

StatefulSetStatus represents the current state of a StatefulSet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset. | [optional] 
**collision_count** | **int** | collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. | [optional] 
**conditions** | [**List[V1StatefulSetCondition]**](V1StatefulSetCondition.md) | Represents the latest available observations of a statefulset&#39;s current state. | [optional] 
**current_replicas** | **int** | currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision. | [optional] 
**current_revision** | **str** | currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas). | [optional] 
**observed_generation** | **int** | observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet&#39;s generation, which is updated on mutation by the API Server. | [optional] 
**ready_replicas** | **int** | readyReplicas is the number of pods created for this StatefulSet with a Ready Condition. | [optional] 
**replicas** | **int** | replicas is the number of Pods created by the StatefulSet controller. | 
**update_revision** | **str** | updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas) | [optional] 
**updated_replicas** | **int** | updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_stateful_set_status import V1StatefulSetStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1StatefulSetStatus from a JSON string
v1_stateful_set_status_instance = V1StatefulSetStatus.from_json(json)
# print the JSON string representation of the object
print(V1StatefulSetStatus.to_json())

# convert the object into a dict
v1_stateful_set_status_dict = v1_stateful_set_status_instance.to_dict()
# create an instance of V1StatefulSetStatus from a dict
v1_stateful_set_status_from_dict = V1StatefulSetStatus.from_dict(v1_stateful_set_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


