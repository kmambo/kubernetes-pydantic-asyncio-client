# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: master
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes_asyncio.client.api.logs_api import LogsApi


class TestLogsApi(unittest.IsolatedAsyncioTestCase):
    """LogsApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = LogsApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_log_file_handler(self) -> None:
        """Test case for log_file_handler

        """
        pass

    async def test_log_file_list_handler(self) -> None:
        """Test case for log_file_list_handler

        """
        pass


if __name__ == '__main__':
    unittest.main()
