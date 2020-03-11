# openapi_client.SRAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment_by_accession_sra_experiments_accession_get**](SRAApi.md#experiment_by_accession_sra_experiments_accession_get) | **GET** /sra/experiments/{accession} | Experiment By Accession
[**experiment_by_accession_sra_experiments_accession_get_0**](SRAApi.md#experiment_by_accession_sra_experiments_accession_get_0) | **GET** /sra/experiments/{accession} | Experiment By Accession
[**experiments_for_sample_sra_samples_accession_experiments_get**](SRAApi.md#experiments_for_sample_sra_samples_accession_experiments_get) | **GET** /sra/samples/{accession}/experiments | Experiments For Sample
[**experiments_for_sample_sra_samples_accession_experiments_get_0**](SRAApi.md#experiments_for_sample_sra_samples_accession_experiments_get_0) | **GET** /sra/samples/{accession}/experiments | Experiments For Sample
[**experiments_for_study_sra_studies_accession_experiments_get**](SRAApi.md#experiments_for_study_sra_studies_accession_experiments_get) | **GET** /sra/studies/{accession}/experiments | Experiments For Study
[**experiments_for_study_sra_studies_accession_experiments_get_0**](SRAApi.md#experiments_for_study_sra_studies_accession_experiments_get_0) | **GET** /sra/studies/{accession}/experiments | Experiments For Study
[**experiments_sra_experiments_get**](SRAApi.md#experiments_sra_experiments_get) | **GET** /sra/experiments | Experiments
[**experiments_sra_experiments_get_0**](SRAApi.md#experiments_sra_experiments_get_0) | **GET** /sra/experiments | Experiments
[**mapping_sra_fields_entity_get**](SRAApi.md#mapping_sra_fields_entity_get) | **GET** /sra/fields/{entity} | Mapping
[**run_by_accession_sra_runs_accession_get**](SRAApi.md#run_by_accession_sra_runs_accession_get) | **GET** /sra/runs/{accession} | Run By Accession
[**run_by_accession_sra_runs_accession_get_0**](SRAApi.md#run_by_accession_sra_runs_accession_get_0) | **GET** /sra/runs/{accession} | Run By Accession
[**runs_for_experiment_sra_experiments_accession_runs_get**](SRAApi.md#runs_for_experiment_sra_experiments_accession_runs_get) | **GET** /sra/experiments/{accession}/runs | Runs For Experiment
[**runs_for_experiment_sra_experiments_accession_runs_get_0**](SRAApi.md#runs_for_experiment_sra_experiments_accession_runs_get_0) | **GET** /sra/experiments/{accession}/runs | Runs For Experiment
[**runs_for_sample_sra_samples_accession_runs_get**](SRAApi.md#runs_for_sample_sra_samples_accession_runs_get) | **GET** /sra/samples/{accession}/runs | Runs For Sample
[**runs_for_sample_sra_samples_accession_runs_get_0**](SRAApi.md#runs_for_sample_sra_samples_accession_runs_get_0) | **GET** /sra/samples/{accession}/runs | Runs For Sample
[**runs_for_study_sra_studies_accession_runs_get**](SRAApi.md#runs_for_study_sra_studies_accession_runs_get) | **GET** /sra/studies/{accession}/runs | Runs For Study
[**runs_for_study_sra_studies_accession_runs_get_0**](SRAApi.md#runs_for_study_sra_studies_accession_runs_get_0) | **GET** /sra/studies/{accession}/runs | Runs For Study
[**runs_sra_runs_get**](SRAApi.md#runs_sra_runs_get) | **GET** /sra/runs | Runs
[**runs_sra_runs_get_0**](SRAApi.md#runs_sra_runs_get_0) | **GET** /sra/runs | Runs
[**sample_by_accession_sra_samples_accession_get**](SRAApi.md#sample_by_accession_sra_samples_accession_get) | **GET** /sra/samples/{accession} | Sample By Accession
[**sample_by_accession_sra_samples_accession_get_0**](SRAApi.md#sample_by_accession_sra_samples_accession_get_0) | **GET** /sra/samples/{accession} | Sample By Accession
[**samples_for_study_sra_studies_accession_samples_get**](SRAApi.md#samples_for_study_sra_studies_accession_samples_get) | **GET** /sra/studies/{accession}/samples | Samples For Study
[**samples_for_study_sra_studies_accession_samples_get_0**](SRAApi.md#samples_for_study_sra_studies_accession_samples_get_0) | **GET** /sra/studies/{accession}/samples | Samples For Study
[**samples_sra_samples_get**](SRAApi.md#samples_sra_samples_get) | **GET** /sra/samples | Samples
[**samples_sra_samples_get_0**](SRAApi.md#samples_sra_samples_get_0) | **GET** /sra/samples | Samples
[**studies_sra_studies_get**](SRAApi.md#studies_sra_studies_get) | **GET** /sra/studies | Studies
[**studies_sra_studies_get_0**](SRAApi.md#studies_sra_studies_get_0) | **GET** /sra/studies | Studies
[**study_by_accession_sra_studies_accession_get**](SRAApi.md#study_by_accession_sra_studies_accession_get) | **GET** /sra/studies/{accession} | Study By Accession
[**study_by_accession_sra_studies_accession_get_0**](SRAApi.md#study_by_accession_sra_studies_accession_get_0) | **GET** /sra/studies/{accession} | Study By Accession


# **experiment_by_accession_sra_experiments_accession_get**
> object experiment_by_accession_sra_experiments_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Experiment By Accession

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Experiment By Accession
        api_response = api_instance.experiment_by_accession_sra_experiments_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiment_by_accession_sra_experiments_accession_get: %s\n" % e)
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

# **experiment_by_accession_sra_experiments_accession_get_0**
> object experiment_by_accession_sra_experiments_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Experiment By Accession

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Experiment By Accession
        api_response = api_instance.experiment_by_accession_sra_experiments_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiment_by_accession_sra_experiments_accession_get_0: %s\n" % e)
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

# **experiments_for_sample_sra_samples_accession_experiments_get**
> object experiments_for_sample_sra_samples_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Experiments For Sample

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Experiments For Sample
        api_response = api_instance.experiments_for_sample_sra_samples_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiments_for_sample_sra_samples_accession_experiments_get: %s\n" % e)
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

# **experiments_for_sample_sra_samples_accession_experiments_get_0**
> object experiments_for_sample_sra_samples_accession_experiments_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Experiments For Sample

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Experiments For Sample
        api_response = api_instance.experiments_for_sample_sra_samples_accession_experiments_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiments_for_sample_sra_samples_accession_experiments_get_0: %s\n" % e)
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

# **experiments_for_study_sra_studies_accession_experiments_get**
> object experiments_for_study_sra_studies_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Experiments For Study

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Experiments For Study
        api_response = api_instance.experiments_for_study_sra_studies_accession_experiments_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiments_for_study_sra_studies_accession_experiments_get: %s\n" % e)
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

# **experiments_for_study_sra_studies_accession_experiments_get_0**
> object experiments_for_study_sra_studies_accession_experiments_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Experiments For Study

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Experiments For Study
        api_response = api_instance.experiments_for_study_sra_studies_accession_experiments_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiments_for_study_sra_studies_accession_experiments_get_0: %s\n" % e)
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

# **experiments_sra_experiments_get**
> ResponseModel experiments_sra_experiments_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Experiments

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Experiments
        api_response = api_instance.experiments_sra_experiments_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiments_sra_experiments_get: %s\n" % e)
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

# **experiments_sra_experiments_get_0**
> ResponseModel experiments_sra_experiments_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Experiments

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Experiments
        api_response = api_instance.experiments_sra_experiments_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->experiments_sra_experiments_get_0: %s\n" % e)
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

# **mapping_sra_fields_entity_get**
> object mapping_sra_fields_entity_get(entity)

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
    api_instance = openapi_client.SRAApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Mapping
        api_response = api_instance.mapping_sra_fields_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->mapping_sra_fields_entity_get: %s\n" % e)
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

# **run_by_accession_sra_runs_accession_get**
> object run_by_accession_sra_runs_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Run By Accession

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Run By Accession
        api_response = api_instance.run_by_accession_sra_runs_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->run_by_accession_sra_runs_accession_get: %s\n" % e)
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

# **run_by_accession_sra_runs_accession_get_0**
> object run_by_accession_sra_runs_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Run By Accession

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Run By Accession
        api_response = api_instance.run_by_accession_sra_runs_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->run_by_accession_sra_runs_accession_get_0: %s\n" % e)
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

# **runs_for_experiment_sra_experiments_accession_runs_get**
> object runs_for_experiment_sra_experiments_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Experiment

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Experiment
        api_response = api_instance.runs_for_experiment_sra_experiments_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_for_experiment_sra_experiments_accession_runs_get: %s\n" % e)
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

# **runs_for_experiment_sra_experiments_accession_runs_get_0**
> object runs_for_experiment_sra_experiments_accession_runs_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Experiment

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Experiment
        api_response = api_instance.runs_for_experiment_sra_experiments_accession_runs_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_for_experiment_sra_experiments_accession_runs_get_0: %s\n" % e)
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

# **runs_for_sample_sra_samples_accession_runs_get**
> object runs_for_sample_sra_samples_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Sample

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Sample
        api_response = api_instance.runs_for_sample_sra_samples_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_for_sample_sra_samples_accession_runs_get: %s\n" % e)
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

# **runs_for_sample_sra_samples_accession_runs_get_0**
> object runs_for_sample_sra_samples_accession_runs_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Sample

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Sample
        api_response = api_instance.runs_for_sample_sra_samples_accession_runs_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_for_sample_sra_samples_accession_runs_get_0: %s\n" % e)
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

# **runs_for_study_sra_studies_accession_runs_get**
> object runs_for_study_sra_studies_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Study

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Study
        api_response = api_instance.runs_for_study_sra_studies_accession_runs_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_for_study_sra_studies_accession_runs_get: %s\n" % e)
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

# **runs_for_study_sra_studies_accession_runs_get_0**
> object runs_for_study_sra_studies_accession_runs_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Runs For Study

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Runs For Study
        api_response = api_instance.runs_for_study_sra_studies_accession_runs_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_for_study_sra_studies_accession_runs_get_0: %s\n" % e)
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

# **runs_sra_runs_get**
> ResponseModel runs_sra_runs_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Runs

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Runs
        api_response = api_instance.runs_sra_runs_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_sra_runs_get: %s\n" % e)
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

# **runs_sra_runs_get_0**
> ResponseModel runs_sra_runs_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Runs

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Runs
        api_response = api_instance.runs_sra_runs_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->runs_sra_runs_get_0: %s\n" % e)
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

# **sample_by_accession_sra_samples_accession_get**
> object sample_by_accession_sra_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Sample By Accession
        api_response = api_instance.sample_by_accession_sra_samples_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sample_by_accession_sra_samples_accession_get: %s\n" % e)
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

# **sample_by_accession_sra_samples_accession_get_0**
> object sample_by_accession_sra_samples_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Sample By Accession
        api_response = api_instance.sample_by_accession_sra_samples_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->sample_by_accession_sra_samples_accession_get_0: %s\n" % e)
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

# **samples_for_study_sra_studies_accession_samples_get**
> object samples_for_study_sra_studies_accession_samples_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Samples For Study

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Samples For Study
        api_response = api_instance.samples_for_study_sra_studies_accession_samples_get(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->samples_for_study_sra_studies_accession_samples_get: %s\n" % e)
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

# **samples_for_study_sra_studies_accession_samples_get_0**
> object samples_for_study_sra_studies_accession_samples_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)

Samples For Study

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str |  (optional)

    try:
        # Samples For Study
        api_response = api_instance.samples_for_study_sra_studies_accession_samples_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields, size=size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->samples_for_study_sra_studies_accession_samples_get_0: %s\n" % e)
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

# **samples_sra_samples_get**
> ResponseModel samples_sra_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Samples
        api_response = api_instance.samples_sra_samples_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->samples_sra_samples_get: %s\n" % e)
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

# **samples_sra_samples_get_0**
> ResponseModel samples_sra_samples_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Samples
        api_response = api_instance.samples_sra_samples_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->samples_sra_samples_get_0: %s\n" % e)
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

# **studies_sra_studies_get**
> ResponseModel studies_sra_studies_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Studies

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Studies
        api_response = api_instance.studies_sra_studies_get(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->studies_sra_studies_get: %s\n" % e)
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

# **studies_sra_studies_get_0**
> ResponseModel studies_sra_studies_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)

Studies

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
    api_instance = openapi_client.SRAApi(api_client)
    q = 'cancer' # str | The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) (optional)
size = 10 # int |  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor is used to scroll through results. For a query with more results than `size`, the result will include `cursor` in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the `cursor` will again be empty in the result json. (optional)
facet_size = 10 # int | The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. (optional) (default to 10)
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])
facets = [] # list[str] | A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. (optional) (default to [])

    try:
        # Studies
        api_response = api_instance.studies_sra_studies_get_0(q=q, size=size, cursor=cursor, facet_size=facet_size, include_fields=include_fields, exclude_fields=exclude_fields, facets=facets)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->studies_sra_studies_get_0: %s\n" % e)
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

# **study_by_accession_sra_studies_accession_get**
> object study_by_accession_sra_studies_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Study By Accession

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Study By Accession
        api_response = api_instance.study_by_accession_sra_studies_accession_get(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->study_by_accession_sra_studies_accession_get: %s\n" % e)
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

# **study_by_accession_sra_studies_accession_get_0**
> object study_by_accession_sra_studies_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)

Study By Accession

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
    api_instance = openapi_client.SRAApi(api_client)
    accession = 'accession_example' # str | An accession for lookup
include_fields = [] # list[str] | Fields to include in results. The default is to all fields (*) (optional) (default to [])
exclude_fields = [] # list[str] | Fields to exclude from results. The default is to not exclude any fields.  (optional) (default to [])

    try:
        # Study By Accession
        api_response = api_instance.study_by_accession_sra_studies_accession_get_0(accession, include_fields=include_fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SRAApi->study_by_accession_sra_studies_accession_get_0: %s\n" % e)
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

