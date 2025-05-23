# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_subject_rules_review_status import V1SubjectRulesReviewStatus

class TestV1SubjectRulesReviewStatus(unittest.TestCase):
    """V1SubjectRulesReviewStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SubjectRulesReviewStatus:
        """Test V1SubjectRulesReviewStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SubjectRulesReviewStatus`
        """
        model = V1SubjectRulesReviewStatus()
        if include_optional:
            return V1SubjectRulesReviewStatus(
                evaluation_error = '',
                incomplete = True,
                non_resource_rules = [
                    kubernetes_asyncio.client.models.v1/non_resource_rule.v1.NonResourceRule(
                        non_resource_urls = [
                            ''
                            ], 
                        verbs = [
                            ''
                            ], )
                    ],
                resource_rules = [
                    kubernetes_asyncio.client.models.v1/resource_rule.v1.ResourceRule(
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
                            ], )
                    ]
            )
        else:
            return V1SubjectRulesReviewStatus(
                incomplete = True,
                non_resource_rules = [
                    kubernetes_asyncio.client.models.v1/non_resource_rule.v1.NonResourceRule(
                        non_resource_urls = [
                            ''
                            ], 
                        verbs = [
                            ''
                            ], )
                    ],
                resource_rules = [
                    kubernetes_asyncio.client.models.v1/resource_rule.v1.ResourceRule(
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
                            ], )
                    ],
        )
        """

    def testV1SubjectRulesReviewStatus(self):
        """Test V1SubjectRulesReviewStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
