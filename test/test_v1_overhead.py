# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_overhead import V1Overhead

class TestV1Overhead(unittest.TestCase):
    """V1Overhead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1Overhead:
        """Test V1Overhead
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1Overhead`
        """
        model = V1Overhead()
        if include_optional:
            return V1Overhead(
                pod_fixed = {
                    'key' : ''
                    }
            )
        else:
            return V1Overhead(
        )
        """

    def testV1Overhead(self):
        """Test V1Overhead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
