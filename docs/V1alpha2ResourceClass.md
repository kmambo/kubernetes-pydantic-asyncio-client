# V1alpha2ResourceClass

ResourceClass is used by administrators to influence how resources are allocated.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**driver_name** | **str** | DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com). | [default to '']
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata | [optional] 
**parameters_ref** | [**V1alpha2ResourceClassParametersReference**](V1alpha2ResourceClassParametersReference.md) | ParametersRef references an arbitrary separate object that may hold parameters that will be used by the driver when allocating a resource that uses this class. A dynamic resource driver can distinguish between parameters stored here and and those stored in ResourceClaimSpec. | [optional] 
**structured_parameters** | **bool** | If and only if allocation of claims using this class is handled via structured parameters, then StructuredParameters must be set to true. | [optional] 
**suitable_nodes** | [**V1NodeSelector**](V1NodeSelector.md) | Only nodes matching the selector will be considered by the scheduler when trying to find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.  Setting this field is optional. If null, all nodes are candidates. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha2_resource_class import V1alpha2ResourceClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClass from a JSON string
v1alpha2_resource_class_instance = V1alpha2ResourceClass.from_json(json)
# print the JSON string representation of the object
print(V1alpha2ResourceClass.to_json())

# convert the object into a dict
v1alpha2_resource_class_dict = v1alpha2_resource_class_instance.to_dict()
# create an instance of V1alpha2ResourceClass from a dict
v1alpha2_resource_class_from_dict = V1alpha2ResourceClass.from_dict(v1alpha2_resource_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


