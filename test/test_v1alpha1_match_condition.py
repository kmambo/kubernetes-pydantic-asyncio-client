# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1alpha1_match_condition import V1alpha1MatchCondition

class TestV1alpha1MatchCondition(unittest.TestCase):
    """V1alpha1MatchCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1MatchCondition:
        """Test V1alpha1MatchCondition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1MatchCondition`
        """
        model = V1alpha1MatchCondition()
        if include_optional:
            return V1alpha1MatchCondition(
                expression = '',
                name = ''
            )
        else:
            return V1alpha1MatchCondition(
                expression = '',
                name = '',
        )
        """

    def testV1alpha1MatchCondition(self):
        """Test V1alpha1MatchCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
