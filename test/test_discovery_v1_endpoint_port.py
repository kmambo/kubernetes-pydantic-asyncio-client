# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.discovery_v1_endpoint_port import DiscoveryV1EndpointPort

class TestDiscoveryV1EndpointPort(unittest.TestCase):
    """DiscoveryV1EndpointPort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscoveryV1EndpointPort:
        """Test DiscoveryV1EndpointPort
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscoveryV1EndpointPort`
        """
        model = DiscoveryV1EndpointPort()
        if include_optional:
            return DiscoveryV1EndpointPort(
                app_protocol = '',
                name = '',
                port = 56,
                protocol = ''
            )
        else:
            return DiscoveryV1EndpointPort(
        )
        """

    def testDiscoveryV1EndpointPort(self):
        """Test DiscoveryV1EndpointPort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
