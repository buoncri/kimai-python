# kimai_python.TaskApi

All URIs are relative to *//demo-plugins.kimai.org/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tasks_get**](TaskApi.md#api_tasks_get) | **GET** /api/tasks | Returns a collection of tasks
[**api_tasks_id_assign_patch**](TaskApi.md#api_tasks_id_assign_patch) | **PATCH** /api/tasks/{id}/assign | Assign a task to the current user
[**api_tasks_id_close_patch**](TaskApi.md#api_tasks_id_close_patch) | **PATCH** /api/tasks/{id}/close | Close a task for the current user
[**api_tasks_id_delete**](TaskApi.md#api_tasks_id_delete) | **DELETE** /api/tasks/{id} | Delete an existing task record
[**api_tasks_id_get**](TaskApi.md#api_tasks_id_get) | **GET** /api/tasks/{id} | Returns one task
[**api_tasks_id_log_patch**](TaskApi.md#api_tasks_id_log_patch) | **PATCH** /api/tasks/{id}/log | Logs work for a task record
[**api_tasks_id_patch**](TaskApi.md#api_tasks_id_patch) | **PATCH** /api/tasks/{id} | Update an existing task
[**api_tasks_id_reopen_patch**](TaskApi.md#api_tasks_id_reopen_patch) | **PATCH** /api/tasks/{id}/reopen | Reopens a task for the current user
[**api_tasks_id_start_patch**](TaskApi.md#api_tasks_id_start_patch) | **PATCH** /api/tasks/{id}/start | Start a task record
[**api_tasks_id_stop_patch**](TaskApi.md#api_tasks_id_stop_patch) | **PATCH** /api/tasks/{id}/stop | Stops a task record for the current user
[**api_tasks_id_unassign_patch**](TaskApi.md#api_tasks_id_unassign_patch) | **PATCH** /api/tasks/{id}/unassign | Unassign a task from the current user
[**api_tasks_post**](TaskApi.md#api_tasks_post) | **POST** /api/tasks | Creates a new Task

# **api_tasks_get**
> list[Task] api_tasks_get(body)

Returns a collection of tasks

Attention: This is a GET request and you can pass in every field of the form as query parameter. Array values need to be written like this: /api/tasks?projects[]=1&projects[]=2

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TaskApi(kimai_python.ApiClient(configuration))
body = kimai_python.TaskQuery() # TaskQuery | Attention: This is a GET request and you can pass in every field of the form as query parameter.

try:
    # Returns a collection of tasks
    api_response = api_instance.api_tasks_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskQuery**](TaskQuery.md)| Attention: This is a GET request and you can pass in every field of the form as query parameter. | 

### Return type

[**list[Task]**](Task.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_assign_patch**
> Task api_tasks_id_assign_patch(id)

Assign a task to the current user

Assign a currently unassigned task to the current user

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task ID to update

try:
    # Assign a task to the current user
    api_response = api_instance.api_tasks_id_assign_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_assign_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to update | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_close_patch**
> Task api_tasks_id_close_patch(id)

Close a task for the current user

Closes an assigned task for the current user

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task ID to close

try:
    # Close a task for the current user
    api_response = api_instance.api_tasks_id_close_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_close_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to close | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_delete**
> api_tasks_id_delete(id)

Delete an existing task record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task record ID to delete

try:
    # Delete an existing task record
    api_instance.api_tasks_id_delete(id)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task record ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_get**
> Task api_tasks_id_get(id)

Returns one task

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TaskApi(kimai_python.ApiClient(configuration))
id = 56 # int | Task ID to fetch

try:
    # Returns one task
    api_response = api_instance.api_tasks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to fetch | 

### Return type

[**Task**](Task.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_log_patch**
> TimesheetEntityExpanded api_tasks_id_log_patch(body, id)

Logs work for a task record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
body = kimai_python.TaskLogWorkForm() # TaskLogWorkForm | 
id = 56 # int | Task ID to log times for

try:
    # Logs work for a task record
    api_response = api_instance.api_tasks_id_log_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_log_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskLogWorkForm**](TaskLogWorkForm.md)|  | 
 **id** | **int**| Task ID to log times for | 

### Return type

[**TimesheetEntityExpanded**](TimesheetEntityExpanded.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_patch**
> Task api_tasks_id_patch(body, id)

Update an existing task

Update an existing task, you can pass all or just a subset of all attributes

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TaskApi(kimai_python.ApiClient(configuration))
body = kimai_python.TaskEditForm() # TaskEditForm | 
id = 56 # int | Task ID to update

try:
    # Update an existing task
    api_response = api_instance.api_tasks_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskEditForm**](TaskEditForm.md)|  | 
 **id** | **int**| Task ID to update | 

### Return type

[**Task**](Task.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_reopen_patch**
> Task api_tasks_id_reopen_patch(id)

Reopens a task for the current user

Reopens an assigned task for the current user

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task ID to reopen

try:
    # Reopens a task for the current user
    api_response = api_instance.api_tasks_id_reopen_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_reopen_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to reopen | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_start_patch**
> Task api_tasks_id_start_patch(id)

Start a task record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task ID to start

try:
    # Start a task record
    api_response = api_instance.api_tasks_id_start_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_start_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to start | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_stop_patch**
> Task api_tasks_id_stop_patch(id)

Stops a task record for the current user

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task ID to stop

try:
    # Stops a task record for the current user
    api_response = api_instance.api_tasks_id_stop_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_stop_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to stop | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_unassign_patch**
> Task api_tasks_id_unassign_patch(id)

Unassign a task from the current user

Unassign a currently assigned task from the current user

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kimai_python.TaskApi()
id = 56 # int | Task ID to update

try:
    # Unassign a task from the current user
    api_response = api_instance.api_tasks_id_unassign_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_id_unassign_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID to update | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_post**
> Task api_tasks_post(body)

Creates a new Task

Creates a new task and returns it afterwards

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TaskApi(kimai_python.ApiClient(configuration))
body = kimai_python.TaskEditForm() # TaskEditForm | 

try:
    # Creates a new Task
    api_response = api_instance.api_tasks_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskEditForm**](TaskEditForm.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

