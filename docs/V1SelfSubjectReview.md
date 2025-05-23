# V1SelfSubjectReview

SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated.  If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes_asyncio.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**status** | [**V1SelfSubjectReviewStatus**](V1SelfSubjectReviewStatus.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_self_subject_review import V1SelfSubjectReview

# TODO update the JSON string below
json = "{}"
# create an instance of V1SelfSubjectReview from a JSON string
v1_self_subject_review_instance = V1SelfSubjectReview.from_json(json)
# print the JSON string representation of the object
print(V1SelfSubjectReview.to_json())

# convert the object into a dict
v1_self_subject_review_dict = v1_self_subject_review_instance.to_dict()
# create an instance of V1SelfSubjectReview from a dict
v1_self_subject_review_from_dict = V1SelfSubjectReview.from_dict(v1_self_subject_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


