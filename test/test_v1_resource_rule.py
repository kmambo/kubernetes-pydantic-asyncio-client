# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_resource_rule import V1ResourceRule

class TestV1ResourceRule(unittest.TestCase):
    """V1ResourceRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ResourceRule:
        """Test V1ResourceRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ResourceRule`
        """
        model = V1ResourceRule()
        if include_optional:
            return V1ResourceRule(
                api_groups = [
                    ''
                    ],
                resource_names = [
                    ''
                    ],
                resources = [
                    ''
                    ],
                verbs = [
                    ''
                    ]
            )
        else:
            return V1ResourceRule(
                verbs = [
                    ''
                    ],
        )
        """

    def testV1ResourceRule(self):
        """Test V1ResourceRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
