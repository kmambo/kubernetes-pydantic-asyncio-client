# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_custom_resource_definition_spec import V1CustomResourceDefinitionSpec

class TestV1CustomResourceDefinitionSpec(unittest.TestCase):
    """V1CustomResourceDefinitionSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CustomResourceDefinitionSpec:
        """Test V1CustomResourceDefinitionSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CustomResourceDefinitionSpec`
        """
        model = V1CustomResourceDefinitionSpec()
        if include_optional:
            return V1CustomResourceDefinitionSpec(
                conversion = kubernetes_asyncio.client.models.v1/custom_resource_conversion.v1.CustomResourceConversion(
                    strategy = '', 
                    webhook = kubernetes_asyncio.client.models.v1/webhook_conversion.v1.WebhookConversion(
                        kubernetes_asyncio.client_config = kubernetes_asyncio.client.models.apiextensions/v1/webhook_client_config.apiextensions.v1.WebhookClientConfig(
                            ca_bundle = 'YQ==', 
                            service = kubernetes_asyncio.client.models.apiextensions/v1/service_reference.apiextensions.v1.ServiceReference(
                                name = '', 
                                namespace = '', 
                                path = '', 
                                port = 56, ), 
                            url = '', ), 
                        conversion_review_versions = [
                            ''
                            ], ), ),
                group = '',
                names = kubernetes_asyncio.client.models.v1/custom_resource_definition_names.v1.CustomResourceDefinitionNames(
                    categories = [
                        ''
                        ], 
                    kind = '', 
                    list_kind = '', 
                    plural = '', 
                    short_names = [
                        ''
                        ], 
                    singular = '', ),
                preserve_unknown_fields = True,
                scope = '',
                versions = [
                    kubernetes_asyncio.client.models.v1/custom_resource_definition_version.v1.CustomResourceDefinitionVersion(
                        additional_printer_columns = [
                            kubernetes_asyncio.client.models.v1/custom_resource_column_definition.v1.CustomResourceColumnDefinition(
                                description = '', 
                                format = '', 
                                json_path = '', 
                                name = '', 
                                priority = 56, 
                                type = '', )
                            ], 
                        deprecated = True, 
                        deprecation_warning = '', 
                        name = '', 
                        schema = kubernetes_asyncio.client.models.v1/custom_resource_validation.v1.CustomResourceValidation(
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
                                    ], ), ), 
                        selectable_fields = [
                            kubernetes_asyncio.client.models.v1/selectable_field.v1.SelectableField(
                                json_path = '', )
                            ], 
                        served = True, 
                        storage = True, 
                        subresources = kubernetes_asyncio.client.models.v1/custom_resource_subresources.v1.CustomResourceSubresources(
                            scale = kubernetes_asyncio.client.models.v1/custom_resource_subresource_scale.v1.CustomResourceSubresourceScale(
                                label_selector_path = '', 
                                spec_replicas_path = '', 
                                status_replicas_path = '', ), 
                            status = kubernetes_asyncio.client.models.status.status(), ), )
                    ]
            )
        else:
            return V1CustomResourceDefinitionSpec(
                group = '',
                names = kubernetes_asyncio.client.models.v1/custom_resource_definition_names.v1.CustomResourceDefinitionNames(
                    categories = [
                        ''
                        ], 
                    kind = '', 
                    list_kind = '', 
                    plural = '', 
                    short_names = [
                        ''
                        ], 
                    singular = '', ),
                scope = '',
                versions = [
                    kubernetes_asyncio.client.models.v1/custom_resource_definition_version.v1.CustomResourceDefinitionVersion(
                        additional_printer_columns = [
                            kubernetes_asyncio.client.models.v1/custom_resource_column_definition.v1.CustomResourceColumnDefinition(
                                description = '', 
                                format = '', 
                                json_path = '', 
                                name = '', 
                                priority = 56, 
                                type = '', )
                            ], 
                        deprecated = True, 
                        deprecation_warning = '', 
                        name = '', 
                        schema = kubernetes_asyncio.client.models.v1/custom_resource_validation.v1.CustomResourceValidation(
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
                                    ], ), ), 
                        selectable_fields = [
                            kubernetes_asyncio.client.models.v1/selectable_field.v1.SelectableField(
                                json_path = '', )
                            ], 
                        served = True, 
                        storage = True, 
                        subresources = kubernetes_asyncio.client.models.v1/custom_resource_subresources.v1.CustomResourceSubresources(
                            scale = kubernetes_asyncio.client.models.v1/custom_resource_subresource_scale.v1.CustomResourceSubresourceScale(
                                label_selector_path = '', 
                                spec_replicas_path = '', 
                                status_replicas_path = '', ), 
                            status = kubernetes_asyncio.client.models.status.status(), ), )
                    ],
        )
        """

    def testV1CustomResourceDefinitionSpec(self):
        """Test V1CustomResourceDefinitionSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
