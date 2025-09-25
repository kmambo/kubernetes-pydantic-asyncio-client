# V1ValidatingAdmissionPolicy

ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. | [optional] 
**spec** | [**V1ValidatingAdmissionPolicySpec**](V1ValidatingAdmissionPolicySpec.md) | Specification of the desired behavior of the ValidatingAdmissionPolicy. | [optional] 
**status** | [**V1ValidatingAdmissionPolicyStatus**](V1ValidatingAdmissionPolicyStatus.md) | The status of the ValidatingAdmissionPolicy, including warnings that are useful to determine if the policy behaves in the expected way. Populated by the system. Read-only. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_validating_admission_policy import V1ValidatingAdmissionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1ValidatingAdmissionPolicy from a JSON string
v1_validating_admission_policy_instance = V1ValidatingAdmissionPolicy.from_json(json)
# print the JSON string representation of the object
print(V1ValidatingAdmissionPolicy.to_json())

# convert the object into a dict
v1_validating_admission_policy_dict = v1_validating_admission_policy_instance.to_dict()
# create an instance of V1ValidatingAdmissionPolicy from a dict
v1_validating_admission_policy_from_dict = V1ValidatingAdmissionPolicy.from_dict(v1_validating_admission_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


