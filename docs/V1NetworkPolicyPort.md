# V1NetworkPolicyPort

NetworkPolicyPort describes a port to allow traffic on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_port** | **int** | endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port. | [optional] 
**port** | **object** | port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. | [optional] 
**protocol** | **str** | protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_network_policy_port import V1NetworkPolicyPort

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicyPort from a JSON string
v1_network_policy_port_instance = V1NetworkPolicyPort.from_json(json)
# print the JSON string representation of the object
print(V1NetworkPolicyPort.to_json())

# convert the object into a dict
v1_network_policy_port_dict = v1_network_policy_port_instance.to_dict()
# create an instance of V1NetworkPolicyPort from a dict
v1_network_policy_port_from_dict = V1NetworkPolicyPort.from_dict(v1_network_policy_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


