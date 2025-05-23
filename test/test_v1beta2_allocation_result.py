# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1beta2_allocation_result import V1beta2AllocationResult

class TestV1beta2AllocationResult(unittest.TestCase):
    """V1beta2AllocationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta2AllocationResult:
        """Test V1beta2AllocationResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta2AllocationResult`
        """
        model = V1beta2AllocationResult()
        if include_optional:
            return V1beta2AllocationResult(
                devices = kubernetes_asyncio.client.models.v1beta2/device_allocation_result.v1beta2.DeviceAllocationResult(
                    config = [
                        kubernetes_asyncio.client.models.v1beta2/device_allocation_configuration.v1beta2.DeviceAllocationConfiguration(
                            opaque = kubernetes_asyncio.client.models.v1beta2/opaque_device_configuration.v1beta2.OpaqueDeviceConfiguration(
                                driver = '', 
                                parameters = kubernetes_asyncio.client.models.parameters.parameters(), ), 
                            requests = [
                                ''
                                ], 
                            source = '', )
                        ], 
                    results = [
                        kubernetes_asyncio.client.models.v1beta2/device_request_allocation_result.v1beta2.DeviceRequestAllocationResult(
                            admin_access = True, 
                            device = '', 
                            driver = '', 
                            pool = '', 
                            request = '', 
                            tolerations = [
                                kubernetes_asyncio.client.models.v1beta2/device_toleration.v1beta2.DeviceToleration(
                                    effect = '', 
                                    key = '', 
                                    operator = '', 
                                    toleration_seconds = 56, 
                                    value = '', )
                                ], )
                        ], ),
                node_selector = kubernetes_asyncio.client.models.v1/node_selector.v1.NodeSelector(
                    node_selector_terms = [
                        kubernetes_asyncio.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                            match_expressions = [
                                kubernetes_asyncio.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '', 
                                    operator = '', 
                                    values = [
                                        ''
                                        ], )
                                ], 
                            match_fields = [
                                kubernetes_asyncio.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '', 
                                    operator = '', )
                                ], )
                        ], )
            )
        else:
            return V1beta2AllocationResult(
        )
        """

    def testV1beta2AllocationResult(self):
        """Test V1beta2AllocationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
