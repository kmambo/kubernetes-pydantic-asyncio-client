# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v2_external_metric_source import V2ExternalMetricSource

class TestV2ExternalMetricSource(unittest.TestCase):
    """V2ExternalMetricSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2ExternalMetricSource:
        """Test V2ExternalMetricSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2ExternalMetricSource`
        """
        model = V2ExternalMetricSource()
        if include_optional:
            return V2ExternalMetricSource(
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
                            }, ), ),
                target = kubernetes_asyncio.client.models.v2/metric_target.v2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '', 
                    type = '', 
                    value = '', )
            )
        else:
            return V2ExternalMetricSource(
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
                            }, ), ),
                target = kubernetes_asyncio.client.models.v2/metric_target.v2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '', 
                    type = '', 
                    value = '', ),
        )
        """

    def testV2ExternalMetricSource(self):
        """Test V2ExternalMetricSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
