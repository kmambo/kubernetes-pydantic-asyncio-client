# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_api_service_list import V1APIServiceList

class TestV1APIServiceList(unittest.TestCase):
    """V1APIServiceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1APIServiceList:
        """Test V1APIServiceList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1APIServiceList`
        """
        model = V1APIServiceList()
        if include_optional:
            return V1APIServiceList(
                api_version = '',
                items = [
                    kubernetes_asyncio.client.models.v1/api_service.v1.APIService(
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
                        spec = kubernetes_asyncio.client.models.v1/api_service_spec.v1.APIServiceSpec(
                            ca_bundle = 'YQ==', 
                            group = '', 
                            group_priority_minimum = 56, 
                            insecure_skip_tls_verify = True, 
                            service = kubernetes_asyncio.client.models.apiregistration/v1/service_reference.apiregistration.v1.ServiceReference(
                                name = '', 
                                namespace = '', 
                                port = 56, ), 
                            version = '', 
                            version_priority = 56, ), 
                        status = kubernetes_asyncio.client.models.v1/api_service_status.v1.APIServiceStatus(
                            conditions = [
                                kubernetes_asyncio.client.models.v1/api_service_condition.v1.APIServiceCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', 
                                    status = '', 
                                    type = '', )
                                ], ), )
                    ],
                kind = '',
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1APIServiceList(
                items = [
                    kubernetes_asyncio.client.models.v1/api_service.v1.APIService(
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
                        spec = kubernetes_asyncio.client.models.v1/api_service_spec.v1.APIServiceSpec(
                            ca_bundle = 'YQ==', 
                            group = '', 
                            group_priority_minimum = 56, 
                            insecure_skip_tls_verify = True, 
                            service = kubernetes_asyncio.client.models.apiregistration/v1/service_reference.apiregistration.v1.ServiceReference(
                                name = '', 
                                namespace = '', 
                                port = 56, ), 
                            version = '', 
                            version_priority = 56, ), 
                        status = kubernetes_asyncio.client.models.v1/api_service_status.v1.APIServiceStatus(
                            conditions = [
                                kubernetes_asyncio.client.models.v1/api_service_condition.v1.APIServiceCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', 
                                    status = '', 
                                    type = '', )
                                ], ), )
                    ],
        )
        """

    def testV1APIServiceList(self):
        """Test V1APIServiceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
