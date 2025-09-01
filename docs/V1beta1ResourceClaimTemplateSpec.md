# V1beta1ResourceClaimTemplateSpec

ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | ObjectMeta may contain labels and annotations that will be copied into the ResourceClaim when creating it. No other fields are allowed and will be rejected during validation. | [optional] 
**spec** | [**V1beta1ResourceClaimSpec**](V1beta1ResourceClaimSpec.md) | Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here. | 

## Example

```python
from kubernetes_asyncio.models.v1beta1_resource_claim_template_spec import V1beta1ResourceClaimTemplateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ResourceClaimTemplateSpec from a JSON string
v1beta1_resource_claim_template_spec_instance = V1beta1ResourceClaimTemplateSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1ResourceClaimTemplateSpec.to_json())

# convert the object into a dict
v1beta1_resource_claim_template_spec_dict = v1beta1_resource_claim_template_spec_instance.to_dict()
# create an instance of V1beta1ResourceClaimTemplateSpec from a dict
v1beta1_resource_claim_template_spec_from_dict = V1beta1ResourceClaimTemplateSpec.from_dict(v1beta1_resource_claim_template_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


