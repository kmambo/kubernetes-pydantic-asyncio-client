# V1PersistentVolumeSpec

PersistentVolumeSpec is the specification of a persistent volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes | [optional] 
**aws_elastic_block_store** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) |  | [optional] 
**azure_disk** | [**V1AzureDiskVolumeSource**](V1AzureDiskVolumeSource.md) |  | [optional] 
**azure_file** | [**V1AzureFilePersistentVolumeSource**](V1AzureFilePersistentVolumeSource.md) |  | [optional] 
**capacity** | **Dict[str, str]** | capacity is the description of the persistent volume&#39;s resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity | [optional] 
**cephfs** | [**V1CephFSPersistentVolumeSource**](V1CephFSPersistentVolumeSource.md) |  | [optional] 
**cinder** | [**V1CinderPersistentVolumeSource**](V1CinderPersistentVolumeSource.md) |  | [optional] 
**claim_ref** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**csi** | [**V1CSIPersistentVolumeSource**](V1CSIPersistentVolumeSource.md) |  | [optional] 
**fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) |  | [optional] 
**flex_volume** | [**V1FlexPersistentVolumeSource**](V1FlexPersistentVolumeSource.md) |  | [optional] 
**flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) |  | [optional] 
**gce_persistent_disk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) |  | [optional] 
**glusterfs** | [**V1GlusterfsPersistentVolumeSource**](V1GlusterfsPersistentVolumeSource.md) |  | [optional] 
**host_path** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) |  | [optional] 
**iscsi** | [**V1ISCSIPersistentVolumeSource**](V1ISCSIPersistentVolumeSource.md) |  | [optional] 
**local** | [**V1LocalVolumeSource**](V1LocalVolumeSource.md) |  | [optional] 
**mount_options** | **List[str]** | mountOptions is the list of mount options, e.g. [\&quot;ro\&quot;, \&quot;soft\&quot;]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options | [optional] 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) |  | [optional] 
**node_affinity** | [**V1VolumeNodeAffinity**](V1VolumeNodeAffinity.md) |  | [optional] 
**persistent_volume_reclaim_policy** | **str** | persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming | [optional] 
**photon_persistent_disk** | [**V1PhotonPersistentDiskVolumeSource**](V1PhotonPersistentDiskVolumeSource.md) |  | [optional] 
**portworx_volume** | [**V1PortworxVolumeSource**](V1PortworxVolumeSource.md) |  | [optional] 
**quobyte** | [**V1QuobyteVolumeSource**](V1QuobyteVolumeSource.md) |  | [optional] 
**rbd** | [**V1RBDPersistentVolumeSource**](V1RBDPersistentVolumeSource.md) |  | [optional] 
**scale_io** | [**V1ScaleIOPersistentVolumeSource**](V1ScaleIOPersistentVolumeSource.md) |  | [optional] 
**storage_class_name** | **str** | storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. | [optional] 
**storageos** | [**V1StorageOSPersistentVolumeSource**](V1StorageOSPersistentVolumeSource.md) |  | [optional] 
**volume_attributes_class_name** | **str** | Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is a beta field and requires enabling VolumeAttributesClass feature (off by default). | [optional] 
**volume_mode** | **str** | volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. | [optional] 
**vsphere_volume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_persistent_volume_spec import V1PersistentVolumeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeSpec from a JSON string
v1_persistent_volume_spec_instance = V1PersistentVolumeSpec.from_json(json)
# print the JSON string representation of the object
print(V1PersistentVolumeSpec.to_json())

# convert the object into a dict
v1_persistent_volume_spec_dict = v1_persistent_volume_spec_instance.to_dict()
# create an instance of V1PersistentVolumeSpec from a dict
v1_persistent_volume_spec_from_dict = V1PersistentVolumeSpec.from_dict(v1_persistent_volume_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


