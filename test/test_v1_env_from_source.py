# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_env_from_source import V1EnvFromSource

class TestV1EnvFromSource(unittest.TestCase):
    """V1EnvFromSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EnvFromSource:
        """Test V1EnvFromSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EnvFromSource`
        """
        model = V1EnvFromSource()
        if include_optional:
            return V1EnvFromSource(
                config_map_ref = kubernetes_asyncio.client.models.v1/config_map_env_source.v1.ConfigMapEnvSource(
                    name = '', 
                    optional = True, ),
                prefix = '',
                secret_ref = kubernetes_asyncio.client.models.v1/secret_env_source.v1.SecretEnvSource(
                    name = '', 
                    optional = True, )
            )
        else:
            return V1EnvFromSource(
        )
        """

    def testV1EnvFromSource(self):
        """Test V1EnvFromSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
