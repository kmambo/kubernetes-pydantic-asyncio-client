# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_container_port import V1ContainerPort

class TestV1ContainerPort(unittest.TestCase):
    """V1ContainerPort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ContainerPort:
        """Test V1ContainerPort
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ContainerPort`
        """
        model = V1ContainerPort()
        if include_optional:
            return V1ContainerPort(
                container_port = 56,
                host_ip = '',
                host_port = 56,
                name = '',
                protocol = ''
            )
        else:
            return V1ContainerPort(
                container_port = 56,
        )
        """

    def testV1ContainerPort(self):
        """Test V1ContainerPort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
