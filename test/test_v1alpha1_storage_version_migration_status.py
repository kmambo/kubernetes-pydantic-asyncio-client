# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1alpha1_storage_version_migration_status import V1alpha1StorageVersionMigrationStatus

class TestV1alpha1StorageVersionMigrationStatus(unittest.TestCase):
    """V1alpha1StorageVersionMigrationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1StorageVersionMigrationStatus:
        """Test V1alpha1StorageVersionMigrationStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1StorageVersionMigrationStatus`
        """
        model = V1alpha1StorageVersionMigrationStatus()
        if include_optional:
            return V1alpha1StorageVersionMigrationStatus(
                conditions = [
                    kubernetes_asyncio.client.models.v1alpha1/migration_condition.v1alpha1.MigrationCondition(
                        last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        status = '', 
                        type = '', )
                    ],
                resource_version = ''
            )
        else:
            return V1alpha1StorageVersionMigrationStatus(
        )
        """

    def testV1alpha1StorageVersionMigrationStatus(self):
        """Test V1alpha1StorageVersionMigrationStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
