# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_node_swap_status import V1NodeSwapStatus

class TestV1NodeSwapStatus(unittest.TestCase):
    """V1NodeSwapStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1NodeSwapStatus:
        """Test V1NodeSwapStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1NodeSwapStatus`
        """
        model = V1NodeSwapStatus()
        if include_optional:
            return V1NodeSwapStatus(
                capacity = 56
            )
        else:
            return V1NodeSwapStatus(
        )
        """

    def testV1NodeSwapStatus(self):
        """Test V1NodeSwapStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
