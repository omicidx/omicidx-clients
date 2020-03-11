# openapi_client.GEOApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapping_geo_fields_entity_get**](GEOApi.md#mapping_geo_fields_entity_get) | **GET** /geo/fields/{entity} | Mapping
[**platform_by_accession_geo_platform_accession_get**](GEOApi.md#platform_by_accession_geo_platform_accession_get) | **GET** /geo/platform/{accession} | Platform By Accession
[**platform_by_accession_geo_platform_accession_get_0**](GEOApi.md#platform_by_accession_geo_platform_accession_get_0) | **GET** /geo/platform/{accession} | Platform By Accession
[**platform_geo_platforms_get**](GEOApi.md#platform_geo_platforms_get) | **GET** /geo/platforms | Platform
[**platform_geo_platforms_get_0**](GEOApi.md#platform_geo_platforms_get_0) | **GET** /geo/platforms | Platform
[**sample_by_accession_geo_samples_accession_get**](GEOApi.md#sample_by_accession_geo_samples_accession_get) | **GET** /geo/samples/{accession} | Sample By Accession
[**sample_by_accession_geo_samples_accession_get_0**](GEOApi.md#sample_by_accession_geo_samples_accession_get_0) | **GET** /geo/samples/{accession} | Sample By Accession
[**samples_for_platform_geo_platforms_accession_samples_get**](GEOApi.md#samples_for_platform_geo_platforms_accession_samples_get) | **GET** /geo/platforms/{accession}/samples | Samples For Platform
[**samples_for_platform_geo_platforms_accession_samples_get_0**](GEOApi.md#samples_for_platform_geo_platforms_accession_samples_get_0) | **GET** /geo/platforms/{accession}/samples | Samples For Platform
[**samples_geo_samples_get**](GEOApi.md#samples_geo_samples_get) | **GET** /geo/samples | Samples
[**samples_geo_samples_get_0**](GEOApi.md#samples_geo_samples_get_0) | **GET** /geo/samples | Samples
[**series_by_accession_geo_series_accession_get**](GEOApi.md#series_by_accession_geo_series_accession_get) | **GET** /geo/series/{accession} | Series By Accession
[**series_by_accession_geo_series_accession_get_0**](GEOApi.md#series_by_accession_geo_series_accession_get_0) | **GET** /geo/series/{accession} | Series By Accession
[**series_geo_series_get**](GEOApi.md#series_geo_series_get) | **GET** /geo/series | Series
[**series_geo_series_get_0**](GEOApi.md#series_geo_series_get_0) | **GET** /geo/series | Series


# **mapping_geo_fields_entity_get**
> object mapping_geo_fields_entity_get(entity)

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
    api_instance = openapi_client.GEOApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Mapping
        api_response = api_instance.mapping_geo_fields_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->mapping_geo_fields_entity_get: %s\n" % e)
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

# **platform_by_accession_geo_platform_accession_get**
> object platform_by_accession_geo_platform_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Platform By Accession

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Platform By Accession
        api_response = api_instance.platform_by_accession_geo_platform_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->platform_by_accession_geo_platform_accession_get: %s\n" % e)
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

# **platform_by_accession_geo_platform_accession_get_0**
> object platform_by_accession_geo_platform_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Platform By Accession

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Platform By Accession
        api_response = api_instance.platform_by_accession_geo_platform_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->platform_by_accession_geo_platform_accession_get_0: %s\n" % e)
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

# **platform_geo_platforms_get**
> ResponseModel platform_geo_platforms_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Platform

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
    api_instance = openapi_client.GEOApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Platform
        api_response = api_instance.platform_geo_platforms_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->platform_geo_platforms_get: %s\n" % e)
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

# **platform_geo_platforms_get_0**
> ResponseModel platform_geo_platforms_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Platform

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
    api_instance = openapi_client.GEOApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Platform
        api_response = api_instance.platform_geo_platforms_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->platform_geo_platforms_get_0: %s\n" % e)
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

# **sample_by_accession_geo_samples_accession_get**
> object sample_by_accession_geo_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Sample By Accession

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Sample By Accession
        api_response = api_instance.sample_by_accession_geo_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->sample_by_accession_geo_samples_accession_get: %s\n" % e)
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

# **sample_by_accession_geo_samples_accession_get_0**
> object sample_by_accession_geo_samples_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Sample By Accession

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Sample By Accession
        api_response = api_instance.sample_by_accession_geo_samples_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->sample_by_accession_geo_samples_accession_get_0: %s\n" % e)
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

# **samples_for_platform_geo_platforms_accession_samples_get**
> object samples_for_platform_geo_platforms_accession_samples_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Samples For Platform

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Samples For Platform
        api_response = api_instance.samples_for_platform_geo_platforms_accession_samples_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->samples_for_platform_geo_platforms_accession_samples_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| An accession for lookup | 
 **include_fields** | [**list[str]**](str.md)| Fields to include in results. The default is to all fields (*) | [optional] [default to []]
 **exclude_fields** | [**list[str]**](str.md)| Fields to exclude from results. The default is to not exclude any fields.  | [optional] [default to []]
 **size** | **int**|  | [optional] [default to 10]
 **cursor** | **str**|  | [optional] 

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

# **samples_for_platform_geo_platforms_accession_samples_get_0**
> object samples_for_platform_geo_platforms_accession_samples_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Samples For Platform

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Samples For Platform
        api_response = api_instance.samples_for_platform_geo_platforms_accession_samples_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->samples_for_platform_geo_platforms_accession_samples_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| An accession for lookup | 
 **include_fields** | [**list[str]**](str.md)| Fields to include in results. The default is to all fields (*) | [optional] [default to []]
 **exclude_fields** | [**list[str]**](str.md)| Fields to exclude from results. The default is to not exclude any fields.  | [optional] [default to []]
 **size** | **int**|  | [optional] [default to 10]
 **cursor** | **str**|  | [optional] 

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

# **samples_geo_samples_get**
> ResponseModel samples_geo_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Samples

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
    api_instance = openapi_client.GEOApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Samples
        api_response = api_instance.samples_geo_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->samples_geo_samples_get: %s\n" % e)
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

# **samples_geo_samples_get_0**
> ResponseModel samples_geo_samples_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Samples

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
    api_instance = openapi_client.GEOApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Samples
        api_response = api_instance.samples_geo_samples_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->samples_geo_samples_get_0: %s\n" % e)
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

# **series_by_accession_geo_series_accession_get**
> object series_by_accession_geo_series_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Series By Accession

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Series By Accession
        api_response = api_instance.series_by_accession_geo_series_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->series_by_accession_geo_series_accession_get: %s\n" % e)
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

# **series_by_accession_geo_series_accession_get_0**
> object series_by_accession_geo_series_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Series By Accession

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
    api_instance = openapi_client.GEOApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Series By Accession
        api_response = api_instance.series_by_accession_geo_series_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->series_by_accession_geo_series_accession_get_0: %s\n" % e)
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

# **series_geo_series_get**
> ResponseModel series_geo_series_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Series

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
    api_instance = openapi_client.GEOApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Series
        api_response = api_instance.series_geo_series_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->series_geo_series_get: %s\n" % e)
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

# **series_geo_series_get_0**
> ResponseModel series_geo_series_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Series

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
    api_instance = openapi_client.GEOApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Series
        api_response = api_instance.series_geo_series_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GEOApi->series_geo_series_get_0: %s\n" % e)
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

