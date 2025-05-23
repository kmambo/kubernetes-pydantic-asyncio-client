# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v2_metric_identifier import V2MetricIdentifier

class TestV2MetricIdentifier(unittest.TestCase):
    """V2MetricIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2MetricIdentifier:
        """Test V2MetricIdentifier
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2MetricIdentifier`
        """
        model = V2MetricIdentifier()
        if include_optional:
            return V2MetricIdentifier(
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
                        }, )
            )
        else:
            return V2MetricIdentifier(
                name = '',
        )
        """

    def testV2MetricIdentifier(self):
        """Test V2MetricIdentifier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
