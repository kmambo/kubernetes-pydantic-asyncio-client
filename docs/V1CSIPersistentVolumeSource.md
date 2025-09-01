# V1CSIPersistentVolumeSource

Represents storage that is managed by an external CSI volume driver (Beta feature)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_expand_secret_ref** | [**V1SecretReference**](V1SecretReference.md) | controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**controller_publish_secret_ref** | [**V1SecretReference**](V1SecretReference.md) | controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**driver** | **str** | driver is the name of the driver to use for this volume. Required. | [default to '']
**fs_type** | **str** | fsType to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. | [optional] 
**node_expand_secret_ref** | [**V1SecretReference**](V1SecretReference.md) | nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**node_publish_secret_ref** | [**V1SecretReference**](V1SecretReference.md) | nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**node_stage_secret_ref** | [**V1SecretReference**](V1SecretReference.md) | nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. | [optional] 
**read_only** | **bool** | readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). | [optional] 
**volume_attributes** | **Dict[str, str]** | volumeAttributes of the volume to publish. | [optional] 
**volume_handle** | **str** | volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. | [default to '']

## Example

```python
from kubernetes_asyncio.models.v1_csi_persistent_volume_source import V1CSIPersistentVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIPersistentVolumeSource from a JSON string
v1_csi_persistent_volume_source_instance = V1CSIPersistentVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1CSIPersistentVolumeSource.to_json())

# convert the object into a dict
v1_csi_persistent_volume_source_dict = v1_csi_persistent_volume_source_instance.to_dict()
# create an instance of V1CSIPersistentVolumeSource from a dict
v1_csi_persistent_volume_source_from_dict = V1CSIPersistentVolumeSource.from_dict(v1_csi_persistent_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


