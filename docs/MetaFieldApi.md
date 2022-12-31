# kimai_python.MetaFieldApi

All URIs are relative to *//demo-plugins.kimai.org/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_metafields_get**](MetaFieldApi.md#api_metafields_get) | **GET** /api/metafields | Returns a collection of meta-fields

# **api_metafields_get**
> list[MetaFieldRule] api_metafields_get(entity=entity)

Returns a collection of meta-fields

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
api_instance = kimai_python.MetaFieldApi(kimai_python.ApiClient(configuration))
entity = 'entity_example' # str | The type of object to fetch meta-fields for. Allowed values: timesheet, customer, project, activity, user, expense - returns all if not given (default: all) (optional)

try:
    # Returns a collection of meta-fields
    api_response = api_instance.api_metafields_get(entity=entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetaFieldApi->api_metafields_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The type of object to fetch meta-fields for. Allowed values: timesheet, customer, project, activity, user, expense - returns all if not given (default: all) | [optional] 

### Return type

[**list[MetaFieldRule]**](MetaFieldRule.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

