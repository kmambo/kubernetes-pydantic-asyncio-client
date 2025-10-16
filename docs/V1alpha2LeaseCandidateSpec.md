# V1alpha2LeaseCandidateSpec

LeaseCandidateSpec is a specification of a Lease.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_version** | **str** | BinaryVersion is the binary version. It must be in a semver format without leading &#x60;v&#x60;. This field is required. | [default to '']
**emulation_version** | **str** | EmulationVersion is the emulation version. It must be in a semver format without leading &#x60;v&#x60;. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is \&quot;OldestEmulationVersion\&quot; | [optional] 
**lease_name** | **str** | LeaseName is the name of the lease for which this candidate is contending. This field is immutable. | [default to '']
**ping_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | [optional] 
**renew_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | [optional] 
**strategy** | **str** | Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled. | 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1alpha2_lease_candidate_spec import V1alpha2LeaseCandidateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2LeaseCandidateSpec from a JSON string
v1alpha2_lease_candidate_spec_instance = V1alpha2LeaseCandidateSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha2LeaseCandidateSpec.to_json())

# convert the object into a dict
v1alpha2_lease_candidate_spec_dict = v1alpha2_lease_candidate_spec_instance.to_dict()
# create an instance of V1alpha2LeaseCandidateSpec from a dict
v1alpha2_lease_candidate_spec_from_dict = V1alpha2LeaseCandidateSpec.from_dict(v1alpha2_lease_candidate_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


