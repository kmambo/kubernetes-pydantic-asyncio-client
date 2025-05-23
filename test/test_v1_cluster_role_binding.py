# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_cluster_role_binding import V1ClusterRoleBinding

class TestV1ClusterRoleBinding(unittest.TestCase):
    """V1ClusterRoleBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ClusterRoleBinding:
        """Test V1ClusterRoleBinding
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ClusterRoleBinding`
        """
        model = V1ClusterRoleBinding()
        if include_optional:
            return V1ClusterRoleBinding(
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
                role_ref = kubernetes_asyncio.client.models.v1/role_ref.v1.RoleRef(
                    api_group = '', 
                    kind = '', 
                    name = '', ),
                subjects = [
                    kubernetes_asyncio.client.models.rbac/v1/subject.rbac.v1.Subject(
                        api_group = '', 
                        kind = '', 
                        name = '', 
                        namespace = '', )
                    ]
            )
        else:
            return V1ClusterRoleBinding(
                role_ref = kubernetes_asyncio.client.models.v1/role_ref.v1.RoleRef(
                    api_group = '', 
                    kind = '', 
                    name = '', ),
        )
        """

    def testV1ClusterRoleBinding(self):
        """Test V1ClusterRoleBinding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
