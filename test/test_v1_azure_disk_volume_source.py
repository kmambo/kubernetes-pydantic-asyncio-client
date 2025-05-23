# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_azure_disk_volume_source import V1AzureDiskVolumeSource

class TestV1AzureDiskVolumeSource(unittest.TestCase):
    """V1AzureDiskVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AzureDiskVolumeSource:
        """Test V1AzureDiskVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AzureDiskVolumeSource`
        """
        model = V1AzureDiskVolumeSource()
        if include_optional:
            return V1AzureDiskVolumeSource(
                caching_mode = '',
                disk_name = '',
                disk_uri = '',
                fs_type = '',
                kind = '',
                read_only = True
            )
        else:
            return V1AzureDiskVolumeSource(
                disk_name = '',
                disk_uri = '',
        )
        """

    def testV1AzureDiskVolumeSource(self):
        """Test V1AzureDiskVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
