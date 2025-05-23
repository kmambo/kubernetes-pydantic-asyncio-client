# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_stateful_set_list import V1StatefulSetList

class TestV1StatefulSetList(unittest.TestCase):
    """V1StatefulSetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1StatefulSetList:
        """Test V1StatefulSetList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1StatefulSetList`
        """
        model = V1StatefulSetList()
        if include_optional:
            return V1StatefulSetList(
                api_version = '',
                items = [
                    kubernetes_asyncio.client.models.v1/stateful_set.v1.StatefulSet(
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
                        spec = kubernetes_asyncio.client.models.v1/stateful_set_spec.v1.StatefulSetSpec(
                            min_ready_seconds = 56, 
                            ordinals = kubernetes_asyncio.client.models.v1/stateful_set_ordinals.v1.StatefulSetOrdinals(
                                start = 56, ), 
                            persistent_volume_claim_retention_policy = kubernetes_asyncio.client.models.v1/stateful_set_persistent_volume_claim_retention_policy.v1.StatefulSetPersistentVolumeClaimRetentionPolicy(
                                when_deleted = '', 
                                when_scaled = '', ), 
                            pod_management_policy = '', 
                            replicas = 56, 
                            revision_history_limit = 56, 
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
                                    }, ), 
                            service_name = '', 
                            template = kubernetes_asyncio.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            update_strategy = kubernetes_asyncio.client.models.v1/stateful_set_update_strategy.v1.StatefulSetUpdateStrategy(
                                rolling_update = kubernetes_asyncio.client.models.v1/rolling_update_stateful_set_strategy.v1.RollingUpdateStatefulSetStrategy(
                                    max_unavailable = kubernetes_asyncio.client.models.max_unavailable.maxUnavailable(), 
                                    partition = 56, ), 
                                type = '', ), 
                            volume_claim_templates = [
                                kubernetes_asyncio.client.models.v1/persistent_volume_claim.v1.PersistentVolumeClaim(
                                    api_version = '', 
                                    kind = '', 
                                    status = kubernetes_asyncio.client.models.v1/persistent_volume_claim_status.v1.PersistentVolumeClaimStatus(
                                        access_modes = [
                                            ''
                                            ], 
                                        allocated_resource_statuses = {
                                            'key' : ''
                                            }, 
                                        allocated_resources = {
                                            'key' : ''
                                            }, 
                                        capacity = {
                                            'key' : ''
                                            }, 
                                        conditions = [
                                            kubernetes_asyncio.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                                                last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                message = '', 
                                                reason = '', 
                                                status = '', 
                                                type = '', )
                                            ], 
                                        current_volume_attributes_class_name = '', 
                                        modify_volume_status = kubernetes_asyncio.client.models.v1/modify_volume_status.v1.ModifyVolumeStatus(
                                            status = '', 
                                            target_volume_attributes_class_name = '', ), 
                                        phase = '', ), )
                                ], ), 
                        status = kubernetes_asyncio.client.models.v1/stateful_set_status.v1.StatefulSetStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            current_replicas = 56, 
                            current_revision = '', 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            update_revision = '', 
                            updated_replicas = 56, ), )
                    ],
                kind = '',
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1StatefulSetList(
                items = [
                    kubernetes_asyncio.client.models.v1/stateful_set.v1.StatefulSet(
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
                        spec = kubernetes_asyncio.client.models.v1/stateful_set_spec.v1.StatefulSetSpec(
                            min_ready_seconds = 56, 
                            ordinals = kubernetes_asyncio.client.models.v1/stateful_set_ordinals.v1.StatefulSetOrdinals(
                                start = 56, ), 
                            persistent_volume_claim_retention_policy = kubernetes_asyncio.client.models.v1/stateful_set_persistent_volume_claim_retention_policy.v1.StatefulSetPersistentVolumeClaimRetentionPolicy(
                                when_deleted = '', 
                                when_scaled = '', ), 
                            pod_management_policy = '', 
                            replicas = 56, 
                            revision_history_limit = 56, 
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
                                    }, ), 
                            service_name = '', 
                            template = kubernetes_asyncio.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            update_strategy = kubernetes_asyncio.client.models.v1/stateful_set_update_strategy.v1.StatefulSetUpdateStrategy(
                                rolling_update = kubernetes_asyncio.client.models.v1/rolling_update_stateful_set_strategy.v1.RollingUpdateStatefulSetStrategy(
                                    max_unavailable = kubernetes_asyncio.client.models.max_unavailable.maxUnavailable(), 
                                    partition = 56, ), 
                                type = '', ), 
                            volume_claim_templates = [
                                kubernetes_asyncio.client.models.v1/persistent_volume_claim.v1.PersistentVolumeClaim(
                                    api_version = '', 
                                    kind = '', 
                                    status = kubernetes_asyncio.client.models.v1/persistent_volume_claim_status.v1.PersistentVolumeClaimStatus(
                                        access_modes = [
                                            ''
                                            ], 
                                        allocated_resource_statuses = {
                                            'key' : ''
                                            }, 
                                        allocated_resources = {
                                            'key' : ''
                                            }, 
                                        capacity = {
                                            'key' : ''
                                            }, 
                                        conditions = [
                                            kubernetes_asyncio.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                                                last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                message = '', 
                                                reason = '', 
                                                status = '', 
                                                type = '', )
                                            ], 
                                        current_volume_attributes_class_name = '', 
                                        modify_volume_status = kubernetes_asyncio.client.models.v1/modify_volume_status.v1.ModifyVolumeStatus(
                                            status = '', 
                                            target_volume_attributes_class_name = '', ), 
                                        phase = '', ), )
                                ], ), 
                        status = kubernetes_asyncio.client.models.v1/stateful_set_status.v1.StatefulSetStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            current_replicas = 56, 
                            current_revision = '', 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            update_revision = '', 
                            updated_replicas = 56, ), )
                    ],
        )
        """

    def testV1StatefulSetList(self):
        """Test V1StatefulSetList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
