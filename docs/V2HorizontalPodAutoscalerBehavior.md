# V2HorizontalPodAutoscalerBehavior

HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_down** | [**V2HPAScalingRules**](V2HPAScalingRules.md) | scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used). | [optional] 
**scale_up** | [**V2HPAScalingRules**](V2HPAScalingRules.md) | scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:   * increase no more than 4 pods per 60 seconds   * double the number of pods per 60 seconds No stabilization is used. | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscalerBehavior from a JSON string
v2_horizontal_pod_autoscaler_behavior_instance = V2HorizontalPodAutoscalerBehavior.from_json(json)
# print the JSON string representation of the object
print(V2HorizontalPodAutoscalerBehavior.to_json())

# convert the object into a dict
v2_horizontal_pod_autoscaler_behavior_dict = v2_horizontal_pod_autoscaler_behavior_instance.to_dict()
# create an instance of V2HorizontalPodAutoscalerBehavior from a dict
v2_horizontal_pod_autoscaler_behavior_from_dict = V2HorizontalPodAutoscalerBehavior.from_dict(v2_horizontal_pod_autoscaler_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


