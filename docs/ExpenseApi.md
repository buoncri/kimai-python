# kimai_python.ExpenseApi

All URIs are relative to *//demo-plugins.kimai.org/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_expenses_get**](ExpenseApi.md#api_expenses_get) | **GET** /api/expenses | Returns a collection of expenses
[**api_expenses_id_delete**](ExpenseApi.md#api_expenses_id_delete) | **DELETE** /api/expenses/{id} | Delete an existing expense record
[**api_expenses_id_duplicate_patch**](ExpenseApi.md#api_expenses_id_duplicate_patch) | **PATCH** /api/expenses/{id}/duplicate | Duplicates an existing expense record
[**api_expenses_id_get**](ExpenseApi.md#api_expenses_id_get) | **GET** /api/expenses/{id} | Returns one expense
[**api_expenses_id_meta_patch**](ExpenseApi.md#api_expenses_id_meta_patch) | **PATCH** /api/expenses/{id}/meta | Sets the value of a meta-field for an existing expense
[**api_expenses_id_patch**](ExpenseApi.md#api_expenses_id_patch) | **PATCH** /api/expenses/{id} | Update an existing expense
[**api_expenses_post**](ExpenseApi.md#api_expenses_post) | **POST** /api/expenses | Creates a new expense

# **api_expenses_get**
> list[ExpenseEntity] api_expenses_get(order_by=order_by, order=order, begin=begin, end=end, refundable=refundable, exported=exported, term=term, page=page, size=size)

Returns a collection of expenses

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: begin, end, duration, total, category, cost, user, customer, project, activity, description, exported, refundable, multiplier (default: begin) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: DESC) (optional)
begin = 'begin_example' # str | Only records after this date will be included (format: HTML5) (optional)
end = 'end_example' # str | Only records before this date will be included (format: HTML5) (optional)
refundable = 'refundable_example' # str | Use this flag if you want to filter for refundable expenses. Allowed values: 0=not refundable, 1=refundable (default: all) (optional)
exported = 'exported_example' # str | Use this flag if you want to filter for export state. Allowed values: 0=not exported, 1=exported (default: all) (optional)
term = 'term_example' # str | Free search term (optional)
page = 'page_example' # str | The page to display, renders a 404 if not found (default: 1) (optional)
size = 'size_example' # str | The amount of entries for each page (default: 50) (optional)

try:
    # Returns a collection of expenses
    api_response = api_instance.api_expenses_get(order_by=order_by, order=order, begin=begin, end=end, refundable=refundable, exported=exported, term=term, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| The field by which results will be ordered. Allowed values: begin, end, duration, total, category, cost, user, customer, project, activity, description, exported, refundable, multiplier (default: begin) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: DESC) | [optional] 
 **begin** | **str**| Only records after this date will be included (format: HTML5) | [optional] 
 **end** | **str**| Only records before this date will be included (format: HTML5) | [optional] 
 **refundable** | **str**| Use this flag if you want to filter for refundable expenses. Allowed values: 0&#x3D;not refundable, 1&#x3D;refundable (default: all) | [optional] 
 **exported** | **str**| Use this flag if you want to filter for export state. Allowed values: 0&#x3D;not exported, 1&#x3D;exported (default: all) | [optional] 
 **term** | **str**| Free search term | [optional] 
 **page** | **str**| The page to display, renders a 404 if not found (default: 1) | [optional] 
 **size** | **str**| The amount of entries for each page (default: 50) | [optional] 

### Return type

[**list[ExpenseEntity]**](ExpenseEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_expenses_id_delete**
> api_expenses_id_delete(id)

Delete an existing expense record

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
id = 56 # int | Expense record ID to delete

try:
    # Delete an existing expense record
    api_instance.api_expenses_id_delete(id)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense record ID to delete | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_expenses_id_duplicate_patch**
> ExpenseEntity api_expenses_id_duplicate_patch(id)

Duplicates an existing expense record

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
id = 56 # int | Expense record ID to duplicate

try:
    # Duplicates an existing expense record
    api_response = api_instance.api_expenses_id_duplicate_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_id_duplicate_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense record ID to duplicate | 

### Return type

[**ExpenseEntity**](ExpenseEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_expenses_id_get**
> ExpenseEntity api_expenses_id_get(id)

Returns one expense

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
id = 56 # int | Expense ID to fetch

try:
    # Returns one expense
    api_response = api_instance.api_expenses_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense ID to fetch | 

### Return type

[**ExpenseEntity**](ExpenseEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_expenses_id_meta_patch**
> ExpenseEntity api_expenses_id_meta_patch(id, body=body)

Sets the value of a meta-field for an existing expense

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
id = 56 # int | Expense record ID to set the meta-field value for
body = kimai_python.IdMetaBody4() # IdMetaBody4 |  (optional)

try:
    # Sets the value of a meta-field for an existing expense
    api_response = api_instance.api_expenses_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_id_meta_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense record ID to set the meta-field value for | 
 **body** | [**IdMetaBody4**](IdMetaBody4.md)|  | [optional] 

### Return type

[**ExpenseEntity**](ExpenseEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_expenses_id_patch**
> ExpenseEntity api_expenses_id_patch(body, id)

Update an existing expense

Update an existing expense, you can pass all or just a subset of all attributes

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
body = kimai_python.ExpenseEditForm() # ExpenseEditForm | 
id = 56 # int | Expense ID to update

try:
    # Update an existing expense
    api_response = api_instance.api_expenses_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpenseEditForm**](ExpenseEditForm.md)|  | 
 **id** | **int**| Expense ID to update | 

### Return type

[**ExpenseEntity**](ExpenseEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_expenses_post**
> ExpenseEntity api_expenses_post(body)

Creates a new expense

Creates a new expense and returns it afterwards

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
api_instance = kimai_python.ExpenseApi(kimai_python.ApiClient(configuration))
body = kimai_python.ExpenseEditForm() # ExpenseEditForm | 

try:
    # Creates a new expense
    api_response = api_instance.api_expenses_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->api_expenses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpenseEditForm**](ExpenseEditForm.md)|  | 

### Return type

[**ExpenseEntity**](ExpenseEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

