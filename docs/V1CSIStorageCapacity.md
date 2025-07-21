# V1CSIStorageCapacity

CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this describes the available capacity in a particular topology segment.  This can be used when considering where to instantiate new PersistentVolumes.  For example this can express things like: - StorageClass \"standard\" has \"1234 GiB\" available in \"topology.kubernetes.io/zone=us-east1\" - StorageClass \"localssd\" has \"10 GiB\" available in \"kubernetes.io/hostname=knode-abc123\"  The following three cases all imply that no capacity is available for a certain combination: - no object exists with suitable topology and storage class name - such an object exists, but the capacity is unset - such an object exists, but the capacity is zero  The producer of these objects can decide which approach is more suitable.  They are consumed by the kube-scheduler when a CSI driver opts into capacity-aware scheduling with CSIDriverSpec.StorageCapacity. The scheduler compares the MaximumVolumeSize against the requested size of pending volumes to filter out unsuitable nodes. If MaximumVolumeSize is unset, it falls back to a comparison against the less precise Capacity. If that is also unset, the scheduler assumes that capacity is insufficient and tries some other node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**capacity** | [**V1CSIStorageCapacityCapacity**](V1CSIStorageCapacityCapacity.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**maximum_volume_size** | [**V1CSIStorageCapacityMaximumVolumeSize**](V1CSIStorageCapacityMaximumVolumeSize.md) |  | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. The name has no particular meaning. It must be a DNS subdomain (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on the cluster, the recommendation is to use csisc-&lt;uuid&gt;, a generated name, or a reverse-domain name which ends with the unique CSI driver name.  Objects are namespaced.  More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**node_topology** | [**V1LabelSelector**](V1LabelSelector.md) | nodeTopology defines which nodes have access to the storage for which capacity was reported. If not set, the storage is not accessible from any node in the cluster. If empty, the storage is accessible from all nodes. This field is immutable. | [optional] 
**storage_class_name** | **str** | storageClassName represents the name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable. | [default to '']

## Example

```python
from kubernetes_asyncio.models.v1_csi_storage_capacity import V1CSIStorageCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIStorageCapacity from a JSON string
v1_csi_storage_capacity_instance = V1CSIStorageCapacity.from_json(json)
# print the JSON string representation of the object
print(V1CSIStorageCapacity.to_json())

# convert the object into a dict
v1_csi_storage_capacity_dict = v1_csi_storage_capacity_instance.to_dict()
# create an instance of V1CSIStorageCapacity from a dict
v1_csi_storage_capacity_from_dict = V1CSIStorageCapacity.from_dict(v1_csi_storage_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


