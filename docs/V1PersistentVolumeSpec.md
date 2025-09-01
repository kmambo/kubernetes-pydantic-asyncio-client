# V1PersistentVolumeSpec

PersistentVolumeSpec is the specification of a persistent volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes | [optional] 
**aws_elastic_block_store** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) | awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore | [optional] 
**azure_disk** | [**V1AzureDiskVolumeSource**](V1AzureDiskVolumeSource.md) | azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. | [optional] 
**azure_file** | [**V1AzureFilePersistentVolumeSource**](V1AzureFilePersistentVolumeSource.md) | azureFile represents an Azure File Service mount on the host and bind mount to the pod. | [optional] 
**capacity** | [**Dict[str, V1PodSpecOverheadValue]**](V1PodSpecOverheadValue.md) | capacity is the description of the persistent volume&#39;s resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity | [optional] 
**cephfs** | [**V1CephFSPersistentVolumeSource**](V1CephFSPersistentVolumeSource.md) | cephFS represents a Ceph FS mount on the host that shares a pod&#39;s lifetime | [optional] 
**cinder** | [**V1CinderPersistentVolumeSource**](V1CinderPersistentVolumeSource.md) | cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | [optional] 
**claim_ref** | [**V1ObjectReference**](V1ObjectReference.md) | claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding | [optional] 
**csi** | [**V1CSIPersistentVolumeSource**](V1CSIPersistentVolumeSource.md) | csi represents storage that is handled by an external CSI driver (Beta feature). | [optional] 
**fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) | fc represents a Fibre Channel resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. | [optional] 
**flex_volume** | [**V1FlexPersistentVolumeSource**](V1FlexPersistentVolumeSource.md) | flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. | [optional] 
**flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) | flocker represents a Flocker volume attached to a kubelet&#39;s host machine and exposed to the pod for its usage. This depends on the Flocker control service being running | [optional] 
**gce_persistent_disk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) | gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk | [optional] 
**glusterfs** | [**V1GlusterfsPersistentVolumeSource**](V1GlusterfsPersistentVolumeSource.md) | glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md | [optional] 
**host_path** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) | hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | [optional] 
**iscsi** | [**V1ISCSIPersistentVolumeSource**](V1ISCSIPersistentVolumeSource.md) | iscsi represents an ISCSI Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. Provisioned by an admin. | [optional] 
**local** | [**V1LocalVolumeSource**](V1LocalVolumeSource.md) | local represents directly-attached storage with node affinity | [optional] 
**mount_options** | **List[str]** | mountOptions is the list of mount options, e.g. [\&quot;ro\&quot;, \&quot;soft\&quot;]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options | [optional] 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) | nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | [optional] 
**node_affinity** | [**V1VolumeNodeAffinity**](V1VolumeNodeAffinity.md) | nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume. | [optional] 
**persistent_volume_reclaim_policy** | **str** | persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming | [optional] 
**photon_persistent_disk** | [**V1PhotonPersistentDiskVolumeSource**](V1PhotonPersistentDiskVolumeSource.md) | photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine | [optional] 
**portworx_volume** | [**V1PortworxVolumeSource**](V1PortworxVolumeSource.md) | portworxVolume represents a portworx volume attached and mounted on kubelets host machine | [optional] 
**quobyte** | [**V1QuobyteVolumeSource**](V1QuobyteVolumeSource.md) | quobyte represents a Quobyte mount on the host that shares a pod&#39;s lifetime | [optional] 
**rbd** | [**V1RBDPersistentVolumeSource**](V1RBDPersistentVolumeSource.md) | rbd represents a Rados Block Device mount on the host that shares a pod&#39;s lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md | [optional] 
**scale_io** | [**V1ScaleIOPersistentVolumeSource**](V1ScaleIOPersistentVolumeSource.md) | scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. | [optional] 
**storage_class_name** | **str** | storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. | [optional] 
**storageos** | [**V1StorageOSPersistentVolumeSource**](V1StorageOSPersistentVolumeSource.md) | storageOS represents a StorageOS volume that is attached to the kubelet&#39;s host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md | [optional] 
**volume_attributes_class_name** | **str** | Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is an alpha field and requires enabling VolumeAttributesClass feature. | [optional] 
**volume_mode** | **str** | volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. | [optional] 
**vsphere_volume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) | vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_persistent_volume_spec import V1PersistentVolumeSpec

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


