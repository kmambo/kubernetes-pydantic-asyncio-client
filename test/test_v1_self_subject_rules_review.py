# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_self_subject_rules_review import V1SelfSubjectRulesReview

class TestV1SelfSubjectRulesReview(unittest.TestCase):
    """V1SelfSubjectRulesReview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SelfSubjectRulesReview:
        """Test V1SelfSubjectRulesReview
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SelfSubjectRulesReview`
        """
        model = V1SelfSubjectRulesReview()
        if include_optional:
            return V1SelfSubjectRulesReview(
                api_version = '',
                kind = '',
                metadata = kubernetes_asyncio.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : ''
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        ''
                        ], 
                    generate_name = '', 
                    generation = 56, 
                    labels = {
                        'key' : ''
                        }, 
                    managed_fields = [
                        kubernetes_asyncio.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '', 
                            fields_type = '', 
                            fields_v1 = kubernetes_asyncio.client.models.fields_v1.fieldsV1(), 
                            manager = '', 
                            operation = '', 
                            subresource = '', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '', 
                    namespace = '', 
                    owner_references = [
                        kubernetes_asyncio.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '', 
                            name = '', 
                            uid = '', )
                        ], 
                    resource_version = '', 
                    self_link = '', 
                    uid = '', ),
                spec = kubernetes_asyncio.client.models.v1/self_subject_rules_review_spec.v1.SelfSubjectRulesReviewSpec(
                    namespace = '', ),
                status = kubernetes_asyncio.client.models.v1/subject_rules_review_status.v1.SubjectRulesReviewStatus(
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
                        ], )
            )
        else:
            return V1SelfSubjectRulesReview(
                spec = kubernetes_asyncio.client.models.v1/self_subject_rules_review_spec.v1.SelfSubjectRulesReviewSpec(
                    namespace = '', ),
        )
        """

    def testV1SelfSubjectRulesReview(self):
        """Test V1SelfSubjectRulesReview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
