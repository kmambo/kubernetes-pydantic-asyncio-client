# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_custom_resource_validation import V1CustomResourceValidation

class TestV1CustomResourceValidation(unittest.TestCase):
    """V1CustomResourceValidation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CustomResourceValidation:
        """Test V1CustomResourceValidation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CustomResourceValidation`
        """
        model = V1CustomResourceValidation()
        if include_optional:
            return V1CustomResourceValidation(
                open_apiv3_schema = kubernetes_asyncio.client.models.v1/json_schema_props.v1.JSONSchemaProps(
                    __ref = '', 
                    __schema = '', 
                    additional_items = kubernetes_asyncio.client.models.additional_items.additionalItems(), 
                    additional_properties = kubernetes_asyncio.client.models.additional_properties.additionalProperties(), 
                    all_of = [
                        kubernetes_asyncio.client.models.v1/json_schema_props.v1.JSONSchemaProps(
                            __ref = '', 
                            __schema = '', 
                            additional_items = kubernetes_asyncio.client.models.additional_items.additionalItems(), 
                            additional_properties = kubernetes_asyncio.client.models.additional_properties.additionalProperties(), 
                            any_of = [
                                
                                ], 
                            default = kubernetes_asyncio.client.models.default.default(), 
                            definitions = {
                                'key' : 
                                }, 
                            dependencies = {
                                'key' : None
                                }, 
                            description = '', 
                            enum = [
                                None
                                ], 
                            example = kubernetes_asyncio.client.models.example.example(), 
                            exclusive_maximum = True, 
                            exclusive_minimum = True, 
                            external_docs = kubernetes_asyncio.client.models.v1/external_documentation.v1.ExternalDocumentation(
                                description = '', 
                                url = '', ), 
                            format = '', 
                            id = '', 
                            items = kubernetes_asyncio.client.models.items.items(), 
                            max_items = 56, 
                            max_length = 56, 
                            max_properties = 56, 
                            maximum = 1.337, 
                            min_items = 56, 
                            min_length = 56, 
                            min_properties = 56, 
                            minimum = 1.337, 
                            multiple_of = 1.337, 
                            not = , 
                            nullable = True, 
                            one_of = [
                                
                                ], 
                            pattern = '', 
                            pattern_properties = {
                                'key' : 
                                }, 
                            properties = {
                                'key' : 
                                }, 
                            required = [
                                ''
                                ], 
                            title = '', 
                            type = '', 
                            unique_items = True, 
                            x_kubernetes_embedded_resource = True, 
                            x_kubernetes_int_or_string = True, 
                            x_kubernetes_list_map_keys = [
                                ''
                                ], 
                            x_kubernetes_list_type = '', 
                            x_kubernetes_map_type = '', 
                            x_kubernetes_preserve_unknown_fields = True, 
                            x_kubernetes_validations = [
                                kubernetes_asyncio.client.models.v1/validation_rule.v1.ValidationRule(
                                    field_path = '', 
                                    message = '', 
                                    message_expression = '', 
                                    optional_old_self = True, 
                                    reason = '', 
                                    rule = '', )
                                ], )
                        ], 
                    any_of = [
                        
                        ], 
                    default = kubernetes_asyncio.client.models.default.default(), 
                    definitions = {
                        'key' : 
                        }, 
                    dependencies = {
                        'key' : None
                        }, 
                    description = '', 
                    enum = [
                        None
                        ], 
                    example = kubernetes_asyncio.client.models.example.example(), 
                    exclusive_maximum = True, 
                    exclusive_minimum = True, 
                    external_docs = kubernetes_asyncio.client.models.v1/external_documentation.v1.ExternalDocumentation(
                        description = '', 
                        url = '', ), 
                    format = '', 
                    id = '', 
                    items = kubernetes_asyncio.client.models.items.items(), 
                    max_items = 56, 
                    max_length = 56, 
                    max_properties = 56, 
                    maximum = 1.337, 
                    min_items = 56, 
                    min_length = 56, 
                    min_properties = 56, 
                    minimum = 1.337, 
                    multiple_of = 1.337, 
                    not = , 
                    nullable = True, 
                    one_of = [
                        
                        ], 
                    pattern = '', 
                    pattern_properties = {
                        'key' : 
                        }, 
                    properties = {
                        'key' : 
                        }, 
                    required = [
                        ''
                        ], 
                    title = '', 
                    type = '', 
                    unique_items = True, 
                    x_kubernetes_embedded_resource = True, 
                    x_kubernetes_int_or_string = True, 
                    x_kubernetes_list_map_keys = [
                        ''
                        ], 
                    x_kubernetes_list_type = '', 
                    x_kubernetes_map_type = '', 
                    x_kubernetes_preserve_unknown_fields = True, 
                    x_kubernetes_validations = [
                        kubernetes_asyncio.client.models.v1/validation_rule.v1.ValidationRule(
                            field_path = '', 
                            message = '', 
                            message_expression = '', 
                            optional_old_self = True, 
                            reason = '', 
                            rule = '', )
                        ], )
            )
        else:
            return V1CustomResourceValidation(
        )
        """

    def testV1CustomResourceValidation(self):
        """Test V1CustomResourceValidation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
