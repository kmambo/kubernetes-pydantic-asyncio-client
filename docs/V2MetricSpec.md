# V2MetricSpec

MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_resource** | [**V2ContainerResourceMetricSource**](V2ContainerResourceMetricSource.md) | containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \&quot;pods\&quot; source. | [optional] 
**external** | [**V2ExternalMetricSource**](V2ExternalMetricSource.md) | external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). | [optional] 
**object** | [**V2ObjectMetricSource**](V2ObjectMetricSource.md) | object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). | [optional] 
**pods** | [**V2PodsMetricSource**](V2PodsMetricSource.md) | pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. | [optional] 
**resource** | [**V2ResourceMetricSource**](V2ResourceMetricSource.md) | resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \&quot;pods\&quot; source. | [optional] 
**type** | **str** | type is the type of metric source.  It should be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each mapping to a matching field in the object. | [default to '']

## Example

```python
from kubernetes_asyncio.models.v2_metric_spec import V2MetricSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricSpec from a JSON string
v2_metric_spec_instance = V2MetricSpec.from_json(json)
# print the JSON string representation of the object
print(V2MetricSpec.to_json())

# convert the object into a dict
v2_metric_spec_dict = v2_metric_spec_instance.to_dict()
# create an instance of V2MetricSpec from a dict
v2_metric_spec_from_dict = V2MetricSpec.from_dict(v2_metric_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


