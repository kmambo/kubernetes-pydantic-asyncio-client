# V1Subject

Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup holds the API group of the referenced subject. Defaults to \&quot;\&quot; for ServiceAccount subjects. Defaults to \&quot;rbac.authorization.k8s.io\&quot; for User and Group subjects. | [optional] 
**kind** | **str** | Kind of object being referenced. Values defined by this API group are \&quot;User\&quot;, \&quot;Group\&quot;, and \&quot;ServiceAccount\&quot;. If the Authorizer does not recognized the kind value, the Authorizer should report an error. | [default to '']
**name** | **str** | Name of the object being referenced. | [default to '']
**namespace** | **str** | Namespace of the referenced object.  If the object kind is non-namespace, such as \&quot;User\&quot; or \&quot;Group\&quot;, and this value is not empty the Authorizer should report an error. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_subject import V1Subject

# TODO update the JSON string below
json = "{}"
# create an instance of V1Subject from a JSON string
v1_subject_instance = V1Subject.from_json(json)
# print the JSON string representation of the object
print(V1Subject.to_json())

# convert the object into a dict
v1_subject_dict = v1_subject_instance.to_dict()
# create an instance of V1Subject from a dict
v1_subject_from_dict = V1Subject.from_dict(v1_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


