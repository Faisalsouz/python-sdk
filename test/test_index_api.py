# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.index_api import IndexApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestIndexApi(unittest.TestCase):
    """IndexApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.index_api.IndexApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_economic_indices(self):
        """Test case for get_all_economic_indices

        Get All Economic Indices  # noqa: E501
        """
        pass

    def test_get_all_sic_indices(self):
        """Test case for get_all_sic_indices

        Get All SIC Indices  # noqa: E501
        """
        pass

    def test_get_all_stock_market_indices(self):
        """Test case for get_all_stock_market_indices

        Get All Stock Market Indices  # noqa: E501
        """
        pass

    def test_get_economic_index_by_id(self):
        """Test case for get_economic_index_by_id

        Get an Economic Index by ID  # noqa: E501
        """
        pass

    def test_get_economic_index_data_point_number(self):
        """Test case for get_economic_index_data_point_number

        Get Economic Index Data Point (Number)  # noqa: E501
        """
        pass

    def test_get_economic_index_data_point_text(self):
        """Test case for get_economic_index_data_point_text

        Get Economic Index Data Point (Text)  # noqa: E501
        """
        pass

    def test_get_economic_index_historical_data(self):
        """Test case for get_economic_index_historical_data

        Get Economic Index Historical Data  # noqa: E501
        """
        pass

    def test_get_sic_index_by_id(self):
        """Test case for get_sic_index_by_id

        Get an SIC Index by ID  # noqa: E501
        """
        pass

    def test_get_sic_index_data_point_number(self):
        """Test case for get_sic_index_data_point_number

        Get SIC Index Data Point (Number)  # noqa: E501
        """
        pass

    def test_get_sic_index_data_point_text(self):
        """Test case for get_sic_index_data_point_text

        Get SIC Index Data Point (Text)  # noqa: E501
        """
        pass

    def test_get_sic_index_historical_data(self):
        """Test case for get_sic_index_historical_data

        Get SIC Index Historical Data  # noqa: E501
        """
        pass

    def test_get_stock_market_index_by_id(self):
        """Test case for get_stock_market_index_by_id

        Get a Stock Market Index by ID  # noqa: E501
        """
        pass

    def test_get_stock_market_index_data_point_number(self):
        """Test case for get_stock_market_index_data_point_number

        Get Stock Market Index Data Point (Number)  # noqa: E501
        """
        pass

    def test_get_stock_market_index_data_point_text(self):
        """Test case for get_stock_market_index_data_point_text

        Get Stock Market Index Data Point (Text)  # noqa: E501
        """
        pass

    def test_get_stock_market_index_historical_data(self):
        """Test case for get_stock_market_index_historical_data

        Get Stock Market Index Historical Data  # noqa: E501
        """
        pass

    def test_search_economic_indices(self):
        """Test case for search_economic_indices

        Search Economic Indices  # noqa: E501
        """
        pass

    def test_search_sic_indices(self):
        """Test case for search_sic_indices

        Search SIC Indices  # noqa: E501
        """
        pass

    def test_search_stock_markets_indices(self):
        """Test case for search_stock_markets_indices

        Search Stock Market Indices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
