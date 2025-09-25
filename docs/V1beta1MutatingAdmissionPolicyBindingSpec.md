# V1beta1MutatingAdmissionPolicyBindingSpec

MutatingAdmissionPolicyBindingSpec is the specification of the MutatingAdmissionPolicyBinding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_resources** | [**V1beta1MatchResources**](V1beta1MatchResources.md) | matchResources limits what resources match this binding and may be mutated by it. Note that if matchResources matches a resource, the resource must also match a policy&#39;s matchConstraints and matchConditions before the resource may be mutated. When matchResources is unset, it does not constrain resource matching, and only the policy&#39;s matchConstraints and matchConditions must match for the resource to be mutated. Additionally, matchResources.resourceRules are optional and do not constraint matching when unset. Note that this is differs from MutatingAdmissionPolicy matchConstraints, where resourceRules are required. The CREATE, UPDATE and CONNECT operations are allowed.  The DELETE operation may not be matched. &#39;*&#39; matches CREATE, UPDATE and CONNECT. | [optional] 
**param_ref** | [**V1beta1ParamRef**](V1beta1ParamRef.md) | paramRef specifies the parameter resource used to configure the admission control policy. It should point to a resource of the type specified in spec.ParamKind of the bound MutatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the MutatingAdmissionPolicy applied. If the policy does not specify a ParamKind then this field is ignored, and the rules are evaluated without a param. | [optional] 
**policy_name** | **str** | policyName references a MutatingAdmissionPolicy name which the MutatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1beta1_mutating_admission_policy_binding_spec import V1beta1MutatingAdmissionPolicyBindingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1MutatingAdmissionPolicyBindingSpec from a JSON string
v1beta1_mutating_admission_policy_binding_spec_instance = V1beta1MutatingAdmissionPolicyBindingSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1MutatingAdmissionPolicyBindingSpec.to_json())

# convert the object into a dict
v1beta1_mutating_admission_policy_binding_spec_dict = v1beta1_mutating_admission_policy_binding_spec_instance.to_dict()
# create an instance of V1beta1MutatingAdmissionPolicyBindingSpec from a dict
v1beta1_mutating_admission_policy_binding_spec_from_dict = V1beta1MutatingAdmissionPolicyBindingSpec.from_dict(v1beta1_mutating_admission_policy_binding_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


