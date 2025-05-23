# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_validation_rule import V1ValidationRule

class TestV1ValidationRule(unittest.TestCase):
    """V1ValidationRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ValidationRule:
        """Test V1ValidationRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ValidationRule`
        """
        model = V1ValidationRule()
        if include_optional:
            return V1ValidationRule(
                field_path = '',
                message = '',
                message_expression = '',
                optional_old_self = True,
                reason = '',
                rule = ''
            )
        else:
            return V1ValidationRule(
                rule = '',
        )
        """

    def testV1ValidationRule(self):
        """Test V1ValidationRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
