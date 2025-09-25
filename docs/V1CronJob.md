# V1CronJob

CronJob represents the configuration of a single cron job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata | [optional] 
**spec** | [**V1CronJobSpec**](V1CronJobSpec.md) | Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 
**status** | [**V1CronJobStatus**](V1CronJobStatus.md) | Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 

## Example

```python
from kubernetes_asyncio_pydantic.models.v1_cron_job import V1CronJob

# TODO update the JSON string below
json = "{}"
# create an instance of V1CronJob from a JSON string
v1_cron_job_instance = V1CronJob.from_json(json)
# print the JSON string representation of the object
print(V1CronJob.to_json())

# convert the object into a dict
v1_cron_job_dict = v1_cron_job_instance.to_dict()
# create an instance of V1CronJob from a dict
v1_cron_job_from_dict = V1CronJob.from_dict(v1_cron_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


