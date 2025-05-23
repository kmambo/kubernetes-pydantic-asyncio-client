# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_job_list import V1JobList

class TestV1JobList(unittest.TestCase):
    """V1JobList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1JobList:
        """Test V1JobList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1JobList`
        """
        model = V1JobList()
        if include_optional:
            return V1JobList(
                api_version = '',
                items = [
                    kubernetes_asyncio.client.models.v1/job.v1.Job(
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
                        spec = kubernetes_asyncio.client.models.v1/job_spec.v1.JobSpec(
                            active_deadline_seconds = 56, 
                            backoff_limit = 56, 
                            backoff_limit_per_index = 56, 
                            completion_mode = '', 
                            completions = 56, 
                            managed_by = '', 
                            manual_selector = True, 
                            max_failed_indexes = 56, 
                            parallelism = 56, 
                            pod_failure_policy = kubernetes_asyncio.client.models.v1/pod_failure_policy.v1.PodFailurePolicy(
                                rules = [
                                    kubernetes_asyncio.client.models.v1/pod_failure_policy_rule.v1.PodFailurePolicyRule(
                                        action = '', 
                                        on_exit_codes = kubernetes_asyncio.client.models.v1/pod_failure_policy_on_exit_codes_requirement.v1.PodFailurePolicyOnExitCodesRequirement(
                                            container_name = '', 
                                            operator = '', 
                                            values = [
                                                56
                                                ], ), 
                                        on_pod_conditions = [
                                            kubernetes_asyncio.client.models.v1/pod_failure_policy_on_pod_conditions_pattern.v1.PodFailurePolicyOnPodConditionsPattern(
                                                status = '', 
                                                type = '', )
                                            ], )
                                    ], ), 
                            pod_replacement_policy = '', 
                            selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '', 
                                        operator = '', )
                                    ], 
                                match_labels = {
                                    'key' : ''
                                    }, ), 
                            success_policy = kubernetes_asyncio.client.models.v1/success_policy.v1.SuccessPolicy(
                                rules = [
                                    kubernetes_asyncio.client.models.v1/success_policy_rule.v1.SuccessPolicyRule(
                                        succeeded_count = 56, 
                                        succeeded_indexes = '', )
                                    ], ), 
                            suspend = True, 
                            template = kubernetes_asyncio.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            ttl_seconds_after_finished = 56, ), 
                        status = kubernetes_asyncio.client.models.v1/job_status.v1.JobStatus(
                            active = 56, 
                            completed_indexes = '', 
                            completion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            conditions = [
                                kubernetes_asyncio.client.models.v1/job_condition.v1.JobCondition(
                                    last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', 
                                    status = '', 
                                    type = '', )
                                ], 
                            failed = 56, 
                            failed_indexes = '', 
                            ready = 56, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            succeeded = 56, 
                            terminating = 56, 
                            uncounted_terminated_pods = kubernetes_asyncio.client.models.v1/uncounted_terminated_pods.v1.UncountedTerminatedPods(
                                failed = [
                                    ''
                                    ], 
                                succeeded = [
                                    ''
                                    ], ), ), )
                    ],
                kind = '',
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1JobList(
                items = [
                    kubernetes_asyncio.client.models.v1/job.v1.Job(
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
                        spec = kubernetes_asyncio.client.models.v1/job_spec.v1.JobSpec(
                            active_deadline_seconds = 56, 
                            backoff_limit = 56, 
                            backoff_limit_per_index = 56, 
                            completion_mode = '', 
                            completions = 56, 
                            managed_by = '', 
                            manual_selector = True, 
                            max_failed_indexes = 56, 
                            parallelism = 56, 
                            pod_failure_policy = kubernetes_asyncio.client.models.v1/pod_failure_policy.v1.PodFailurePolicy(
                                rules = [
                                    kubernetes_asyncio.client.models.v1/pod_failure_policy_rule.v1.PodFailurePolicyRule(
                                        action = '', 
                                        on_exit_codes = kubernetes_asyncio.client.models.v1/pod_failure_policy_on_exit_codes_requirement.v1.PodFailurePolicyOnExitCodesRequirement(
                                            container_name = '', 
                                            operator = '', 
                                            values = [
                                                56
                                                ], ), 
                                        on_pod_conditions = [
                                            kubernetes_asyncio.client.models.v1/pod_failure_policy_on_pod_conditions_pattern.v1.PodFailurePolicyOnPodConditionsPattern(
                                                status = '', 
                                                type = '', )
                                            ], )
                                    ], ), 
                            pod_replacement_policy = '', 
                            selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '', 
                                        operator = '', )
                                    ], 
                                match_labels = {
                                    'key' : ''
                                    }, ), 
                            success_policy = kubernetes_asyncio.client.models.v1/success_policy.v1.SuccessPolicy(
                                rules = [
                                    kubernetes_asyncio.client.models.v1/success_policy_rule.v1.SuccessPolicyRule(
                                        succeeded_count = 56, 
                                        succeeded_indexes = '', )
                                    ], ), 
                            suspend = True, 
                            template = kubernetes_asyncio.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            ttl_seconds_after_finished = 56, ), 
                        status = kubernetes_asyncio.client.models.v1/job_status.v1.JobStatus(
                            active = 56, 
                            completed_indexes = '', 
                            completion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            conditions = [
                                kubernetes_asyncio.client.models.v1/job_condition.v1.JobCondition(
                                    last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '', 
                                    reason = '', 
                                    status = '', 
                                    type = '', )
                                ], 
                            failed = 56, 
                            failed_indexes = '', 
                            ready = 56, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            succeeded = 56, 
                            terminating = 56, 
                            uncounted_terminated_pods = kubernetes_asyncio.client.models.v1/uncounted_terminated_pods.v1.UncountedTerminatedPods(
                                failed = [
                                    ''
                                    ], 
                                succeeded = [
                                    ''
                                    ], ), ), )
                    ],
        )
        """

    def testV1JobList(self):
        """Test V1JobList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
