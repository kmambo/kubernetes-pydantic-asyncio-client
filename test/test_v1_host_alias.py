# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_host_alias import V1HostAlias

class TestV1HostAlias(unittest.TestCase):
    """V1HostAlias unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1HostAlias:
        """Test V1HostAlias
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1HostAlias`
        """
        model = V1HostAlias()
        if include_optional:
            return V1HostAlias(
                hostnames = [
                    ''
                    ],
                ip = ''
            )
        else:
            return V1HostAlias(
                ip = '',
        )
        """

    def testV1HostAlias(self):
        """Test V1HostAlias"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
