# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_validating_webhook_configuration import V1ValidatingWebhookConfiguration

class TestV1ValidatingWebhookConfiguration(unittest.TestCase):
    """V1ValidatingWebhookConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ValidatingWebhookConfiguration:
        """Test V1ValidatingWebhookConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ValidatingWebhookConfiguration`
        """
        model = V1ValidatingWebhookConfiguration()
        if include_optional:
            return V1ValidatingWebhookConfiguration(
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
                webhooks = [
                    kubernetes_asyncio.client.models.v1/validating_webhook.v1.ValidatingWebhook(
                        admission_review_versions = [
                            ''
                            ], 
                        kubernetes_asyncio.client_config = kubernetes_asyncio.client.models.admissionregistration/v1/webhook_client_config.admissionregistration.v1.WebhookClientConfig(
                            ca_bundle = 'YQ==', 
                            service = kubernetes_asyncio.client.models.admissionregistration/v1/service_reference.admissionregistration.v1.ServiceReference(
                                name = '', 
                                namespace = '', 
                                path = '', 
                                port = 56, ), 
                            url = '', ), 
                        failure_policy = '', 
                        match_conditions = [
                            kubernetes_asyncio.client.models.v1/match_condition.v1.MatchCondition(
                                expression = '', 
                                name = '', )
                            ], 
                        match_policy = '', 
                        name = '', 
                        namespace_selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                            match_expressions = [
                                kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                    key = '', 
                                    operator = '', 
                                    values = [
                                        ''
                                        ], )
                                ], 
                            match_labels = {
                                'key' : ''
                                }, ), 
                        object_selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(), 
                        rules = [
                            kubernetes_asyncio.client.models.v1/rule_with_operations.v1.RuleWithOperations(
                                api_groups = [
                                    ''
                                    ], 
                                api_versions = [
                                    ''
                                    ], 
                                operations = [
                                    ''
                                    ], 
                                resources = [
                                    ''
                                    ], 
                                scope = '', )
                            ], 
                        side_effects = '', 
                        timeout_seconds = 56, )
                    ]
            )
        else:
            return V1ValidatingWebhookConfiguration(
        )
        """

    def testV1ValidatingWebhookConfiguration(self):
        """Test V1ValidatingWebhookConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
