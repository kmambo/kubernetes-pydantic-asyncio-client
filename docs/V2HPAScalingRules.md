# V2HPAScalingRules

HPAScalingRules configures the scaling behavior for one direction via scaling Policy Rules and a configurable metric tolerance.  Scaling Policy Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen.  The tolerance is applied to the metric values and prevents scaling too eagerly for small metric variations. (Note that setting a tolerance requires enabling the alpha HPAConfigurableTolerance feature gate.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[V2HPAScalingPolicy]**](V2HPAScalingPolicy.md) | policies is a list of potential scaling polices which can be used during scaling. If not set, use the default values: - For scale up: allow doubling the number of pods, or an absolute change of 4 pods in a 15s window. - For scale down: allow all pods to be removed in a 15s window. | [optional] 
**select_policy** | **str** | selectPolicy is used to specify which policy should be used. If not set, the default value Max is used. | [optional] 
**stabilization_window_seconds** | **int** | stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). | [optional] 
**tolerance** | [**V2HPAScalingRulesTolerance**](V2HPAScalingRulesTolerance.md) |  | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v2_hpa_scaling_rules import V2HPAScalingRules

# TODO update the JSON string below
json = "{}"
# create an instance of V2HPAScalingRules from a JSON string
v2_hpa_scaling_rules_instance = V2HPAScalingRules.from_json(json)
# print the JSON string representation of the object
print(V2HPAScalingRules.to_json())

# convert the object into a dict
v2_hpa_scaling_rules_dict = v2_hpa_scaling_rules_instance.to_dict()
# create an instance of V2HPAScalingRules from a dict
v2_hpa_scaling_rules_from_dict = V2HPAScalingRules.from_dict(v2_hpa_scaling_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


