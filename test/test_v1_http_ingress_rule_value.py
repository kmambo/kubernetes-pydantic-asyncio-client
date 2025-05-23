# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_http_ingress_rule_value import V1HTTPIngressRuleValue

class TestV1HTTPIngressRuleValue(unittest.TestCase):
    """V1HTTPIngressRuleValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1HTTPIngressRuleValue:
        """Test V1HTTPIngressRuleValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1HTTPIngressRuleValue`
        """
        model = V1HTTPIngressRuleValue()
        if include_optional:
            return V1HTTPIngressRuleValue(
                paths = [
                    kubernetes_asyncio.client.models.v1/http_ingress_path.v1.HTTPIngressPath(
                        backend = kubernetes_asyncio.client.models.v1/ingress_backend.v1.IngressBackend(
                            resource = kubernetes_asyncio.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                                api_group = '', 
                                kind = '', 
                                name = '', ), 
                            service = kubernetes_asyncio.client.models.v1/ingress_service_backend.v1.IngressServiceBackend(
                                name = '', 
                                port = kubernetes_asyncio.client.models.v1/service_backend_port.v1.ServiceBackendPort(
                                    name = '', 
                                    number = 56, ), ), ), 
                        path = '', 
                        path_type = '', )
                    ]
            )
        else:
            return V1HTTPIngressRuleValue(
                paths = [
                    kubernetes_asyncio.client.models.v1/http_ingress_path.v1.HTTPIngressPath(
                        backend = kubernetes_asyncio.client.models.v1/ingress_backend.v1.IngressBackend(
                            resource = kubernetes_asyncio.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                                api_group = '', 
                                kind = '', 
                                name = '', ), 
                            service = kubernetes_asyncio.client.models.v1/ingress_service_backend.v1.IngressServiceBackend(
                                name = '', 
                                port = kubernetes_asyncio.client.models.v1/service_backend_port.v1.ServiceBackendPort(
                                    name = '', 
                                    number = 56, ), ), ), 
                        path = '', 
                        path_type = '', )
                    ],
        )
        """

    def testV1HTTPIngressRuleValue(self):
        """Test V1HTTPIngressRuleValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
