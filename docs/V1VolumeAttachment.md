# V1VolumeAttachment

VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.  VolumeAttachment objects are non-namespaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1VolumeAttachmentSpec**](V1VolumeAttachmentSpec.md) | spec represents specification of the desired attach/detach volume behavior. Populated by the Kubernetes system. | 
**status** | [**V1VolumeAttachmentStatus**](V1VolumeAttachmentStatus.md) | status represents status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_volume_attachment import V1VolumeAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeAttachment from a JSON string
v1_volume_attachment_instance = V1VolumeAttachment.from_json(json)
# print the JSON string representation of the object
print(V1VolumeAttachment.to_json())

# convert the object into a dict
v1_volume_attachment_dict = v1_volume_attachment_instance.to_dict()
# create an instance of V1VolumeAttachment from a dict
v1_volume_attachment_from_dict = V1VolumeAttachment.from_dict(v1_volume_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


