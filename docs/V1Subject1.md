# V1Subject1

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V1GroupSubject**](V1GroupSubject.md) | &#x60;group&#x60; matches based on user group name. | [optional] 
**kind** | **str** | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | [default to '']
**service_account** | [**V1ServiceAccountSubject**](V1ServiceAccountSubject.md) | &#x60;serviceAccount&#x60; matches ServiceAccounts. | [optional] 
**user** | [**V1UserSubject**](V1UserSubject.md) | &#x60;user&#x60; matches based on username. | [optional] 

## Example

```python
from kubernetes_asyncio.models.v1_subject1 import V1Subject1

# TODO update the JSON string below
json = "{}"
# create an instance of V1Subject1 from a JSON string
v1_subject1_instance = V1Subject1.from_json(json)
# print the JSON string representation of the object
print(V1Subject1.to_json())

# convert the object into a dict
v1_subject1_dict = v1_subject1_instance.to_dict()
# create an instance of V1Subject1 from a dict
v1_subject1_from_dict = V1Subject1.from_dict(v1_subject1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


