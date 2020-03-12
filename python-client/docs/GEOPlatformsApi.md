# omicidx_client.GEOPlatformsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**by_accession_geo_platform_accession_get**](GEOPlatformsApi.md#by_accession_geo_platform_accession_get) | **GET** /geo/platform/{accession} | Platform By Accession


# **by_accession_geo_platform_accession_get**
> object by_accession_geo_platform_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Platform By Accession

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
    api_instance = omicidx_client.GEOPlatformsApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Platform By Accession
        api_response = api_instance.by_accession_geo_platform_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOPlatformsApi->by_accession_geo_platform_accession_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| An accession for lookup | 
 **include_fields** | [**list[str]**](str.md)| Fields to include in results. The default is to all fields (*) | [optional] [default to []]
 **exclude_fields** | [**list[str]**](str.md)| Fields to exclude from results. The default is to not exclude any fields.  | [optional] [default to []]

### Return type

**object**

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

