# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facets_by_index_facets_entity_get**](DefaultApi.md#facets_by_index_facets_entity_get) | **GET** /facets/{entity} | Facets By Index


# **facets_by_index_facets_entity_get**
> list[str] facets_by_index_facets_entity_get(entity)

Facets By Index

Return the available facet fields for an entity

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    entity = None # object | 

    try:
        # Facets By Index
        api_response = api_instance.facets_by_index_facets_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->facets_by_index_facets_entity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**object**](.md)|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

