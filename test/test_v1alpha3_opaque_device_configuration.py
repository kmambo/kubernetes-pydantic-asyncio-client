# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1alpha3_opaque_device_configuration import V1alpha3OpaqueDeviceConfiguration

class TestV1alpha3OpaqueDeviceConfiguration(unittest.TestCase):
    """V1alpha3OpaqueDeviceConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha3OpaqueDeviceConfiguration:
        """Test V1alpha3OpaqueDeviceConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha3OpaqueDeviceConfiguration`
        """
        model = V1alpha3OpaqueDeviceConfiguration()
        if include_optional:
            return V1alpha3OpaqueDeviceConfiguration(
                driver = '',
                parameters = kubernetes_asyncio.client.models.parameters.parameters()
            )
        else:
            return V1alpha3OpaqueDeviceConfiguration(
                driver = '',
                parameters = kubernetes_asyncio.client.models.parameters.parameters(),
        )
        """

    def testV1alpha3OpaqueDeviceConfiguration(self):
        """Test V1alpha3OpaqueDeviceConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
