# V1MatchResources

MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_resource_rules** | [**List[V1NamedRuleWithOperations]**](V1NamedRuleWithOperations.md) | ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded) | [optional] 
**match_policy** | **str** | matchPolicy defines how the \&quot;MatchResources\&quot; list is used to match incoming requests. Allowed values are \&quot;Exact\&quot; or \&quot;Equivalent\&quot;.  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but \&quot;rules\&quot; only included &#x60;apiGroups:[\&quot;apps\&quot;], apiVersions:[\&quot;v1\&quot;], resources: [\&quot;deployments\&quot;]&#x60;, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and \&quot;rules\&quot; only included &#x60;apiGroups:[\&quot;apps\&quot;], apiVersions:[\&quot;v1\&quot;], resources: [\&quot;deployments\&quot;]&#x60;, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.  Defaults to \&quot;Equivalent\&quot; | [optional] 
**namespace_selector** | [**V1LabelSelector**](V1LabelSelector.md) | NamespaceSelector decides whether to run the admission control policy on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the policy.  For example, to run the webhook on any objects whose namespace is not associated with \&quot;runlevel\&quot; of \&quot;0\&quot; or \&quot;1\&quot;;  you will set the selector as follows: \&quot;namespaceSelector\&quot;: {   \&quot;matchExpressions\&quot;: [     {       \&quot;key\&quot;: \&quot;runlevel\&quot;,       \&quot;operator\&quot;: \&quot;NotIn\&quot;,       \&quot;values\&quot;: [         \&quot;0\&quot;,         \&quot;1\&quot;       ]     }   ] }  If instead you want to only run the policy on any objects whose namespace is associated with the \&quot;environment\&quot; of \&quot;prod\&quot; or \&quot;staging\&quot;; you will set the selector as follows: \&quot;namespaceSelector\&quot;: {   \&quot;matchExpressions\&quot;: [     {       \&quot;key\&quot;: \&quot;environment\&quot;,       \&quot;operator\&quot;: \&quot;In\&quot;,       \&quot;values\&quot;: [         \&quot;prod\&quot;,         \&quot;staging\&quot;       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.  Default to the empty LabelSelector, which matches everything. | [optional] 
**object_selector** | [**V1LabelSelector**](V1LabelSelector.md) | ObjectSelector decides whether to run the validation based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the cel validation, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. | [optional] 
**resource_rules** | [**List[V1NamedRuleWithOperations]**](V1NamedRuleWithOperations.md) | ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_match_resources import V1MatchResources

# TODO update the JSON string below
json = "{}"
# create an instance of V1MatchResources from a JSON string
v1_match_resources_instance = V1MatchResources.from_json(json)
# print the JSON string representation of the object
print(V1MatchResources.to_json())

# convert the object into a dict
v1_match_resources_dict = v1_match_resources_instance.to_dict()
# create an instance of V1MatchResources from a dict
v1_match_resources_from_dict = V1MatchResources.from_dict(v1_match_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


