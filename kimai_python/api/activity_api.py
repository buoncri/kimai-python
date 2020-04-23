# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen.   # noqa: E501

    OpenAPI spec version: 0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kimai_python.api_client import ApiClient


class ActivityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_activities_get(self, **kwargs):  # noqa: E501
        """Returns a collection of activities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project: Project ID to filter activities
        :param str projects: Comma separated list of project IDs to filter activities
        :param str visible: Visibility status to filter activities. Allowed values: 1=visible, 2=hidden, 3=all (default: 1)
        :param str globals: Use if you want to fetch only global activities. Allowed values: true (default: false)
        :param str globals_first: Deprecated parameter, value is not used any more
        :param str order_by: The field by which results will be ordered. Allowed values: id, name, project (default: name)
        :param str order: The result order. Allowed values: ASC, DESC (default: ASC)
        :param str term: Free search term
        :return: list[ActivityCollection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_activities_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a collection of activities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project: Project ID to filter activities
        :param str projects: Comma separated list of project IDs to filter activities
        :param str visible: Visibility status to filter activities. Allowed values: 1=visible, 2=hidden, 3=all (default: 1)
        :param str globals: Use if you want to fetch only global activities. Allowed values: true (default: false)
        :param str globals_first: Deprecated parameter, value is not used any more
        :param str order_by: The field by which results will be ordered. Allowed values: id, name, project (default: name)
        :param str order: The result order. Allowed values: ASC, DESC (default: ASC)
        :param str term: Free search term
        :return: list[ActivityCollection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project', 'projects', 'visible', 'globals', 'globals_first', 'order_by', 'order', 'term']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_activities_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'project' in params and not re.search(r'\\d+', params['project']):  # noqa: E501
            raise ValueError("Invalid value for parameter `project` when calling `api_activities_get`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'projects' in params and not re.search(r'[\\d|,]+', params['projects']):  # noqa: E501
            raise ValueError("Invalid value for parameter `projects` when calling `api_activities_get`, must conform to the pattern `/[\\d|,]+/`")  # noqa: E501
        if 'visible' in params and not re.search(r'1|2|3', params['visible']):  # noqa: E501
            raise ValueError("Invalid value for parameter `visible` when calling `api_activities_get`, must conform to the pattern `/1|2|3/`")  # noqa: E501
        if 'globals' in params and not re.search(r'true', params['globals']):  # noqa: E501
            raise ValueError("Invalid value for parameter `globals` when calling `api_activities_get`, must conform to the pattern `/true/`")  # noqa: E501
        if 'globals_first' in params and not re.search(r'true|false', params['globals_first']):  # noqa: E501
            raise ValueError("Invalid value for parameter `globals_first` when calling `api_activities_get`, must conform to the pattern `/true|false/`")  # noqa: E501
        if 'order_by' in params and not re.search(r'id|name|project', params['order_by']):  # noqa: E501
            raise ValueError("Invalid value for parameter `order_by` when calling `api_activities_get`, must conform to the pattern `/id|name|project/`")  # noqa: E501
        if 'order' in params and not re.search(r'ASC|DESC', params['order']):  # noqa: E501
            raise ValueError("Invalid value for parameter `order` when calling `api_activities_get`, must conform to the pattern `/ASC|DESC/`")  # noqa: E501
        if 'term' in params and not re.search(r'[a-zA-Z0-9 \\-,:]+', params['term']):  # noqa: E501
            raise ValueError("Invalid value for parameter `term` when calling `api_activities_get`, must conform to the pattern `/[a-zA-Z0-9 \\-,:]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project' in params:
            query_params.append(('project', params['project']))  # noqa: E501
        if 'projects' in params:
            query_params.append(('projects', params['projects']))  # noqa: E501
        if 'visible' in params:
            query_params.append(('visible', params['visible']))  # noqa: E501
        if 'globals' in params:
            query_params.append(('globals', params['globals']))  # noqa: E501
        if 'globals_first' in params:
            query_params.append(('globalsFirst', params['globals_first']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'term' in params:
            query_params.append(('term', params['term']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ActivityCollection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_activities_id_get(self, id, **kwargs):  # noqa: E501
        """Returns one activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Activity ID to fetch (required)
        :return: ActivityEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_activities_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns one activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Activity ID to fetch (required)
        :return: ActivityEntity
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
                    " to method api_activities_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_activities_id_get`")  # noqa: E501

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
            '/api/activities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_activities_id_meta_patch(self, id, **kwargs):  # noqa: E501
        """Sets the value of a meta-field for an existing activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_meta_patch(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Activity record ID to set the meta-field value for (required)
        :param Body body:
        :return: ActivityEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_id_meta_patch_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_id_meta_patch_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_activities_id_meta_patch_with_http_info(self, id, **kwargs):  # noqa: E501
        """Sets the value of a meta-field for an existing activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_meta_patch_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Activity record ID to set the meta-field value for (required)
        :param Body body:
        :return: ActivityEntity
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
                    " to method api_activities_id_meta_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_activities_id_meta_patch`")  # noqa: E501

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
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}/meta', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_activities_id_patch(self, body, id, **kwargs):  # noqa: E501
        """Update an existing activity  # noqa: E501

        Update an existing activity, you can pass all or just a subset of all attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_patch(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActivityEditForm body: (required)
        :param int id: Activity ID to update (required)
        :return: ActivityEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_id_patch_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def api_activities_id_patch_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update an existing activity  # noqa: E501

        Update an existing activity, you can pass all or just a subset of all attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_patch_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActivityEditForm body: (required)
        :param int id: Activity ID to update (required)
        :return: ActivityEntity
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
                    " to method api_activities_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_activities_id_patch`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_activities_id_patch`")  # noqa: E501

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
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_activities_id_rates_get(self, id, **kwargs):  # noqa: E501
        """Returns a collection of all rates for one activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_rates_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The activity whose rates will be returned (required)
        :return: list[ActivityRate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_id_rates_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_id_rates_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_activities_id_rates_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns a collection of all rates for one activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_rates_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The activity whose rates will be returned (required)
        :return: list[ActivityRate]
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
                    " to method api_activities_id_rates_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_activities_id_rates_get`")  # noqa: E501

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
            '/api/activities/{id}/rates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ActivityRate]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_activities_id_rates_post(self, id, body, **kwargs):  # noqa: E501
        """Adds a new rate to an activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_rates_post(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The activity to add the rate for (required)
        :param ActivityRateForm body: (required)
        :return: ActivityRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_id_rates_post_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_id_rates_post_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def api_activities_id_rates_post_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Adds a new rate to an activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_rates_post_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The activity to add the rate for (required)
        :param ActivityRateForm body: (required)
        :return: ActivityRate
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
                    " to method api_activities_id_rates_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_activities_id_rates_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_activities_id_rates_post`")  # noqa: E501

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
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}/rates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityRate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_activities_id_rates_rate_id_delete(self, id, rate_id, **kwargs):  # noqa: E501
        """Deletes one rate for an activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_rates_rate_id_delete(id, rate_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The activity whose rate will be removed (required)
        :param int rate_id: The rate to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_id_rates_rate_id_delete_with_http_info(id, rate_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_id_rates_rate_id_delete_with_http_info(id, rate_id, **kwargs)  # noqa: E501
            return data

    def api_activities_id_rates_rate_id_delete_with_http_info(self, id, rate_id, **kwargs):  # noqa: E501
        """Deletes one rate for an activity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_id_rates_rate_id_delete_with_http_info(id, rate_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The activity whose rate will be removed (required)
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
                    " to method api_activities_id_rates_rate_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_activities_id_rates_rate_id_delete`")  # noqa: E501
        # verify the required parameter 'rate_id' is set
        if ('rate_id' not in params or
                params['rate_id'] is None):
            raise ValueError("Missing the required parameter `rate_id` when calling `api_activities_id_rates_rate_id_delete`")  # noqa: E501

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
            '/api/activities/{id}/rates/{rateId}', 'DELETE',
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

    def api_activities_post(self, body, **kwargs):  # noqa: E501
        """Creates a new activity  # noqa: E501

        Creates a new activity and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActivityEditForm body: (required)
        :return: ActivityEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_activities_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_activities_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_activities_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new activity  # noqa: E501

        Creates a new activity and returns it afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_activities_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActivityEditForm body: (required)
        :return: ActivityEntity
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
                    " to method api_activities_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_activities_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['apiToken', 'apiUser']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
