# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_user_subject import V1UserSubject

class TestV1UserSubject(unittest.TestCase):
    """V1UserSubject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserSubject:
        """Test V1UserSubject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserSubject`
        """
        model = V1UserSubject()
        if include_optional:
            return V1UserSubject(
                name = ''
            )
        else:
            return V1UserSubject(
                name = '',
        )
        """

    def testV1UserSubject(self):
        """Test V1UserSubject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
