# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_node_list import V1NodeList

class TestV1NodeList(unittest.TestCase):
    """V1NodeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1NodeList:
        """Test V1NodeList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1NodeList`
        """
        model = V1NodeList()
        if include_optional:
            return V1NodeList(
                api_version = '',
                items = [
                    kubernetes_asyncio.client.models.v1/node.v1.Node(
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
                        spec = kubernetes_asyncio.client.models.v1/node_spec.v1.NodeSpec(
                            config_source = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(
                                config_map = kubernetes_asyncio.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                                    kubelet_config_key = '', 
                                    name = '', 
                                    namespace = '', 
                                    resource_version = '', 
                                    uid = '', ), ), 
                            external_id = '', 
                            pod_cidr = '', 
                            pod_cidrs = [
                                ''
                                ], 
                            provider_id = '', 
                            taints = [
                                kubernetes_asyncio.client.models.v1/taint.v1.Taint(
                                    effect = '', 
                                    key = '', 
                                    time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    value = '', )
                                ], 
                            unschedulable = True, ), 
                        status = kubernetes_asyncio.client.models.v1/node_status.v1.NodeStatus(
                            addresses = [
                                kubernetes_asyncio.client.models.v1/node_address.v1.NodeAddress(
                                    address = '', 
                                    type = '', )
                                ], 
                            allocatable = {
                                'key' : ''
                                }, 
                            capacity = {
                                'key' : ''
                                }, 
                            conditions = [
                                kubernetes_asyncio.client.models.v1/node_condition.v1.NodeCondition(
                                    last_heartbeat_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', 
                                    status = '', 
                                    type = '', )
                                ], 
                            config = kubernetes_asyncio.client.models.v1/node_config_status.v1.NodeConfigStatus(
                                active = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(), 
                                assigned = , 
                                error = '', 
                                last_known_good = , ), 
                            daemon_endpoints = kubernetes_asyncio.client.models.v1/node_daemon_endpoints.v1.NodeDaemonEndpoints(
                                kubelet_endpoint = kubernetes_asyncio.client.models.v1/daemon_endpoint.v1.DaemonEndpoint(
                                    port = 56, ), ), 
                            features = kubernetes_asyncio.client.models.v1/node_features.v1.NodeFeatures(
                                supplemental_groups_policy = True, ), 
                            images = [
                                kubernetes_asyncio.client.models.v1/container_image.v1.ContainerImage(
                                    names = [
                                        ''
                                        ], 
                                    size_bytes = 56, )
                                ], 
                            node_info = kubernetes_asyncio.client.models.v1/node_system_info.v1.NodeSystemInfo(
                                architecture = '', 
                                boot_id = '', 
                                container_runtime_version = '', 
                                kernel_version = '', 
                                kube_proxy_version = '', 
                                kubelet_version = '', 
                                machine_id = '', 
                                operating_system = '', 
                                os_image = '', 
                                swap = kubernetes_asyncio.client.models.v1/node_swap_status.v1.NodeSwapStatus(), 
                                system_uuid = '', ), 
                            phase = '', 
                            runtime_handlers = [
                                kubernetes_asyncio.client.models.v1/node_runtime_handler.v1.NodeRuntimeHandler(
                                    name = '', )
                                ], 
                            volumes_attached = [
                                kubernetes_asyncio.client.models.v1/attached_volume.v1.AttachedVolume(
                                    device_path = '', 
                                    name = '', )
                                ], 
                            volumes_in_use = [
                                ''
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
            return V1NodeList(
                items = [
                    kubernetes_asyncio.client.models.v1/node.v1.Node(
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
                        spec = kubernetes_asyncio.client.models.v1/node_spec.v1.NodeSpec(
                            config_source = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(
                                config_map = kubernetes_asyncio.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                                    kubelet_config_key = '', 
                                    name = '', 
                                    namespace = '', 
                                    resource_version = '', 
                                    uid = '', ), ), 
                            external_id = '', 
                            pod_cidr = '', 
                            pod_cidrs = [
                                ''
                                ], 
                            provider_id = '', 
                            taints = [
                                kubernetes_asyncio.client.models.v1/taint.v1.Taint(
                                    effect = '', 
                                    key = '', 
                                    time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    value = '', )
                                ], 
                            unschedulable = True, ), 
                        status = kubernetes_asyncio.client.models.v1/node_status.v1.NodeStatus(
                            addresses = [
                                kubernetes_asyncio.client.models.v1/node_address.v1.NodeAddress(
                                    address = '', 
                                    type = '', )
                                ], 
                            allocatable = {
                                'key' : ''
                                }, 
                            capacity = {
                                'key' : ''
                                }, 
                            conditions = [
                                kubernetes_asyncio.client.models.v1/node_condition.v1.NodeCondition(
                                    last_heartbeat_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', 
                                    status = '', 
                                    type = '', )
                                ], 
                            config = kubernetes_asyncio.client.models.v1/node_config_status.v1.NodeConfigStatus(
                                active = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(), 
                                assigned = , 
                                error = '', 
                                last_known_good = , ), 
                            daemon_endpoints = kubernetes_asyncio.client.models.v1/node_daemon_endpoints.v1.NodeDaemonEndpoints(
                                kubelet_endpoint = kubernetes_asyncio.client.models.v1/daemon_endpoint.v1.DaemonEndpoint(
                                    port = 56, ), ), 
                            features = kubernetes_asyncio.client.models.v1/node_features.v1.NodeFeatures(
                                supplemental_groups_policy = True, ), 
                            images = [
                                kubernetes_asyncio.client.models.v1/container_image.v1.ContainerImage(
                                    names = [
                                        ''
                                        ], 
                                    size_bytes = 56, )
                                ], 
                            node_info = kubernetes_asyncio.client.models.v1/node_system_info.v1.NodeSystemInfo(
                                architecture = '', 
                                boot_id = '', 
                                container_runtime_version = '', 
                                kernel_version = '', 
                                kube_proxy_version = '', 
                                kubelet_version = '', 
                                machine_id = '', 
                                operating_system = '', 
                                os_image = '', 
                                swap = kubernetes_asyncio.client.models.v1/node_swap_status.v1.NodeSwapStatus(), 
                                system_uuid = '', ), 
                            phase = '', 
                            runtime_handlers = [
                                kubernetes_asyncio.client.models.v1/node_runtime_handler.v1.NodeRuntimeHandler(
                                    name = '', )
                                ], 
                            volumes_attached = [
                                kubernetes_asyncio.client.models.v1/attached_volume.v1.AttachedVolume(
                                    device_path = '', 
                                    name = '', )
                                ], 
                            volumes_in_use = [
                                ''
                                ], ), )
                    ],
        )
        """

    def testV1NodeList(self):
        """Test V1NodeList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
