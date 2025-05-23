# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1alpha1_mutating_admission_policy_binding_spec import V1alpha1MutatingAdmissionPolicyBindingSpec

class TestV1alpha1MutatingAdmissionPolicyBindingSpec(unittest.TestCase):
    """V1alpha1MutatingAdmissionPolicyBindingSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1MutatingAdmissionPolicyBindingSpec:
        """Test V1alpha1MutatingAdmissionPolicyBindingSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1MutatingAdmissionPolicyBindingSpec`
        """
        model = V1alpha1MutatingAdmissionPolicyBindingSpec()
        if include_optional:
            return V1alpha1MutatingAdmissionPolicyBindingSpec(
                match_resources = kubernetes_asyncio.client.models.v1alpha1/match_resources.v1alpha1.MatchResources(
                    exclude_resource_rules = [
                        kubernetes_asyncio.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
                            api_groups = [
                                ''
                                ], 
                            api_versions = [
                                ''
                                ], 
                            operations = [
                                ''
                                ], 
                            resource_names = [
                                ''
                                ], 
                            resources = [
                                ''
                                ], 
                            scope = '', )
                        ], 
                    match_policy = '', 
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
                    resource_rules = [
                        kubernetes_asyncio.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
                            scope = '', )
                        ], ),
                param_ref = kubernetes_asyncio.client.models.v1alpha1/param_ref.v1alpha1.ParamRef(
                    name = '', 
                    namespace = '', 
                    parameter_not_found_action = '', 
                    selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
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
                            }, ), ),
                policy_name = ''
            )
        else:
            return V1alpha1MutatingAdmissionPolicyBindingSpec(
        )
        """

    def testV1alpha1MutatingAdmissionPolicyBindingSpec(self):
        """Test V1alpha1MutatingAdmissionPolicyBindingSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
