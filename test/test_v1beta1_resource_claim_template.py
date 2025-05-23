# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1beta1_resource_claim_template import V1beta1ResourceClaimTemplate

class TestV1beta1ResourceClaimTemplate(unittest.TestCase):
    """V1beta1ResourceClaimTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1ResourceClaimTemplate:
        """Test V1beta1ResourceClaimTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1ResourceClaimTemplate`
        """
        model = V1beta1ResourceClaimTemplate()
        if include_optional:
            return V1beta1ResourceClaimTemplate(
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
                spec = kubernetes_asyncio.client.models.v1beta1/resource_claim_template_spec.v1beta1.ResourceClaimTemplateSpec(
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
                    spec = kubernetes_asyncio.client.models.v1beta1/resource_claim_spec.v1beta1.ResourceClaimSpec(
                        devices = kubernetes_asyncio.client.models.v1beta1/device_claim.v1beta1.DeviceClaim(
                            config = [
                                kubernetes_asyncio.client.models.v1beta1/device_claim_configuration.v1beta1.DeviceClaimConfiguration(
                                    opaque = kubernetes_asyncio.client.models.v1beta1/opaque_device_configuration.v1beta1.OpaqueDeviceConfiguration(
                                        driver = '', 
                                        parameters = kubernetes_asyncio.client.models.parameters.parameters(), ), 
                                    requests = [
                                        ''
                                        ], )
                                ], 
                            constraints = [
                                kubernetes_asyncio.client.models.v1beta1/device_constraint.v1beta1.DeviceConstraint(
                                    match_attribute = '', )
                                ], 
                            requests = [
                                kubernetes_asyncio.client.models.v1beta1/device_request.v1beta1.DeviceRequest(
                                    admin_access = True, 
                                    allocation_mode = '', 
                                    count = 56, 
                                    device_class_name = '', 
                                    first_available = [
                                        kubernetes_asyncio.client.models.v1beta1/device_sub_request.v1beta1.DeviceSubRequest(
                                            allocation_mode = '', 
                                            count = 56, 
                                            device_class_name = '', 
                                            name = '', 
                                            selectors = [
                                                kubernetes_asyncio.client.models.v1beta1/device_selector.v1beta1.DeviceSelector(
                                                    cel = kubernetes_asyncio.client.models.v1beta1/cel_device_selector.v1beta1.CELDeviceSelector(
                                                        expression = '', ), )
                                                ], 
                                            tolerations = [
                                                kubernetes_asyncio.client.models.v1beta1/device_toleration.v1beta1.DeviceToleration(
                                                    effect = '', 
                                                    key = '', 
                                                    operator = '', 
                                                    toleration_seconds = 56, 
                                                    value = '', )
                                                ], )
                                        ], 
                                    name = '', 
                                    selectors = [
                                        kubernetes_asyncio.client.models.v1beta1/device_selector.v1beta1.DeviceSelector()
                                        ], 
                                    tolerations = [
                                        kubernetes_asyncio.client.models.v1beta1/device_toleration.v1beta1.DeviceToleration(
                                            effect = '', 
                                            key = '', 
                                            operator = '', 
                                            toleration_seconds = 56, 
                                            value = '', )
                                        ], )
                                ], ), ), )
            )
        else:
            return V1beta1ResourceClaimTemplate(
                spec = kubernetes_asyncio.client.models.v1beta1/resource_claim_template_spec.v1beta1.ResourceClaimTemplateSpec(
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
                    spec = kubernetes_asyncio.client.models.v1beta1/resource_claim_spec.v1beta1.ResourceClaimSpec(
                        devices = kubernetes_asyncio.client.models.v1beta1/device_claim.v1beta1.DeviceClaim(
                            config = [
                                kubernetes_asyncio.client.models.v1beta1/device_claim_configuration.v1beta1.DeviceClaimConfiguration(
                                    opaque = kubernetes_asyncio.client.models.v1beta1/opaque_device_configuration.v1beta1.OpaqueDeviceConfiguration(
                                        driver = '', 
                                        parameters = kubernetes_asyncio.client.models.parameters.parameters(), ), 
                                    requests = [
                                        ''
                                        ], )
                                ], 
                            constraints = [
                                kubernetes_asyncio.client.models.v1beta1/device_constraint.v1beta1.DeviceConstraint(
                                    match_attribute = '', )
                                ], 
                            requests = [
                                kubernetes_asyncio.client.models.v1beta1/device_request.v1beta1.DeviceRequest(
                                    admin_access = True, 
                                    allocation_mode = '', 
                                    count = 56, 
                                    device_class_name = '', 
                                    first_available = [
                                        kubernetes_asyncio.client.models.v1beta1/device_sub_request.v1beta1.DeviceSubRequest(
                                            allocation_mode = '', 
                                            count = 56, 
                                            device_class_name = '', 
                                            name = '', 
                                            selectors = [
                                                kubernetes_asyncio.client.models.v1beta1/device_selector.v1beta1.DeviceSelector(
                                                    cel = kubernetes_asyncio.client.models.v1beta1/cel_device_selector.v1beta1.CELDeviceSelector(
                                                        expression = '', ), )
                                                ], 
                                            tolerations = [
                                                kubernetes_asyncio.client.models.v1beta1/device_toleration.v1beta1.DeviceToleration(
                                                    effect = '', 
                                                    key = '', 
                                                    operator = '', 
                                                    toleration_seconds = 56, 
                                                    value = '', )
                                                ], )
                                        ], 
                                    name = '', 
                                    selectors = [
                                        kubernetes_asyncio.client.models.v1beta1/device_selector.v1beta1.DeviceSelector()
                                        ], 
                                    tolerations = [
                                        kubernetes_asyncio.client.models.v1beta1/device_toleration.v1beta1.DeviceToleration(
                                            effect = '', 
                                            key = '', 
                                            operator = '', 
                                            toleration_seconds = 56, 
                                            value = '', )
                                        ], )
                                ], ), ), ),
        )
        """

    def testV1beta1ResourceClaimTemplate(self):
        """Test V1beta1ResourceClaimTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
