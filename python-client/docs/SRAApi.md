# omicidx_client.SRAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**by_accession_sra_experiments_accession_get**](SRAApi.md#by_accession_sra_experiments_accession_get) | **GET** /sra/experiments/{accession} | Experiment By Accession
[**by_accession_sra_runs_accession_get**](SRAApi.md#by_accession_sra_runs_accession_get) | **GET** /sra/runs/{accession} | Run By Accession
[**by_accession_sra_samples_accession_get**](SRAApi.md#by_accession_sra_samples_accession_get) | **GET** /sra/samples/{accession} | Sample By Accession
[**by_accession_sra_studies_accession_get**](SRAApi.md#by_accession_sra_studies_accession_get) | **GET** /sra/studies/{accession} | Study By Accession
[**for_experiment_sra_experiments_accession_runs_get**](SRAApi.md#for_experiment_sra_experiments_accession_runs_get) | **GET** /sra/experiments/{accession}/runs | Runs For Experiment
[**for_sample_sra_samples_accession_experiments_get**](SRAApi.md#for_sample_sra_samples_accession_experiments_get) | **GET** /sra/samples/{accession}/experiments | Experiments For Sample
[**for_sample_sra_samples_accession_runs_get**](SRAApi.md#for_sample_sra_samples_accession_runs_get) | **GET** /sra/samples/{accession}/runs | Runs For Sample
[**for_study_sra_studies_accession_experiments_get**](SRAApi.md#for_study_sra_studies_accession_experiments_get) | **GET** /sra/studies/{accession}/experiments | Experiments For Study
[**for_study_sra_studies_accession_runs_get**](SRAApi.md#for_study_sra_studies_accession_runs_get) | **GET** /sra/studies/{accession}/runs | Runs For Study
[**for_study_sra_studies_accession_samples_get**](SRAApi.md#for_study_sra_studies_accession_samples_get) | **GET** /sra/studies/{accession}/samples | Samples For Study
[**sra_experiments_get**](SRAApi.md#sra_experiments_get) | **GET** /sra/experiments | Experiments
[**sra_fields_entity_get**](SRAApi.md#sra_fields_entity_get) | **GET** /sra/fields/{entity} | Mapping
[**sra_runs_get**](SRAApi.md#sra_runs_get) | **GET** /sra/runs | Runs
[**sra_samples_get**](SRAApi.md#sra_samples_get) | **GET** /sra/samples | Samples
[**sra_studies_get**](SRAApi.md#sra_studies_get) | **GET** /sra/studies | Studies


# **by_accession_sra_experiments_accession_get**
> object by_accession_sra_experiments_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Experiment By Accession

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Experiment By Accession
        api_response = api_instance.by_accession_sra_experiments_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->by_accession_sra_experiments_accession_get: %s\n" % e)
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

# **by_accession_sra_runs_accession_get**
> object by_accession_sra_runs_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Run By Accession

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Run By Accession
        api_response = api_instance.by_accession_sra_runs_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->by_accession_sra_runs_accession_get: %s\n" % e)
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

# **by_accession_sra_samples_accession_get**
> object by_accession_sra_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Sample By Accession

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Sample By Accession
        api_response = api_instance.by_accession_sra_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->by_accession_sra_samples_accession_get: %s\n" % e)
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

# **by_accession_sra_studies_accession_get**
> object by_accession_sra_studies_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Study By Accession

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Study By Accession
        api_response = api_instance.by_accession_sra_studies_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->by_accession_sra_studies_accession_get: %s\n" % e)
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

# **for_experiment_sra_experiments_accession_runs_get**
> object for_experiment_sra_experiments_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Experiment

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Experiment
        api_response = api_instance.for_experiment_sra_experiments_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->for_experiment_sra_experiments_accession_runs_get: %s\n" % e)
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

# **for_sample_sra_samples_accession_experiments_get**
> object for_sample_sra_samples_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Experiments For Sample

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Experiments For Sample
        api_response = api_instance.for_sample_sra_samples_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->for_sample_sra_samples_accession_experiments_get: %s\n" % e)
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

# **for_sample_sra_samples_accession_runs_get**
> object for_sample_sra_samples_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Sample

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Sample
        api_response = api_instance.for_sample_sra_samples_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->for_sample_sra_samples_accession_runs_get: %s\n" % e)
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

# **for_study_sra_studies_accession_experiments_get**
> object for_study_sra_studies_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Experiments For Study

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Experiments For Study
        api_response = api_instance.for_study_sra_studies_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->for_study_sra_studies_accession_experiments_get: %s\n" % e)
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

# **for_study_sra_studies_accession_runs_get**
> object for_study_sra_studies_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Study

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Study
        api_response = api_instance.for_study_sra_studies_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->for_study_sra_studies_accession_runs_get: %s\n" % e)
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

# **for_study_sra_studies_accession_samples_get**
> object for_study_sra_studies_accession_samples_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Samples For Study

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
    api_instance = omicidx_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Samples For Study
        api_response = api_instance.for_study_sra_studies_accession_samples_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->for_study_sra_studies_accession_samples_get: %s\n" % e)
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

# **sra_experiments_get**
> ResponseModel sra_experiments_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Experiments

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
    api_instance = omicidx_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Experiments
        api_response = api_instance.sra_experiments_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sra_experiments_get: %s\n" % e)
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

# **sra_fields_entity_get**
> object sra_fields_entity_get(entity)

Mapping

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
    api_instance = omicidx_client.SRAApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Mapping
        api_response = api_instance.sra_fields_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sra_fields_entity_get: %s\n" % e)
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

# **sra_runs_get**
> ResponseModel sra_runs_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Runs

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
    api_instance = omicidx_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Runs
        api_response = api_instance.sra_runs_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sra_runs_get: %s\n" % e)
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

# **sra_samples_get**
> ResponseModel sra_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Samples

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
    api_instance = omicidx_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Samples
        api_response = api_instance.sra_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sra_samples_get: %s\n" % e)
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

# **sra_studies_get**
> ResponseModel sra_studies_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Studies

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
    api_instance = omicidx_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Studies
        api_response = api_instance.sra_studies_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sra_studies_get: %s\n" % e)
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

