# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_empty_dir_volume_source import V1EmptyDirVolumeSource

class TestV1EmptyDirVolumeSource(unittest.TestCase):
    """V1EmptyDirVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EmptyDirVolumeSource:
        """Test V1EmptyDirVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EmptyDirVolumeSource`
        """
        model = V1EmptyDirVolumeSource()
        if include_optional:
            return V1EmptyDirVolumeSource(
                medium = '',
                size_limit = ''
            )
        else:
            return V1EmptyDirVolumeSource(
        )
        """

    def testV1EmptyDirVolumeSource(self):
        """Test V1EmptyDirVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
