# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_container_state_running import V1ContainerStateRunning

class TestV1ContainerStateRunning(unittest.TestCase):
    """V1ContainerStateRunning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ContainerStateRunning:
        """Test V1ContainerStateRunning
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ContainerStateRunning`
        """
        model = V1ContainerStateRunning()
        if include_optional:
            return V1ContainerStateRunning(
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return V1ContainerStateRunning(
        )
        """

    def testV1ContainerStateRunning(self):
        """Test V1ContainerStateRunning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
