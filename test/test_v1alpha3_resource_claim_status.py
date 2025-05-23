# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1alpha3_resource_claim_status import V1alpha3ResourceClaimStatus

class TestV1alpha3ResourceClaimStatus(unittest.TestCase):
    """V1alpha3ResourceClaimStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha3ResourceClaimStatus:
        """Test V1alpha3ResourceClaimStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha3ResourceClaimStatus`
        """
        model = V1alpha3ResourceClaimStatus()
        if include_optional:
            return V1alpha3ResourceClaimStatus(
                allocation = kubernetes_asyncio.client.models.v1alpha3/allocation_result.v1alpha3.AllocationResult(
                    devices = kubernetes_asyncio.client.models.v1alpha3/device_allocation_result.v1alpha3.DeviceAllocationResult(
                        config = [
                            kubernetes_asyncio.client.models.v1alpha3/device_allocation_configuration.v1alpha3.DeviceAllocationConfiguration(
                                opaque = kubernetes_asyncio.client.models.v1alpha3/opaque_device_configuration.v1alpha3.OpaqueDeviceConfiguration(
                                    driver = '', 
                                    parameters = kubernetes_asyncio.client.models.parameters.parameters(), ), 
                                requests = [
                                    ''
                                    ], 
                                source = '', )
                            ], 
                        results = [
                            kubernetes_asyncio.client.models.v1alpha3/device_request_allocation_result.v1alpha3.DeviceRequestAllocationResult(
                                admin_access = True, 
                                device = '', 
                                driver = '', 
                                pool = '', 
                                request = '', 
                                tolerations = [
                                    kubernetes_asyncio.client.models.v1alpha3/device_toleration.v1alpha3.DeviceToleration(
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
                            ], ), ),
                devices = [
                    kubernetes_asyncio.client.models.v1alpha3/allocated_device_status.v1alpha3.AllocatedDeviceStatus(
                        conditions = [
                            kubernetes_asyncio.client.models.v1/condition.v1.Condition(
                                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                message = '', 
                                observed_generation = 56, 
                                reason = '', 
                                status = '', 
                                type = '', )
                            ], 
                        data = kubernetes_asyncio.client.models.data.data(), 
                        device = '', 
                        driver = '', 
                        network_data = kubernetes_asyncio.client.models.v1alpha3/network_device_data.v1alpha3.NetworkDeviceData(
                            hardware_address = '', 
                            interface_name = '', 
                            ips = [
                                ''
                                ], ), 
                        pool = '', )
                    ],
                reserved_for = [
                    kubernetes_asyncio.client.models.v1alpha3/resource_claim_consumer_reference.v1alpha3.ResourceClaimConsumerReference(
                        api_group = '', 
                        name = '', 
                        resource = '', 
                        uid = '', )
                    ]
            )
        else:
            return V1alpha3ResourceClaimStatus(
        )
        """

    def testV1alpha3ResourceClaimStatus(self):
        """Test V1alpha3ResourceClaimStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
