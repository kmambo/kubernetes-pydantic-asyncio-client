# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1alpha3_counter_set import V1alpha3CounterSet

class TestV1alpha3CounterSet(unittest.TestCase):
    """V1alpha3CounterSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha3CounterSet:
        """Test V1alpha3CounterSet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha3CounterSet`
        """
        model = V1alpha3CounterSet()
        if include_optional:
            return V1alpha3CounterSet(
                counters = {
                    'key' : kubernetes_asyncio.client.models.v1alpha3/counter.v1alpha3.Counter(
                        value = '', )
                    },
                name = ''
            )
        else:
            return V1alpha3CounterSet(
                counters = {
                    'key' : kubernetes_asyncio.client.models.v1alpha3/counter.v1alpha3.Counter(
                        value = '', )
                    },
                name = '',
        )
        """

    def testV1alpha3CounterSet(self):
        """Test V1alpha3CounterSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
