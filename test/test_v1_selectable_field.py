# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_selectable_field import V1SelectableField

class TestV1SelectableField(unittest.TestCase):
    """V1SelectableField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SelectableField:
        """Test V1SelectableField
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SelectableField`
        """
        model = V1SelectableField()
        if include_optional:
            return V1SelectableField(
                json_path = ''
            )
        else:
            return V1SelectableField(
                json_path = '',
        )
        """

    def testV1SelectableField(self):
        """Test V1SelectableField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
