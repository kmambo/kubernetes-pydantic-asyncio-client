# V1alpha1PodCertificateRequestStatus

PodCertificateRequestStatus describes the status of the request, and holds the certificate data if the request is issued.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_refresh_at** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**certificate_chain** | **str** | certificateChain is populated with an issued certificate by the signer. This field is set via the /status subresource. Once populated, this field is immutable.  If the certificate signing request is denied, a condition of type \&quot;Denied\&quot; is added and this field remains empty. If the signer cannot issue the certificate, a condition of type \&quot;Failed\&quot; is added and this field remains empty.  Validation requirements:  1. certificateChain must consist of one or more PEM-formatted certificates.  2. Each entry must be a valid PEM-wrapped, DER-encoded ASN.1 Certificate as     described in section 4 of RFC5280.  If more than one block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.  When projecting the chain into a pod volume, kubelet will drop any data in-between the PEM blocks, as well as any PEM block headers. | [optional] 
**conditions** | [**List[V1Condition]**](V1Condition.md) | conditions applied to the request.  The types \&quot;Issued\&quot;, \&quot;Denied\&quot;, and \&quot;Failed\&quot; have special handling.  At most one of these conditions may be present, and they must have status \&quot;True\&quot;.  If the request is denied with &#x60;Reason&#x3D;UnsupportedKeyType&#x60;, the signer may suggest a key type that will work in the message field. | [optional] 
**not_after** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**not_before** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1alpha1_pod_certificate_request_status import V1alpha1PodCertificateRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1PodCertificateRequestStatus from a JSON string
v1alpha1_pod_certificate_request_status_instance = V1alpha1PodCertificateRequestStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha1PodCertificateRequestStatus.to_json())

# convert the object into a dict
v1alpha1_pod_certificate_request_status_dict = v1alpha1_pod_certificate_request_status_instance.to_dict()
# create an instance of V1alpha1PodCertificateRequestStatus from a dict
v1alpha1_pod_certificate_request_status_from_dict = V1alpha1PodCertificateRequestStatus.from_dict(v1alpha1_pod_certificate_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


