# V2MetricStatus

MetricStatus describes the last-read state of a single metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_resource** | [**V2ContainerResourceMetricStatus**](V2ContainerResourceMetricStatus.md) | container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \&quot;pods\&quot; source. | [optional] 
**external** | [**V2ExternalMetricStatus**](V2ExternalMetricStatus.md) | external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). | [optional] 
**object** | [**V2ObjectMetricStatus**](V2ObjectMetricStatus.md) | object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). | [optional] 
**pods** | [**V2PodsMetricStatus**](V2PodsMetricStatus.md) | pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. | [optional] 
**resource** | [**V2ResourceMetricStatus**](V2ResourceMetricStatus.md) | resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \&quot;pods\&quot; source. | [optional] 
**type** | **str** | type is the type of metric source.  It will be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. | [default to '']

## Example

```python
from kubernetes_asyncio.models.v2_metric_status import V2MetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricStatus from a JSON string
v2_metric_status_instance = V2MetricStatus.from_json(json)
# print the JSON string representation of the object
print(V2MetricStatus.to_json())

# convert the object into a dict
v2_metric_status_dict = v2_metric_status_instance.to_dict()
# create an instance of V2MetricStatus from a dict
v2_metric_status_from_dict = V2MetricStatus.from_dict(v2_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


