# V1VolumeProjection

Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_trust_bundle** | [**V1ClusterTrustBundleProjection**](V1ClusterTrustBundleProjection.md) | ClusterTrustBundle allows a pod to access the &#x60;.spec.trustBundle&#x60; field of ClusterTrustBundle objects in an auto-updating file.  Alpha, gated by the ClusterTrustBundleProjection feature gate.  ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.  Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time. | [optional] 
**config_map** | [**V1ConfigMapProjection**](V1ConfigMapProjection.md) | configMap information about the configMap data to project | [optional] 
**downward_api** | [**V1DownwardAPIProjection**](V1DownwardAPIProjection.md) | downwardAPI information about the downwardAPI data to project | [optional] 
**secret** | [**V1SecretProjection**](V1SecretProjection.md) | secret information about the secret data to project | [optional] 
**service_account_token** | [**V1ServiceAccountTokenProjection**](V1ServiceAccountTokenProjection.md) | serviceAccountToken is information about the serviceAccountToken data to project | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_volume_projection import V1VolumeProjection

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeProjection from a JSON string
v1_volume_projection_instance = V1VolumeProjection.from_json(json)
# print the JSON string representation of the object
print(V1VolumeProjection.to_json())

# convert the object into a dict
v1_volume_projection_dict = v1_volume_projection_instance.to_dict()
# create an instance of V1VolumeProjection from a dict
v1_volume_projection_from_dict = V1VolumeProjection.from_dict(v1_volume_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


