# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration

class TestV1beta2OpaqueDeviceConfiguration(unittest.TestCase):
    """V1beta2OpaqueDeviceConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta2OpaqueDeviceConfiguration:
        """Test V1beta2OpaqueDeviceConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta2OpaqueDeviceConfiguration`
        """
        model = V1beta2OpaqueDeviceConfiguration()
        if include_optional:
            return V1beta2OpaqueDeviceConfiguration(
                driver = '',
                parameters = kubernetes_asyncio.client.models.parameters.parameters()
            )
        else:
            return V1beta2OpaqueDeviceConfiguration(
                driver = '',
                parameters = kubernetes_asyncio.client.models.parameters.parameters(),
        )
        """

    def testV1beta2OpaqueDeviceConfiguration(self):
        """Test V1beta2OpaqueDeviceConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
