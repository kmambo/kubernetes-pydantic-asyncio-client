# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_endpoint_slice_list import V1EndpointSliceList

class TestV1EndpointSliceList(unittest.TestCase):
    """V1EndpointSliceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EndpointSliceList:
        """Test V1EndpointSliceList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EndpointSliceList`
        """
        model = V1EndpointSliceList()
        if include_optional:
            return V1EndpointSliceList(
                api_version = '',
                items = [
                    kubernetes_asyncio.client.models.v1/endpoint_slice.v1.EndpointSlice(
                        address_type = '', 
                        api_version = '', 
                        endpoints = [
                            kubernetes_asyncio.client.models.v1/endpoint.v1.Endpoint(
                                addresses = [
                                    ''
                                    ], 
                                conditions = kubernetes_asyncio.client.models.v1/endpoint_conditions.v1.EndpointConditions(
                                    ready = True, 
                                    serving = True, 
                                    terminating = True, ), 
                                deprecated_topology = {
                                    'key' : ''
                                    }, 
                                hints = kubernetes_asyncio.client.models.v1/endpoint_hints.v1.EndpointHints(
                                    for_nodes = [
                                        kubernetes_asyncio.client.models.v1/for_node.v1.ForNode(
                                            name = '', )
                                        ], 
                                    for_zones = [
                                        kubernetes_asyncio.client.models.v1/for_zone.v1.ForZone(
                                            name = '', )
                                        ], ), 
                                hostname = '', 
                                node_name = '', 
                                target_ref = kubernetes_asyncio.client.models.v1/object_reference.v1.ObjectReference(
                                    api_version = '', 
                                    field_path = '', 
                                    kind = '', 
                                    name = '', 
                                    namespace = '', 
                                    resource_version = '', 
                                    uid = '', ), 
                                zone = '', )
                            ], 
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
                        ports = [
                            kubernetes_asyncio.client.models.discovery/v1/endpoint_port.discovery.v1.EndpointPort(
                                app_protocol = '', 
                                name = '', 
                                port = 56, 
                                protocol = '', )
                            ], )
                    ],
                kind = '',
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1EndpointSliceList(
                items = [
                    kubernetes_asyncio.client.models.v1/endpoint_slice.v1.EndpointSlice(
                        address_type = '', 
                        api_version = '', 
                        endpoints = [
                            kubernetes_asyncio.client.models.v1/endpoint.v1.Endpoint(
                                addresses = [
                                    ''
                                    ], 
                                conditions = kubernetes_asyncio.client.models.v1/endpoint_conditions.v1.EndpointConditions(
                                    ready = True, 
                                    serving = True, 
                                    terminating = True, ), 
                                deprecated_topology = {
                                    'key' : ''
                                    }, 
                                hints = kubernetes_asyncio.client.models.v1/endpoint_hints.v1.EndpointHints(
                                    for_nodes = [
                                        kubernetes_asyncio.client.models.v1/for_node.v1.ForNode(
                                            name = '', )
                                        ], 
                                    for_zones = [
                                        kubernetes_asyncio.client.models.v1/for_zone.v1.ForZone(
                                            name = '', )
                                        ], ), 
                                hostname = '', 
                                node_name = '', 
                                target_ref = kubernetes_asyncio.client.models.v1/object_reference.v1.ObjectReference(
                                    api_version = '', 
                                    field_path = '', 
                                    kind = '', 
                                    name = '', 
                                    namespace = '', 
                                    resource_version = '', 
                                    uid = '', ), 
                                zone = '', )
                            ], 
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
                        ports = [
                            kubernetes_asyncio.client.models.discovery/v1/endpoint_port.discovery.v1.EndpointPort(
                                app_protocol = '', 
                                name = '', 
                                port = 56, 
                                protocol = '', )
                            ], )
                    ],
        )
        """

    def testV1EndpointSliceList(self):
        """Test V1EndpointSliceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
