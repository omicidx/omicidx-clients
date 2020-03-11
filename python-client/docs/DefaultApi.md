# omicidx_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**by_index_facets_entity_get**](DefaultApi.md#by_index_facets_entity_get) | **GET** /facets/{entity} | Facets By Index


# **by_index_facets_entity_get**
> list[str] by_index_facets_entity_get(entity)

Facets By Index

Return the available facet fields for an entity

### Example

```python
from __future__ import print_function
import time
import omicidx_client
from omicidx_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with omicidx_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = omicidx_client.DefaultApi(api_client)
    entity = None # object | 

    try:
        # Facets By Index
        api_response = api_instance.by_index_facets_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->by_index_facets_entity_get: %s\n" % e)
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

