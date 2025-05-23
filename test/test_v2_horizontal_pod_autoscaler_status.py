# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus

class TestV2HorizontalPodAutoscalerStatus(unittest.TestCase):
    """V2HorizontalPodAutoscalerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2HorizontalPodAutoscalerStatus:
        """Test V2HorizontalPodAutoscalerStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2HorizontalPodAutoscalerStatus`
        """
        model = V2HorizontalPodAutoscalerStatus()
        if include_optional:
            return V2HorizontalPodAutoscalerStatus(
                conditions = [
                    kubernetes_asyncio.client.models.v2/horizontal_pod_autoscaler_condition.v2.HorizontalPodAutoscalerCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        status = '', 
                        type = '', )
                    ],
                current_metrics = [
                    kubernetes_asyncio.client.models.v2/metric_status.v2.MetricStatus(
                        container_resource = kubernetes_asyncio.client.models.v2/container_resource_metric_status.v2.ContainerResourceMetricStatus(
                            container = '', 
                            current = kubernetes_asyncio.client.models.v2/metric_value_status.v2.MetricValueStatus(
                                average_utilization = 56, 
                                average_value = '', 
                                value = '', ), 
                            name = '', ), 
                        external = kubernetes_asyncio.client.models.v2/external_metric_status.v2.ExternalMetricStatus(
                            current = kubernetes_asyncio.client.models.v2/metric_value_status.v2.MetricValueStatus(
                                average_utilization = 56, 
                                average_value = '', 
                                value = '', ), 
                            metric = kubernetes_asyncio.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                name = '', 
                                selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                                    match_expressions = [
                                        kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                            key = '', 
                                            operator = '', 
                                            values = [
                                                ''
                                                ], )
                                        ], 
                                    match_labels = {
                                        'key' : ''
                                        }, ), ), ), 
                        object = kubernetes_asyncio.client.models.v2/object_metric_status.v2.ObjectMetricStatus(
                            current = , 
                            described_object = kubernetes_asyncio.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                                api_version = '', 
                                kind = '', 
                                name = '', ), 
                            metric = kubernetes_asyncio.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                name = '', ), ), 
                        pods = kubernetes_asyncio.client.models.v2/pods_metric_status.v2.PodsMetricStatus(
                            current = , 
                            metric = , ), 
                        resource = kubernetes_asyncio.client.models.v2/resource_metric_status.v2.ResourceMetricStatus(
                            current = , 
                            name = '', ), 
                        type = '', )
                    ],
                current_replicas = 56,
                desired_replicas = 56,
                last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                observed_generation = 56
            )
        else:
            return V2HorizontalPodAutoscalerStatus(
                desired_replicas = 56,
        )
        """

    def testV2HorizontalPodAutoscalerStatus(self):
        """Test V2HorizontalPodAutoscalerStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
