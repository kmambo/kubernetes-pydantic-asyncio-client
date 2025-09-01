# V1alpha1LeaseCandidateSpec

LeaseCandidateSpec is a specification of a Lease.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_version** | **str** | BinaryVersion is the binary version. It must be in a semver format without leading &#x60;v&#x60;. This field is required when strategy is \&quot;OldestEmulationVersion\&quot; | [optional] 
**emulation_version** | **str** | EmulationVersion is the emulation version. It must be in a semver format without leading &#x60;v&#x60;. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is \&quot;OldestEmulationVersion\&quot; | [optional] 
**lease_name** | **str** | LeaseName is the name of the lease for which this candidate is contending. This field is immutable. | [default to '']
**ping_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | [optional] 
**preferred_strategies** | **List[str]** | PreferredStrategies indicates the list of strategies for picking the leader for coordinated leader election. The list is ordered, and the first strategy supersedes all other strategies. The list is used by coordinated leader election to make a decision about the final election strategy. This follows as - If all clients have strategy X as the first element in this list, strategy X will be used. - If a candidate has strategy [X] and another candidate has strategy [Y, X], Y supersedes X and strategy Y   will be used. - If a candidate has strategy [X, Y] and another candidate has strategy [Y, X], this is a user error and leader   election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled. | 
**renew_time** | **datetime** | MicroTime is version of Time with microsecond level precision. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1alpha1_lease_candidate_spec import V1alpha1LeaseCandidateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1LeaseCandidateSpec from a JSON string
v1alpha1_lease_candidate_spec_instance = V1alpha1LeaseCandidateSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha1LeaseCandidateSpec.to_json())

# convert the object into a dict
v1alpha1_lease_candidate_spec_dict = v1alpha1_lease_candidate_spec_instance.to_dict()
# create an instance of V1alpha1LeaseCandidateSpec from a dict
v1alpha1_lease_candidate_spec_from_dict = V1alpha1LeaseCandidateSpec.from_dict(v1alpha1_lease_candidate_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


