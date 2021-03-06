# \SRAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ByAccessionSraExperimentsAccessionGet**](SRAApi.md#ByAccessionSraExperimentsAccessionGet) | **Get** /sra/experiments/{accession} | Experiment By Accession
[**ByAccessionSraRunsAccessionGet**](SRAApi.md#ByAccessionSraRunsAccessionGet) | **Get** /sra/runs/{accession} | Run By Accession
[**ByAccessionSraSamplesAccessionGet**](SRAApi.md#ByAccessionSraSamplesAccessionGet) | **Get** /sra/samples/{accession} | Sample By Accession
[**ByAccessionSraStudiesAccessionGet**](SRAApi.md#ByAccessionSraStudiesAccessionGet) | **Get** /sra/studies/{accession} | Study By Accession
[**ForExperimentSraExperimentsAccessionRunsGet**](SRAApi.md#ForExperimentSraExperimentsAccessionRunsGet) | **Get** /sra/experiments/{accession}/runs | Runs For Experiment
[**ForSampleSraSamplesAccessionExperimentsGet**](SRAApi.md#ForSampleSraSamplesAccessionExperimentsGet) | **Get** /sra/samples/{accession}/experiments | Experiments For Sample
[**ForSampleSraSamplesAccessionRunsGet**](SRAApi.md#ForSampleSraSamplesAccessionRunsGet) | **Get** /sra/samples/{accession}/runs | Runs For Sample
[**ForStudySraStudiesAccessionExperimentsGet**](SRAApi.md#ForStudySraStudiesAccessionExperimentsGet) | **Get** /sra/studies/{accession}/experiments | Experiments For Study
[**ForStudySraStudiesAccessionRunsGet**](SRAApi.md#ForStudySraStudiesAccessionRunsGet) | **Get** /sra/studies/{accession}/runs | Runs For Study
[**ForStudySraStudiesAccessionSamplesGet**](SRAApi.md#ForStudySraStudiesAccessionSamplesGet) | **Get** /sra/studies/{accession}/samples | Samples For Study
[**SraExperimentsGet**](SRAApi.md#SraExperimentsGet) | **Get** /sra/experiments | Experiments
[**SraFieldsEntityGet**](SRAApi.md#SraFieldsEntityGet) | **Get** /sra/fields/{entity} | Mapping
[**SraRunsGet**](SRAApi.md#SraRunsGet) | **Get** /sra/runs | Runs
[**SraSamplesGet**](SRAApi.md#SraSamplesGet) | **Get** /sra/samples | Samples
[**SraStudiesGet**](SRAApi.md#SraStudiesGet) | **Get** /sra/studies | Studies



## ByAccessionSraExperimentsAccessionGet

> map[string]interface{} ByAccessionSraExperimentsAccessionGet(ctx, accession, optional)

Experiment By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ByAccessionSraExperimentsAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ByAccessionSraExperimentsAccessionGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ByAccessionSraRunsAccessionGet

> map[string]interface{} ByAccessionSraRunsAccessionGet(ctx, accession, optional)

Run By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ByAccessionSraRunsAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ByAccessionSraRunsAccessionGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ByAccessionSraSamplesAccessionGet

> map[string]interface{} ByAccessionSraSamplesAccessionGet(ctx, accession, optional)

Sample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ByAccessionSraSamplesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ByAccessionSraSamplesAccessionGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ByAccessionSraStudiesAccessionGet

> map[string]interface{} ByAccessionSraStudiesAccessionGet(ctx, accession, optional)

Study By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ByAccessionSraStudiesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ByAccessionSraStudiesAccessionGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForExperimentSraExperimentsAccessionRunsGet

> map[string]interface{} ForExperimentSraExperimentsAccessionRunsGet(ctx, accession, optional)

Runs For Experiment

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ForExperimentSraExperimentsAccessionRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ForExperimentSraExperimentsAccessionRunsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForSampleSraSamplesAccessionExperimentsGet

> map[string]interface{} ForSampleSraSamplesAccessionExperimentsGet(ctx, accession, optional)

Experiments For Sample

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ForSampleSraSamplesAccessionExperimentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ForSampleSraSamplesAccessionExperimentsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForSampleSraSamplesAccessionRunsGet

> map[string]interface{} ForSampleSraSamplesAccessionRunsGet(ctx, accession, optional)

Runs For Sample

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ForSampleSraSamplesAccessionRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ForSampleSraSamplesAccessionRunsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForStudySraStudiesAccessionExperimentsGet

> map[string]interface{} ForStudySraStudiesAccessionExperimentsGet(ctx, accession, optional)

Experiments For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ForStudySraStudiesAccessionExperimentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ForStudySraStudiesAccessionExperimentsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForStudySraStudiesAccessionRunsGet

> map[string]interface{} ForStudySraStudiesAccessionRunsGet(ctx, accession, optional)

Runs For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ForStudySraStudiesAccessionRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ForStudySraStudiesAccessionRunsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForStudySraStudiesAccessionSamplesGet

> map[string]interface{} ForStudySraStudiesAccessionSamplesGet(ctx, accession, optional)

Samples For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ForStudySraStudiesAccessionSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ForStudySraStudiesAccessionSamplesGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SraExperimentsGet

> ResponseModel SraExperimentsGet(ctx, optional)

Experiments

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SraExperimentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SraExperimentsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **optional.String**| The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) | 
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**| The cursor is used to scroll through results. For a query with more results than &#x60;size&#x60;, the result will include &#x60;cursor&#x60; in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the &#x60;cursor&#x60; will again be empty in the result json. | 
 **facetSize** | **optional.Int32**| The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. | [default to 10]
 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **facets** | [**optional.Interface of []string**](string.md)| A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. | [default to []]

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SraFieldsEntityGet

> map[string]interface{} SraFieldsEntityGet(ctx, entity)

Mapping

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**entity** | **string**|  | 

### Return type

[**map[string]interface{}**](map[string]interface{}.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SraRunsGet

> ResponseModel SraRunsGet(ctx, optional)

Runs

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SraRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SraRunsGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **optional.String**| The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) | 
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**| The cursor is used to scroll through results. For a query with more results than &#x60;size&#x60;, the result will include &#x60;cursor&#x60; in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the &#x60;cursor&#x60; will again be empty in the result json. | 
 **facetSize** | **optional.Int32**| The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. | [default to 10]
 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **facets** | [**optional.Interface of []string**](string.md)| A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. | [default to []]

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SraSamplesGet

> ResponseModel SraSamplesGet(ctx, optional)

Samples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SraSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SraSamplesGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **optional.String**| The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) | 
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**| The cursor is used to scroll through results. For a query with more results than &#x60;size&#x60;, the result will include &#x60;cursor&#x60; in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the &#x60;cursor&#x60; will again be empty in the result json. | 
 **facetSize** | **optional.Int32**| The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. | [default to 10]
 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **facets** | [**optional.Interface of []string**](string.md)| A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. | [default to []]

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SraStudiesGet

> ResponseModel SraStudiesGet(ctx, optional)

Studies

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SraStudiesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SraStudiesGetOpts struct


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **optional.String**| The query, using [lucene query syntax](https://lucene.apache.org/core/3_6_0/queryparsersyntax.html) | 
 **size** | **optional.Int32**|  | [default to 10]
 **cursor** | **optional.String**| The cursor is used to scroll through results. For a query with more results than &#x60;size&#x60;, the result will include &#x60;cursor&#x60; in the result json. Use that value here and re-issue the query. The next set or results will be returned. When no more results are available, the &#x60;cursor&#x60; will again be empty in the result json. | 
 **facetSize** | **optional.Int32**| The maximum number of records returned for each facet. This has no effect unless one or more facets are specified. | [default to 10]
 **includeFields** | [**optional.Interface of []string**](string.md)| Fields to include in results. The default is to all fields (*) | [default to []]
 **excludeFields** | [**optional.Interface of []string**](string.md)| Fields to exclude from results. The default is to not exclude any fields.  | [default to []]
 **facets** | [**optional.Interface of []string**](string.md)| A list of strings identifying fields for faceted search results. Simple term faceting is used here, meaning that fields that are short text and repeated across records will be binned and counted. | [default to []]

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

