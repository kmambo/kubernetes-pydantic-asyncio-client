# V1CertificateSigningRequestSpec

CertificateSigningRequestSpec contains the certificate request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_seconds** | **int** | expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a kubernetes_asyncio.client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.  Certificate signers may not honor this field for various reasons:    1. Old signer that is unaware of the field (such as the in-tree      implementations prior to v1.22)   2. Signer whose configured maximum is shorter than the requested duration   3. Signer whose configured minimum is longer than the requested duration  The minimum valid value for expirationSeconds is 600, i.e. 10 minutes. | [optional] 
**extra** | **Dict[str, List[str]]** | extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. | [optional] 
**groups** | **List[str]** | groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. | [optional] 
**request** | **bytearray** | request contains an x509 certificate signing request encoded in a \&quot;CERTIFICATE REQUEST\&quot; PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded. | 
**signer_name** | **str** | signerName indicates the requested signer, and is a qualified name.  List/watch requests for CertificateSigningRequests can filter on this field using a \&quot;spec.signerName&#x3D;NAME\&quot; fieldSelector.  Well-known Kubernetes signers are:  1. \&quot;kubernetes.io/kube-apiserver-kubernetes_asyncio.client\&quot;: issues kubernetes_asyncio.client certificates that can be used to authenticate to kube-apiserver.   Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the \&quot;csrsigning\&quot; controller in kube-controller-manager.  2. \&quot;kubernetes.io/kube-apiserver-kubernetes_asyncio.client-kubelet\&quot;: issues kubernetes_asyncio.client certificates that kubelets use to authenticate to kube-apiserver.   Requests for this signer can be auto-approved by the \&quot;csrapproving\&quot; controller in kube-controller-manager, and can be issued by the \&quot;csrsigning\&quot; controller in kube-controller-manager.  3. \&quot;kubernetes.io/kubelet-serving\&quot; issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.   Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the \&quot;csrsigning\&quot; controller in kube-controller-manager.  More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers  Custom signerNames can also be specified. The signer defines:  1. Trust distribution: how trust (CA bundles) are distributed.  2. Permitted subjects: and behavior when a disallowed subject is requested.  3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.  4. Required, permitted, or forbidden key usages / extended key usages.  5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.  6. Whether or not requests for CA certificates are allowed. | 
**uid** | **str** | uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. | [optional] 
**usages** | **List[str]** | usages specifies a set of key usages requested in the issued certificate.  Requests for TLS kubernetes_asyncio.client certificates typically request: \&quot;digital signature\&quot;, \&quot;key encipherment\&quot;, \&quot;kubernetes_asyncio.client auth\&quot;.  Requests for TLS serving certificates typically request: \&quot;key encipherment\&quot;, \&quot;digital signature\&quot;, \&quot;server auth\&quot;.  Valid values are:  \&quot;signing\&quot;, \&quot;digital signature\&quot;, \&quot;content commitment\&quot;,  \&quot;key encipherment\&quot;, \&quot;key agreement\&quot;, \&quot;data encipherment\&quot;,  \&quot;cert sign\&quot;, \&quot;crl sign\&quot;, \&quot;encipher only\&quot;, \&quot;decipher only\&quot;, \&quot;any\&quot;,  \&quot;server auth\&quot;, \&quot;kubernetes_asyncio.client auth\&quot;,  \&quot;code signing\&quot;, \&quot;email protection\&quot;, \&quot;s/mime\&quot;,  \&quot;ipsec end system\&quot;, \&quot;ipsec tunnel\&quot;, \&quot;ipsec user\&quot;,  \&quot;timestamping\&quot;, \&quot;ocsp signing\&quot;, \&quot;microsoft sgc\&quot;, \&quot;netscape sgc\&quot; | [optional] 
**username** | **str** | username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable. | [optional] 

## Example

```python
from kubernetes_asyncio.client.models.v1_certificate_signing_request_spec import V1CertificateSigningRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1CertificateSigningRequestSpec from a JSON string
v1_certificate_signing_request_spec_instance = V1CertificateSigningRequestSpec.from_json(json)
# print the JSON string representation of the object
print(V1CertificateSigningRequestSpec.to_json())

# convert the object into a dict
v1_certificate_signing_request_spec_dict = v1_certificate_signing_request_spec_instance.to_dict()
# create an instance of V1CertificateSigningRequestSpec from a dict
v1_certificate_signing_request_spec_from_dict = V1CertificateSigningRequestSpec.from_dict(v1_certificate_signing_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


