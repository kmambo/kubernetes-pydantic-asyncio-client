# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_volume_projection import V1VolumeProjection

class TestV1VolumeProjection(unittest.TestCase):
    """V1VolumeProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1VolumeProjection:
        """Test V1VolumeProjection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1VolumeProjection`
        """
        model = V1VolumeProjection()
        if include_optional:
            return V1VolumeProjection(
                cluster_trust_bundle = kubernetes_asyncio.client.models.v1/cluster_trust_bundle_projection.v1.ClusterTrustBundleProjection(
                    label_selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
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
                    name = '', 
                    optional = True, 
                    path = '', 
                    signer_name = '', ),
                config_map = kubernetes_asyncio.client.models.v1/config_map_projection.v1.ConfigMapProjection(
                    items = [
                        kubernetes_asyncio.client.models.v1/key_to_path.v1.KeyToPath(
                            key = '', 
                            mode = 56, 
                            path = '', )
                        ], 
                    name = '', 
                    optional = True, ),
                downward_api = kubernetes_asyncio.client.models.v1/downward_api_projection.v1.DownwardAPIProjection(
                    items = [
                        kubernetes_asyncio.client.models.v1/downward_api_volume_file.v1.DownwardAPIVolumeFile(
                            field_ref = kubernetes_asyncio.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                                api_version = '', 
                                field_path = '', ), 
                            mode = 56, 
                            path = '', 
                            resource_field_ref = kubernetes_asyncio.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                                container_name = '', 
                                divisor = '', 
                                resource = '', ), )
                        ], ),
                secret = kubernetes_asyncio.client.models.v1/secret_projection.v1.SecretProjection(
                    items = [
                        kubernetes_asyncio.client.models.v1/key_to_path.v1.KeyToPath(
                            key = '', 
                            mode = 56, 
                            path = '', )
                        ], 
                    name = '', 
                    optional = True, ),
                service_account_token = kubernetes_asyncio.client.models.v1/service_account_token_projection.v1.ServiceAccountTokenProjection(
                    audience = '', 
                    expiration_seconds = 56, 
                    path = '', )
            )
        else:
            return V1VolumeProjection(
        )
        """

    def testV1VolumeProjection(self):
        """Test V1VolumeProjection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
