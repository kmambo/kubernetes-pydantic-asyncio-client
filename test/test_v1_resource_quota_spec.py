# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_resource_quota_spec import V1ResourceQuotaSpec

class TestV1ResourceQuotaSpec(unittest.TestCase):
    """V1ResourceQuotaSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ResourceQuotaSpec:
        """Test V1ResourceQuotaSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ResourceQuotaSpec`
        """
        model = V1ResourceQuotaSpec()
        if include_optional:
            return V1ResourceQuotaSpec(
                hard = {
                    'key' : ''
                    },
                scope_selector = kubernetes_asyncio.client.models.v1/scope_selector.v1.ScopeSelector(
                    match_expressions = [
                        kubernetes_asyncio.client.models.v1/scoped_resource_selector_requirement.v1.ScopedResourceSelectorRequirement(
                            operator = '', 
                            scope_name = '', 
                            values = [
                                ''
                                ], )
                        ], ),
                scopes = [
                    ''
                    ]
            )
        else:
            return V1ResourceQuotaSpec(
        )
        """

    def testV1ResourceQuotaSpec(self):
        """Test V1ResourceQuotaSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
