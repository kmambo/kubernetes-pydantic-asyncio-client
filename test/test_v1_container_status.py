# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_container_status import V1ContainerStatus

class TestV1ContainerStatus(unittest.TestCase):
    """V1ContainerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ContainerStatus:
        """Test V1ContainerStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ContainerStatus`
        """
        model = V1ContainerStatus()
        if include_optional:
            return V1ContainerStatus(
                allocated_resources = {
                    'key' : ''
                    },
                allocated_resources_status = [
                    kubernetes_asyncio.client.models.v1/resource_status.v1.ResourceStatus(
                        name = '', 
                        resources = [
                            kubernetes_asyncio.client.models.v1/resource_health.v1.ResourceHealth(
                                health = '', 
                                resource_id = '', )
                            ], )
                    ],
                container_id = '',
                image = '',
                image_id = '',
                last_state = kubernetes_asyncio.client.models.v1/container_state.v1.ContainerState(
                    running = kubernetes_asyncio.client.models.v1/container_state_running.v1.ContainerStateRunning(
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    terminated = kubernetes_asyncio.client.models.v1/container_state_terminated.v1.ContainerStateTerminated(
                        container_id = '', 
                        exit_code = 56, 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        signal = 56, 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    waiting = kubernetes_asyncio.client.models.v1/container_state_waiting.v1.ContainerStateWaiting(
                        message = '', 
                        reason = '', ), ),
                name = '',
                ready = True,
                resources = kubernetes_asyncio.client.models.v1/resource_requirements.v1.ResourceRequirements(
                    claims = [
                        kubernetes_asyncio.client.models.v1/resource_claim.v1.ResourceClaim(
                            name = '', 
                            request = '', )
                        ], 
                    limits = {
                        'key' : ''
                        }, 
                    requests = {
                        'key' : ''
                        }, ),
                restart_count = 56,
                started = True,
                state = kubernetes_asyncio.client.models.v1/container_state.v1.ContainerState(
                    running = kubernetes_asyncio.client.models.v1/container_state_running.v1.ContainerStateRunning(
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    terminated = kubernetes_asyncio.client.models.v1/container_state_terminated.v1.ContainerStateTerminated(
                        container_id = '', 
                        exit_code = 56, 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        signal = 56, 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    waiting = kubernetes_asyncio.client.models.v1/container_state_waiting.v1.ContainerStateWaiting(
                        message = '', 
                        reason = '', ), ),
                stop_signal = '',
                user = kubernetes_asyncio.client.models.v1/container_user.v1.ContainerUser(
                    linux = kubernetes_asyncio.client.models.v1/linux_container_user.v1.LinuxContainerUser(
                        gid = 56, 
                        supplemental_groups = [
                            56
                            ], 
                        uid = 56, ), ),
                volume_mounts = [
                    kubernetes_asyncio.client.models.v1/volume_mount_status.v1.VolumeMountStatus(
                        mount_path = '', 
                        name = '', 
                        read_only = True, 
                        recursive_read_only = '', )
                    ]
            )
        else:
            return V1ContainerStatus(
                image = '',
                image_id = '',
                name = '',
                ready = True,
                restart_count = 56,
        )
        """

    def testV1ContainerStatus(self):
        """Test V1ContainerStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
