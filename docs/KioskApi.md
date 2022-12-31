# kimai_python.KioskApi

All URIs are relative to *//demo-plugins.kimai.org/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_kiosks_get**](KioskApi.md#api_kiosks_get) | **GET** /api/kiosks | Returns a collection of UserAuthCodes objects
[**api_kiosks_id_get**](KioskApi.md#api_kiosks_id_get) | **GET** /api/kiosks/{id} | Returns one UserAuthCodes entity

# **api_kiosks_get**
> list[UserAuthCodes] api_kiosks_get(order_by=order_by, order=order, page=page, size=size)

Returns a collection of UserAuthCodes objects

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
api_instance = kimai_python.KioskApi(kimai_python.ApiClient(configuration))
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, user, type, code (default: id) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: DESC) (optional)
page = 'page_example' # str | The page to display, renders a 404 if not found (default: 1) (optional)
size = 'size_example' # str | The amount of entries for each page (default: 50) (optional)

try:
    # Returns a collection of UserAuthCodes objects
    api_response = api_instance.api_kiosks_get(order_by=order_by, order=order, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KioskApi->api_kiosks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, user, type, code (default: id) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: DESC) | [optional] 
 **page** | **str**| The page to display, renders a 404 if not found (default: 1) | [optional] 
 **size** | **str**| The amount of entries for each page (default: 50) | [optional] 

### Return type

[**list[UserAuthCodes]**](UserAuthCodes.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_kiosks_id_get**
> UserAuthCodes api_kiosks_id_get(id)

Returns one UserAuthCodes entity

Creates the code for the configured default type (if not yet existing).

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
api_instance = kimai_python.KioskApi(kimai_python.ApiClient(configuration))
id = 56 # int | User ID to fetch

try:
    # Returns one UserAuthCodes entity
    api_response = api_instance.api_kiosks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KioskApi->api_kiosks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID to fetch | 

### Return type

[**UserAuthCodes**](UserAuthCodes.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

