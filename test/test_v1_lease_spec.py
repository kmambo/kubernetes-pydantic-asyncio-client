# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1_lease_spec import V1LeaseSpec

class TestV1LeaseSpec(unittest.TestCase):
    """V1LeaseSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1LeaseSpec:
        """Test V1LeaseSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1LeaseSpec`
        """
        model = V1LeaseSpec()
        if include_optional:
            return V1LeaseSpec(
                acquire_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                holder_identity = '',
                lease_duration_seconds = 56,
                lease_transitions = 56,
                preferred_holder = '',
                renew_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                strategy = ''
            )
        else:
            return V1LeaseSpec(
        )
        """

    def testV1LeaseSpec(self):
        """Test V1LeaseSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
