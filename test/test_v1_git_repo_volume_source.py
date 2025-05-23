# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_git_repo_volume_source import V1GitRepoVolumeSource

class TestV1GitRepoVolumeSource(unittest.TestCase):
    """V1GitRepoVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GitRepoVolumeSource:
        """Test V1GitRepoVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GitRepoVolumeSource`
        """
        model = V1GitRepoVolumeSource()
        if include_optional:
            return V1GitRepoVolumeSource(
                directory = '',
                repository = '',
                revision = ''
            )
        else:
            return V1GitRepoVolumeSource(
                repository = '',
        )
        """

    def testV1GitRepoVolumeSource(self):
        """Test V1GitRepoVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
