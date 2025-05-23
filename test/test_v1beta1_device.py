# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.models.v1beta1_device import V1beta1Device

class TestV1beta1Device(unittest.TestCase):
    """V1beta1Device unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1Device:
        """Test V1beta1Device
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1Device`
        """
        model = V1beta1Device()
        if include_optional:
            return V1beta1Device(
                basic = kubernetes_asyncio.client.models.v1beta1/basic_device.v1beta1.BasicDevice(
                    all_nodes = True, 
                    attributes = {
                        'key' : kubernetes_asyncio.client.models.v1beta1/device_attribute.v1beta1.DeviceAttribute(
                            bool = True, 
                            int = 56, 
                            string = '', 
                            version = '', )
                        }, 
                    capacity = {
                        'key' : kubernetes_asyncio.client.models.v1beta1/device_capacity.v1beta1.DeviceCapacity(
                            value = '', )
                        }, 
                    consumes_counters = [
                        kubernetes_asyncio.client.models.v1beta1/device_counter_consumption.v1beta1.DeviceCounterConsumption(
                            counter_set = '', 
                            counters = {
                                'key' : kubernetes_asyncio.client.models.v1beta1/counter.v1beta1.Counter(
                                    value = '', )
                                }, )
                        ], 
                    node_name = '', 
                    node_selector = kubernetes_asyncio.client.models.v1/node_selector.v1.NodeSelector(
                        node_selector_terms = [
                            kubernetes_asyncio.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                match_expressions = [
                                    kubernetes_asyncio.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                        key = '', 
                                        operator = '', 
                                        values = [
                                            ''
                                            ], )
                                    ], 
                                match_fields = [
                                    kubernetes_asyncio.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                        key = '', 
                                        operator = '', )
                                    ], )
                            ], ), 
                    taints = [
                        kubernetes_asyncio.client.models.v1beta1/device_taint.v1beta1.DeviceTaint(
                            effect = '', 
                            key = '', 
                            time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            value = '', )
                        ], ),
                name = ''
            )
        else:
            return V1beta1Device(
                name = '',
        )
        """

    def testV1beta1Device(self):
        """Test V1beta1Device"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
