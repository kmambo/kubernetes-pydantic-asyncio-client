# V1ReplicationController

ReplicationController represents the configuration of a replication controller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1ReplicationControllerSpec**](V1ReplicationControllerSpec.md) | Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 
**status** | [**V1ReplicationControllerStatus**](V1ReplicationControllerStatus.md) | Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_replication_controller import V1ReplicationController

# TODO update the JSON string below
json = "{}"
# create an instance of V1ReplicationController from a JSON string
v1_replication_controller_instance = V1ReplicationController.from_json(json)
# print the JSON string representation of the object
print(V1ReplicationController.to_json())

# convert the object into a dict
v1_replication_controller_dict = v1_replication_controller_instance.to_dict()
# create an instance of V1ReplicationController from a dict
v1_replication_controller_from_dict = V1ReplicationController.from_dict(v1_replication_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


