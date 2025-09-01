# V1CSIStorageCapacityCapacity

capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kubernetes_asyncio.models.v1_csi_storage_capacity_capacity import V1CSIStorageCapacityCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIStorageCapacityCapacity from a JSON string
v1_csi_storage_capacity_capacity_instance = V1CSIStorageCapacityCapacity.from_json(json)
# print the JSON string representation of the object
print(V1CSIStorageCapacityCapacity.to_json())

# convert the object into a dict
v1_csi_storage_capacity_capacity_dict = v1_csi_storage_capacity_capacity_instance.to_dict()
# create an instance of V1CSIStorageCapacityCapacity from a dict
v1_csi_storage_capacity_capacity_from_dict = V1CSIStorageCapacityCapacity.from_dict(v1_csi_storage_capacity_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


