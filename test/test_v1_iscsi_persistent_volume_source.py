# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_iscsi_persistent_volume_source import V1ISCSIPersistentVolumeSource

class TestV1ISCSIPersistentVolumeSource(unittest.TestCase):
    """V1ISCSIPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ISCSIPersistentVolumeSource:
        """Test V1ISCSIPersistentVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ISCSIPersistentVolumeSource`
        """
        model = V1ISCSIPersistentVolumeSource()
        if include_optional:
            return V1ISCSIPersistentVolumeSource(
                chap_auth_discovery = True,
                chap_auth_session = True,
                fs_type = '',
                initiator_name = '',
                iqn = '',
                iscsi_interface = '',
                lun = 56,
                portals = [
                    ''
                    ],
                read_only = True,
                secret_ref = kubernetes_asyncio.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                target_portal = ''
            )
        else:
            return V1ISCSIPersistentVolumeSource(
                iqn = '',
                lun = 56,
                target_portal = '',
        )
        """

    def testV1ISCSIPersistentVolumeSource(self):
        """Test V1ISCSIPersistentVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
