# openapi_client.BiosampleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**biosample_by_accession_biosample_samples_accession_get**](BiosampleApi.md#biosample_by_accession_biosample_samples_accession_get) | **GET** /biosample/samples/{accession} | Biosample By Accession
[**biosample_by_accession_biosample_samples_accession_get_0**](BiosampleApi.md#biosample_by_accession_biosample_samples_accession_get_0) | **GET** /biosample/samples/{accession} | Biosample By Accession
[**biosamples_biosample_samples_get**](BiosampleApi.md#biosamples_biosample_samples_get) | **GET** /biosample/samples | Biosamples
[**biosamples_biosample_samples_get_0**](BiosampleApi.md#biosamples_biosample_samples_get_0) | **GET** /biosample/samples | Biosamples
[**mapping_biosample_fields_entity_get**](BiosampleApi.md#mapping_biosample_fields_entity_get) | **GET** /biosample/fields/{entity} | Mapping


# **biosample_by_accession_biosample_samples_accession_get**
> object biosample_by_accession_biosample_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Biosample By Accession

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
    api_instance = openapi_client.BiosampleApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Biosample By Accession
        api_response = api_instance.biosample_by_accession_biosample_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiosampleApi->biosample_by_accession_biosample_samples_accession_get: %s\n" % e)
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

# **biosample_by_accession_biosample_samples_accession_get_0**
> object biosample_by_accession_biosample_samples_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Biosample By Accession

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
    api_instance = openapi_client.BiosampleApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Biosample By Accession
        api_response = api_instance.biosample_by_accession_biosample_samples_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiosampleApi->biosample_by_accession_biosample_samples_accession_get_0: %s\n" % e)
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

# **biosamples_biosample_samples_get**
> ResponseModel biosamples_biosample_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Biosamples

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
    api_instance = openapi_client.BiosampleApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Biosamples
        api_response = api_instance.biosamples_biosample_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiosampleApi->biosamples_biosample_samples_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) | [optional] 
 **size** | **int**|  | [optional] [default to 10]
 **cursor** | **str**| The cursor is used to scroll through results. For a query with more results than &#x60;size&#x60;, the result will include &#x60;cursor&#x60; in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the &#x60;cursor&#x60; will again be empty in the result json. | [optional] 
 **facet_size** | **int**| The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. | [optional] [default to 10]
 **include_fields** | [**list[str]**](str.md)| Fields to include in results. The default is to all fields (*) | [optional] [default to []]
 **exclude_fields** | [**list[str]**](str.md)| Fields to exclude from results. The default is to not exclude any fields.  | [optional] [default to []]
 **facets** | [**list[str]**](str.md)| A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. | [optional] [default to []]

### Return type

[**ResponseModel**](ResponseModel.md)

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

# **biosamples_biosample_samples_get_0**
> ResponseModel biosamples_biosample_samples_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Biosamples

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
    api_instance = openapi_client.BiosampleApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Biosamples
        api_response = api_instance.biosamples_biosample_samples_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiosampleApi->biosamples_biosample_samples_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) | [optional] 
 **size** | **int**|  | [optional] [default to 10]
 **cursor** | **str**| The cursor is used to scroll through results. For a query with more results than &#x60;size&#x60;, the result will include &#x60;cursor&#x60; in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the &#x60;cursor&#x60; will again be empty in the result json. | [optional] 
 **facet_size** | **int**| The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. | [optional] [default to 10]
 **include_fields** | [**list[str]**](str.md)| Fields to include in results. The default is to all fields (*) | [optional] [default to []]
 **exclude_fields** | [**list[str]**](str.md)| Fields to exclude from results. The default is to not exclude any fields.  | [optional] [default to []]
 **facets** | [**list[str]**](str.md)| A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. | [optional] [default to []]

### Return type

[**ResponseModel**](ResponseModel.md)

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

# **mapping_biosample_fields_entity_get**
> object mapping_biosample_fields_entity_get(entity)

Mapping

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
    api_instance = openapi_client.BiosampleApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Mapping
        api_response = api_instance.mapping_biosample_fields_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiosampleApi->mapping_biosample_fields_entity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 

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

