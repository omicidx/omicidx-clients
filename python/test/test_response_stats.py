# coding: utf-8

"""
    OmicIDX

        The OmicIDX API documentation is available in three forms:  - [RapiDoc](/docs) - [OpenAPI/Swagger Interactive](/swatterdoc) - [ReDoc (more readable in some ways)](/redoc)    # noqa: E501

    The version of the OpenAPI document: 0.99
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.response_stats import ResponseStats  # noqa: E501
from openapi_client.rest import ApiException

class TestResponseStats(unittest.TestCase):
    """ResponseStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResponseStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.response_stats.ResponseStats()  # noqa: E501
        if include_optional :
            return ResponseStats(
                total = 56, 
                took = 1.337
            )
        else :
            return ResponseStats(
                total = 56,
                took = 1.337,
        )

    def testResponseStats(self):
        """Test ResponseStats"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()