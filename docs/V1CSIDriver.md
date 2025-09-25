# V1CSIDriver

CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster. Kubernetes attach detach controller uses this object to determine whether attach is required. Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver objects are non-namespaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata. metadata.Name indicates the name of the CSI driver that this object refers to; it MUST be the same name returned by the CSI GetPluginName() call for that driver. The driver name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1CSIDriverSpec**](V1CSIDriverSpec.md) | spec represents the specification of the CSI Driver. | 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_csi_driver import V1CSIDriver

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIDriver from a JSON string
v1_csi_driver_instance = V1CSIDriver.from_json(json)
# print the JSON string representation of the object
print(V1CSIDriver.to_json())

# convert the object into a dict
v1_csi_driver_dict = v1_csi_driver_instance.to_dict()
# create an instance of V1CSIDriver from a dict
v1_csi_driver_from_dict = V1CSIDriver.from_dict(v1_csi_driver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


