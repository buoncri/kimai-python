# coding: utf-8

"""
    Kimai - API Docs

    JSON API for the Kimai time-tracking software: [API documentation](https://www.kimai.org/documentation/rest-api.html), [Swagger definition file](doc.json)   # noqa: E501

    OpenAPI spec version: 0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kimai_python.api_client import ApiClient


class ExpenseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_expenses_get(self, **kwargs):  # noqa: E501
        """Returns a collection of expenses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_by: The field by which results will be ordered. Allowed values: begin, end, duration, total, category, cost, user, customer, project, activity, description, exported, refundable, multiplier (default: begin)
        :param str order: The result order. Allowed values: ASC, DESC (default: DESC)
        :param str begin: Only records after this date will be included (format: HTML5)
        :param str end: Only records before this date will be included (format: HTML5)
        :param str refundable: Use this flag if you want to filter for refundable expenses. Allowed values: 0=not refundable, 1=refundable (default: all)
        :param str exported: Use this flag if you want to filter for export state. Allowed values: 0=not exported, 1=exported (default: all)
        :param str term: Free search term
        :param str page: The page to display, renders a 404 if not found (default: 1)
        :param str size: The amount of entries for each page (default: 50)
        :return: list[ExpenseEntity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_expenses_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a collection of expenses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_by: The field by which results will be ordered. Allowed values: begin, end, duration, total, category, cost, user, customer, project, activity, description, exported, refundable, multiplier (default: begin)
        :param str order: The result order. Allowed values: ASC, DESC (default: DESC)
        :param str begin: Only records after this date will be included (format: HTML5)
        :param str end: Only records before this date will be included (format: HTML5)
        :param str refundable: Use this flag if you want to filter for refundable expenses. Allowed values: 0=not refundable, 1=refundable (default: all)
        :param str exported: Use this flag if you want to filter for export state. Allowed values: 0=not exported, 1=exported (default: all)
        :param str term: Free search term
        :param str page: The page to display, renders a 404 if not found (default: 1)
        :param str size: The amount of entries for each page (default: 50)
        :return: list[ExpenseEntity]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_by', 'order', 'begin', 'end', 'refundable', 'exported', 'term', 'page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'begin' in params:
            query_params.append(('begin', params['begin']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'refundable' in params:
            query_params.append(('refundable', params['refundable']))  # noqa: E501
        if 'exported' in params:
            query_params.append(('exported', params['exported']))  # noqa: E501
        if 'term' in params:
            query_params.append(('term', params['term']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ExpenseEntity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_expenses_id_delete(self, id, **kwargs):  # noqa: E501
        """Delete an existing expense record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense record ID to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_expenses_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete an existing expense record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense record ID to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_expenses_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_expenses_id_duplicate_patch(self, id, **kwargs):  # noqa: E501
        """Duplicates an existing expense record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_duplicate_patch(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense record ID to duplicate (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_id_duplicate_patch_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_id_duplicate_patch_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_expenses_id_duplicate_patch_with_http_info(self, id, **kwargs):  # noqa: E501
        """Duplicates an existing expense record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_duplicate_patch_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense record ID to duplicate (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_id_duplicate_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_expenses_id_duplicate_patch`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses/{id}/duplicate', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpenseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_expenses_id_get(self, id, **kwargs):  # noqa: E501
        """Returns one expense  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense ID to fetch (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_expenses_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns one expense  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense ID to fetch (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_expenses_id_get`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpenseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_expenses_id_meta_patch(self, id, **kwargs):  # noqa: E501
        """Sets the value of a meta-field for an existing expense  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_meta_patch(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense record ID to set the meta-field value for (required)
        :param IdMetaBody4 body:
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_id_meta_patch_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_id_meta_patch_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_expenses_id_meta_patch_with_http_info(self, id, **kwargs):  # noqa: E501
        """Sets the value of a meta-field for an existing expense  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_meta_patch_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense record ID to set the meta-field value for (required)
        :param IdMetaBody4 body:
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_id_meta_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_expenses_id_meta_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses/{id}/meta', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpenseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_expenses_id_patch(self, body, id, **kwargs):  # noqa: E501
        """Update an existing expense  # noqa: E501

        Update an existing expense, you can pass all or just a subset of all attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_patch(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExpenseEditForm body: (required)
        :param int id: Expense ID to update (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def api_expenses_id_patch_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update an existing expense  # noqa: E501

        Update an existing expense, you can pass all or just a subset of all attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_id_patch_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExpenseEditForm body: (required)
        :param int id: Expense ID to update (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_expenses_id_patch`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_expenses_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpenseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_expenses_post(self, body, **kwargs):  # noqa: E501
        """Creates a new expense  # noqa: E501

        Creates a new expense and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExpenseEditForm body: (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_expenses_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_expenses_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_expenses_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new expense  # noqa: E501

        Creates a new expense and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_expenses_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExpenseEditForm body: (required)
        :return: ExpenseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_expenses_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_expenses_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/expenses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpenseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
