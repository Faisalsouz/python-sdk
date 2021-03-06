# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class FilingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def filter_filings(self, company, **kwargs):  # noqa: E501
        """Filter Filings  # noqa: E501

        Returns Filings that match the specified filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_filings(company, async=True)
        >>> result = thread.get()

        :param async bool
        :param str company: Filings for the given `company` identifier (ticker, CIK, LEI, Intrinio ID) (required)
        :param str report_type: Filter by report type
        :param date start_date: Filed on or after the given date
        :param date end_date: Filed before or after the given date
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.filter_filings_with_http_info(company, **kwargs)  # noqa: E501
        else:
            (data) = self.filter_filings_with_http_info(company, **kwargs)  # noqa: E501
            return data

    def filter_filings_with_http_info(self, company, **kwargs):  # noqa: E501
        """Filter Filings  # noqa: E501

        Returns Filings that match the specified filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_filings_with_http_info(company, async=True)
        >>> result = thread.get()

        :param async bool
        :param str company: Filings for the given `company` identifier (ticker, CIK, LEI, Intrinio ID) (required)
        :param str report_type: Filter by report type
        :param date start_date: Filed on or after the given date
        :param date end_date: Filed before or after the given date
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company', 'report_type', 'start_date', 'end_date', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_filings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company' is set
        if ('company' not in params or
                params['company'] is None):
            raise ValueError("Missing the required parameter `company` when calling `filter_filings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company' in params:
            query_params.append(('company', params['company']))  # noqa: E501
        if 'report_type' in params:
            query_params.append(('report_type', params['report_type']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/filter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseFilings',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def filter_notes(self, **kwargs):  # noqa: E501
        """Filter SEC filing notes  # noqa: E501

        Returns SEC filing notes matching the supplied criteria  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_notes(async=True)
        >>> result = thread.get()

        :param async bool
        :param str company: A Company identifier (Ticker, CIK, LEI, Intrinio ID)
        :param str report_type: Notes contained in filings that match the given report type
        :param date filing_start_date: Limit search to filings on or after this date
        :param date filing_end_date: Limit search to filings on or before this date
        :param date period_ended_start_date: Limit search to filings with a period end date on or after this date
        :param date period_ended_end_date: Limit search to filings with a period end date on or before this date
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilingNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.filter_notes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_notes_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_notes_with_http_info(self, **kwargs):  # noqa: E501
        """Filter SEC filing notes  # noqa: E501

        Returns SEC filing notes matching the supplied criteria  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.filter_notes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str company: A Company identifier (Ticker, CIK, LEI, Intrinio ID)
        :param str report_type: Notes contained in filings that match the given report type
        :param date filing_start_date: Limit search to filings on or after this date
        :param date filing_end_date: Limit search to filings on or before this date
        :param date period_ended_start_date: Limit search to filings with a period end date on or after this date
        :param date period_ended_end_date: Limit search to filings with a period end date on or before this date
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilingNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company', 'report_type', 'filing_start_date', 'filing_end_date', 'period_ended_start_date', 'period_ended_end_date', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_notes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company' in params:
            query_params.append(('company', params['company']))  # noqa: E501
        if 'report_type' in params:
            query_params.append(('report_type', params['report_type']))  # noqa: E501
        if 'filing_start_date' in params:
            query_params.append(('filing_start_date', params['filing_start_date']))  # noqa: E501
        if 'filing_end_date' in params:
            query_params.append(('filing_end_date', params['filing_end_date']))  # noqa: E501
        if 'period_ended_start_date' in params:
            query_params.append(('period_ended_start_date', params['period_ended_start_date']))  # noqa: E501
        if 'period_ended_end_date' in params:
            query_params.append(('period_ended_end_date', params['period_ended_end_date']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/notes/filter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseFilingNotes',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_filings(self, **kwargs):  # noqa: E501
        """All Filings  # noqa: E501

        Returns all Filings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_filings(async=True)
        >>> result = thread.get()

        :param async bool
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_filings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_filings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_filings_with_http_info(self, **kwargs):  # noqa: E501
        """All Filings  # noqa: E501

        Returns all Filings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_filings_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_filings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseFilings',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_notes(self, **kwargs):  # noqa: E501
        """Get All SEC filing notes  # noqa: E501

        Return All notes from SEC Filings, most-recent first  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_notes(async=True)
        >>> result = thread.get()

        :param async bool
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilingNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_notes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_notes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_notes_with_http_info(self, **kwargs):  # noqa: E501
        """Get All SEC filing notes  # noqa: E501

        Return All notes from SEC Filings, most-recent first  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_notes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseFilingNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_notes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/notes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseFilingNotes',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_filing_by_id(self, id, **kwargs):  # noqa: E501
        """Lookup Filing  # noqa: E501

        Returns the Filing with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filing_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID of the Filing (required)
        :return: Filing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_filing_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_filing_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_filing_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Lookup Filing  # noqa: E501

        Returns the Filing with the given `identifier`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filing_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID of the Filing (required)
        :return: Filing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_filing_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_filing_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Filing',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_note(self, identifier, **kwargs):  # noqa: E501
        """Get an SEC filing note by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_note(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID of the filing note (required)
        :param str content_format: Returns content in html (as filed) or plain text
        :return: FilingNote
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_note_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_note_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get an SEC filing note by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_note_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID of the filing note (required)
        :param str content_format: Returns content in html (as filed) or plain text
        :return: FilingNote
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'content_format']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_note`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'content_format' in params:
            query_params.append(('content_format', params['content_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/notes/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilingNote',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_note_html(self, identifier, **kwargs):  # noqa: E501
        """Returns the content of an SEC filing note as originally filed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_note_html(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID of the filing note (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_note_html_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_html_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_note_html_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Returns the content of an SEC filing note as originally filed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_note_html_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID of the filing note (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_html" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_note_html`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/notes/{identifier}/html', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_note_text(self, identifier, **kwargs):  # noqa: E501
        """Returns the content of an SEC filing note stripped of HTML  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_note_text(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID of the filing note (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_note_text_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_text_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_note_text_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Returns the content of an SEC filing note stripped of HTML  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_note_text_with_http_info(identifier, async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: The Intrinio ID of the filing note (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_text" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_note_text`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/notes/{identifier}/text', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_notes(self, query, **kwargs):  # noqa: E501
        """Search Filing Notes  # noqa: E501

        Searches SEC filing notes using the text in `query`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_notes(query, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: Search for notes that contain all or parts of this text (required)
        :param date filing_start_date: Limit search to filings on or after this date
        :param date filing_end_date: Limit search to filings on or before this date
        :param float page_size: The number of results to return
        :return: ApiResponseFilingNotesSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_notes_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_notes_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_notes_with_http_info(self, query, **kwargs):  # noqa: E501
        """Search Filing Notes  # noqa: E501

        Searches SEC filing notes using the text in `query`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_notes_with_http_info(query, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query: Search for notes that contain all or parts of this text (required)
        :param date filing_start_date: Limit search to filings on or after this date
        :param date filing_end_date: Limit search to filings on or before this date
        :param float page_size: The number of results to return
        :return: ApiResponseFilingNotesSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'filing_start_date', 'filing_end_date', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_notes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_notes`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `search_notes`, must be a value less than or equal to `1000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'filing_start_date' in params:
            query_params.append(('filing_start_date', params['filing_start_date']))  # noqa: E501
        if 'filing_end_date' in params:
            query_params.append(('filing_end_date', params['filing_end_date']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/filings/notes/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseFilingNotesSearch',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
