# V1CSIStorageCapacityMaximumVolumeSize

maximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1_csi_storage_capacity_maximum_volume_size import V1CSIStorageCapacityMaximumVolumeSize

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIStorageCapacityMaximumVolumeSize from a JSON string
v1_csi_storage_capacity_maximum_volume_size_instance = V1CSIStorageCapacityMaximumVolumeSize.from_json(json)
# print the JSON string representation of the object
print(V1CSIStorageCapacityMaximumVolumeSize.to_json())

# convert the object into a dict
v1_csi_storage_capacity_maximum_volume_size_dict = v1_csi_storage_capacity_maximum_volume_size_instance.to_dict()
# create an instance of V1CSIStorageCapacityMaximumVolumeSize from a dict
v1_csi_storage_capacity_maximum_volume_size_from_dict = V1CSIStorageCapacityMaximumVolumeSize.from_dict(v1_csi_storage_capacity_maximum_volume_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


