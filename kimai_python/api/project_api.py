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


class ProjectApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_projects_get(self, **kwargs):  # noqa: E501
        """Returns a collection of projects.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer: Customer ID to filter projects
        :param str customers: Comma separated list of customer IDs to filter projects
        :param str visible: Visibility status to filter projects. Allowed values: 1=visible, 2=hidden, 3=both (default: 1)
        :param str start: Only projects that started before this date will be included. Allowed format: HTML5 (default: now, if end is also empty)
        :param str end: Only projects that ended after this date will be included. Allowed format: HTML5 (default: now, if start is also empty)
        :param str ignore_dates: If set, start and end are completely ignored. Allowed values: 1 (default: off)
        :param str global_activities: If given, filters projects by their 'global activity' support. Allowed values: 1 (supports global activities) and 0 (without global activities) (default: all)
        :param str order: The result order. Allowed values: ASC, DESC (default: ASC)
        :param str order_by: The field by which results will be ordered. Allowed values: id, name, customer (default: name)
        :param str term: Free search term
        :return: list[ProjectCollection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_projects_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a collection of projects.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer: Customer ID to filter projects
        :param str customers: Comma separated list of customer IDs to filter projects
        :param str visible: Visibility status to filter projects. Allowed values: 1=visible, 2=hidden, 3=both (default: 1)
        :param str start: Only projects that started before this date will be included. Allowed format: HTML5 (default: now, if end is also empty)
        :param str end: Only projects that ended after this date will be included. Allowed format: HTML5 (default: now, if start is also empty)
        :param str ignore_dates: If set, start and end are completely ignored. Allowed values: 1 (default: off)
        :param str global_activities: If given, filters projects by their 'global activity' support. Allowed values: 1 (supports global activities) and 0 (without global activities) (default: all)
        :param str order: The result order. Allowed values: ASC, DESC (default: ASC)
        :param str order_by: The field by which results will be ordered. Allowed values: id, name, customer (default: name)
        :param str term: Free search term
        :return: list[ProjectCollection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer', 'customers', 'visible', 'start', 'end', 'ignore_dates', 'global_activities', 'order', 'order_by', 'term']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_projects_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer' in params:
            query_params.append(('customer', params['customer']))  # noqa: E501
        if 'customers' in params:
            query_params.append(('customers', params['customers']))  # noqa: E501
        if 'visible' in params:
            query_params.append(('visible', params['visible']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'ignore_dates' in params:
            query_params.append(('ignoreDates', params['ignore_dates']))  # noqa: E501
        if 'global_activities' in params:
            query_params.append(('globalActivities', params['global_activities']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'term' in params:
            query_params.append(('term', params['term']))  # noqa: E501

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
            '/api/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectCollection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_projects_id_get(self, id, **kwargs):  # noqa: E501
        """Returns one project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ProjectEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_projects_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns one project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ProjectEntity
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
                    " to method api_projects_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_projects_id_get`")  # noqa: E501

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
            '/api/projects/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_projects_id_meta_patch(self, id, **kwargs):  # noqa: E501
        """Sets the value of a meta-field for an existing project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_meta_patch(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Project record ID to set the meta-field value for (required)
        :param IdMetaBody2 body:
        :return: ProjectEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_id_meta_patch_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_id_meta_patch_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_projects_id_meta_patch_with_http_info(self, id, **kwargs):  # noqa: E501
        """Sets the value of a meta-field for an existing project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_meta_patch_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Project record ID to set the meta-field value for (required)
        :param IdMetaBody2 body:
        :return: ProjectEntity
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
                    " to method api_projects_id_meta_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_projects_id_meta_patch`")  # noqa: E501

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
            '/api/projects/{id}/meta', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_projects_id_patch(self, body, id, **kwargs):  # noqa: E501
        """Update an existing project  # noqa: E501

        Update an existing project, you can pass all or just a subset of all attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_patch(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectEditForm body: (required)
        :param int id: Project ID to update (required)
        :return: ProjectEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def api_projects_id_patch_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update an existing project  # noqa: E501

        Update an existing project, you can pass all or just a subset of all attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_patch_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectEditForm body: (required)
        :param int id: Project ID to update (required)
        :return: ProjectEntity
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
                    " to method api_projects_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_projects_id_patch`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_projects_id_patch`")  # noqa: E501

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
            '/api/projects/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_projects_id_rates_get(self, id, **kwargs):  # noqa: E501
        """Returns a collection of all rates for one project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_rates_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The project whose rates will be returned (required)
        :return: list[ProjectRate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_id_rates_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_id_rates_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_projects_id_rates_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns a collection of all rates for one project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_rates_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The project whose rates will be returned (required)
        :return: list[ProjectRate]
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
                    " to method api_projects_id_rates_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_projects_id_rates_get`")  # noqa: E501

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
            '/api/projects/{id}/rates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectRate]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_projects_id_rates_post(self, body, id, **kwargs):  # noqa: E501
        """Adds a new rate to an project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_rates_post(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectRateForm body: (required)
        :param int id: The project to add the rate for (required)
        :return: ProjectRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_id_rates_post_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_id_rates_post_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def api_projects_id_rates_post_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Adds a new rate to an project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_rates_post_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectRateForm body: (required)
        :param int id: The project to add the rate for (required)
        :return: ProjectRate
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
                    " to method api_projects_id_rates_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_projects_id_rates_post`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_projects_id_rates_post`")  # noqa: E501

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
            '/api/projects/{id}/rates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectRate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_projects_id_rates_rate_id_delete(self, id, rate_id, **kwargs):  # noqa: E501
        """Deletes one rate for an project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_rates_rate_id_delete(id, rate_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The project whose rate will be removed (required)
        :param int rate_id: The rate to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_id_rates_rate_id_delete_with_http_info(id, rate_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_id_rates_rate_id_delete_with_http_info(id, rate_id, **kwargs)  # noqa: E501
            return data

    def api_projects_id_rates_rate_id_delete_with_http_info(self, id, rate_id, **kwargs):  # noqa: E501
        """Deletes one rate for an project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_id_rates_rate_id_delete_with_http_info(id, rate_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The project whose rate will be removed (required)
        :param int rate_id: The rate to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'rate_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_projects_id_rates_rate_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_projects_id_rates_rate_id_delete`")  # noqa: E501
        # verify the required parameter 'rate_id' is set
        if ('rate_id' not in params or
                params['rate_id'] is None):
            raise ValueError("Missing the required parameter `rate_id` when calling `api_projects_id_rates_rate_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'rate_id' in params:
            path_params['rateId'] = params['rate_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/projects/{id}/rates/{rateId}', 'DELETE',
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

    def api_projects_post(self, body, **kwargs):  # noqa: E501
        """Creates a new project  # noqa: E501

        Creates a new project and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectEditForm body: (required)
        :return: ProjectEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_projects_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_projects_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_projects_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new project  # noqa: E501

        Creates a new project and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_projects_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectEditForm body: (required)
        :return: ProjectEntity
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
                    " to method api_projects_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_projects_post`")  # noqa: E501

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
            '/api/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
