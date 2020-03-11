# \SRAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExperimentByAccessionSraExperimentsAccessionGet**](SRAApi.md#ExperimentByAccessionSraExperimentsAccessionGet) | **Get** /sra/experiments/{accession} | Experiment By Accession
[**ExperimentByAccessionSraExperimentsAccessionGet_0**](SRAApi.md#ExperimentByAccessionSraExperimentsAccessionGet_0) | **Get** /sra/experiments/{accession} | Experiment By Accession
[**ExperimentsForSampleSraSamplesAccessionExperimentsGet**](SRAApi.md#ExperimentsForSampleSraSamplesAccessionExperimentsGet) | **Get** /sra/samples/{accession}/experiments | Experiments For Sample
[**ExperimentsForSampleSraSamplesAccessionExperimentsGet_0**](SRAApi.md#ExperimentsForSampleSraSamplesAccessionExperimentsGet_0) | **Get** /sra/samples/{accession}/experiments | Experiments For Sample
[**ExperimentsForStudySraStudiesAccessionExperimentsGet**](SRAApi.md#ExperimentsForStudySraStudiesAccessionExperimentsGet) | **Get** /sra/studies/{accession}/experiments | Experiments For Study
[**ExperimentsForStudySraStudiesAccessionExperimentsGet_0**](SRAApi.md#ExperimentsForStudySraStudiesAccessionExperimentsGet_0) | **Get** /sra/studies/{accession}/experiments | Experiments For Study
[**ExperimentsSraExperimentsGet**](SRAApi.md#ExperimentsSraExperimentsGet) | **Get** /sra/experiments | Experiments
[**ExperimentsSraExperimentsGet_0**](SRAApi.md#ExperimentsSraExperimentsGet_0) | **Get** /sra/experiments | Experiments
[**MappingSraFieldsEntityGet**](SRAApi.md#MappingSraFieldsEntityGet) | **Get** /sra/fields/{entity} | Mapping
[**RunByAccessionSraRunsAccessionGet**](SRAApi.md#RunByAccessionSraRunsAccessionGet) | **Get** /sra/runs/{accession} | Run By Accession
[**RunByAccessionSraRunsAccessionGet_0**](SRAApi.md#RunByAccessionSraRunsAccessionGet_0) | **Get** /sra/runs/{accession} | Run By Accession
[**RunsForExperimentSraExperimentsAccessionRunsGet**](SRAApi.md#RunsForExperimentSraExperimentsAccessionRunsGet) | **Get** /sra/experiments/{accession}/runs | Runs For Experiment
[**RunsForExperimentSraExperimentsAccessionRunsGet_0**](SRAApi.md#RunsForExperimentSraExperimentsAccessionRunsGet_0) | **Get** /sra/experiments/{accession}/runs | Runs For Experiment
[**RunsForSampleSraSamplesAccessionRunsGet**](SRAApi.md#RunsForSampleSraSamplesAccessionRunsGet) | **Get** /sra/samples/{accession}/runs | Runs For Sample
[**RunsForSampleSraSamplesAccessionRunsGet_0**](SRAApi.md#RunsForSampleSraSamplesAccessionRunsGet_0) | **Get** /sra/samples/{accession}/runs | Runs For Sample
[**RunsForStudySraStudiesAccessionRunsGet**](SRAApi.md#RunsForStudySraStudiesAccessionRunsGet) | **Get** /sra/studies/{accession}/runs | Runs For Study
[**RunsForStudySraStudiesAccessionRunsGet_0**](SRAApi.md#RunsForStudySraStudiesAccessionRunsGet_0) | **Get** /sra/studies/{accession}/runs | Runs For Study
[**RunsSraRunsGet**](SRAApi.md#RunsSraRunsGet) | **Get** /sra/runs | Runs
[**RunsSraRunsGet_0**](SRAApi.md#RunsSraRunsGet_0) | **Get** /sra/runs | Runs
[**SampleByAccessionSraSamplesAccessionGet**](SRAApi.md#SampleByAccessionSraSamplesAccessionGet) | **Get** /sra/samples/{accession} | Sample By Accession
[**SampleByAccessionSraSamplesAccessionGet_0**](SRAApi.md#SampleByAccessionSraSamplesAccessionGet_0) | **Get** /sra/samples/{accession} | Sample By Accession
[**SamplesForStudySraStudiesAccessionSamplesGet**](SRAApi.md#SamplesForStudySraStudiesAccessionSamplesGet) | **Get** /sra/studies/{accession}/samples | Samples For Study
[**SamplesForStudySraStudiesAccessionSamplesGet_0**](SRAApi.md#SamplesForStudySraStudiesAccessionSamplesGet_0) | **Get** /sra/studies/{accession}/samples | Samples For Study
[**SamplesSraSamplesGet**](SRAApi.md#SamplesSraSamplesGet) | **Get** /sra/samples | Samples
[**SamplesSraSamplesGet_0**](SRAApi.md#SamplesSraSamplesGet_0) | **Get** /sra/samples | Samples
[**StudiesSraStudiesGet**](SRAApi.md#StudiesSraStudiesGet) | **Get** /sra/studies | Studies
[**StudiesSraStudiesGet_0**](SRAApi.md#StudiesSraStudiesGet_0) | **Get** /sra/studies | Studies
[**StudyByAccessionSraStudiesAccessionGet**](SRAApi.md#StudyByAccessionSraStudiesAccessionGet) | **Get** /sra/studies/{accession} | Study By Accession
[**StudyByAccessionSraStudiesAccessionGet_0**](SRAApi.md#StudyByAccessionSraStudiesAccessionGet_0) | **Get** /sra/studies/{accession} | Study By Accession



## ExperimentByAccessionSraExperimentsAccessionGet

> map[string]interface{} ExperimentByAccessionSraExperimentsAccessionGet(ctx, accession, optional)

Experiment By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ExperimentByAccessionSraExperimentsAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentByAccessionSraExperimentsAccessionGetOpts struct


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


## ExperimentByAccessionSraExperimentsAccessionGet_0

> map[string]interface{} ExperimentByAccessionSraExperimentsAccessionGet_0(ctx, accession, optional)

Experiment By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ExperimentByAccessionSraExperimentsAccessionGet_1Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentByAccessionSraExperimentsAccessionGet_1Opts struct


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


## ExperimentsForSampleSraSamplesAccessionExperimentsGet

> map[string]interface{} ExperimentsForSampleSraSamplesAccessionExperimentsGet(ctx, accession, optional)

Experiments For Sample

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ExperimentsForSampleSraSamplesAccessionExperimentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentsForSampleSraSamplesAccessionExperimentsGetOpts struct


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


## ExperimentsForSampleSraSamplesAccessionExperimentsGet_0

> map[string]interface{} ExperimentsForSampleSraSamplesAccessionExperimentsGet_0(ctx, accession, optional)

Experiments For Sample

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ExperimentsForSampleSraSamplesAccessionExperimentsGet_2Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentsForSampleSraSamplesAccessionExperimentsGet_2Opts struct


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


## ExperimentsForStudySraStudiesAccessionExperimentsGet

> map[string]interface{} ExperimentsForStudySraStudiesAccessionExperimentsGet(ctx, accession, optional)

Experiments For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ExperimentsForStudySraStudiesAccessionExperimentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentsForStudySraStudiesAccessionExperimentsGetOpts struct


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


## ExperimentsForStudySraStudiesAccessionExperimentsGet_0

> map[string]interface{} ExperimentsForStudySraStudiesAccessionExperimentsGet_0(ctx, accession, optional)

Experiments For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ExperimentsForStudySraStudiesAccessionExperimentsGet_3Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentsForStudySraStudiesAccessionExperimentsGet_3Opts struct


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


## ExperimentsSraExperimentsGet

> ResponseModel ExperimentsSraExperimentsGet(ctx, optional)

Experiments

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ExperimentsSraExperimentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentsSraExperimentsGetOpts struct


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


## ExperimentsSraExperimentsGet_0

> ResponseModel ExperimentsSraExperimentsGet_0(ctx, optional)

Experiments

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ExperimentsSraExperimentsGet_4Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ExperimentsSraExperimentsGet_4Opts struct


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


## MappingSraFieldsEntityGet

> map[string]interface{} MappingSraFieldsEntityGet(ctx, entity)

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


## RunByAccessionSraRunsAccessionGet

> map[string]interface{} RunByAccessionSraRunsAccessionGet(ctx, accession, optional)

Run By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunByAccessionSraRunsAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunByAccessionSraRunsAccessionGetOpts struct


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


## RunByAccessionSraRunsAccessionGet_0

> map[string]interface{} RunByAccessionSraRunsAccessionGet_0(ctx, accession, optional)

Run By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunByAccessionSraRunsAccessionGet_5Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunByAccessionSraRunsAccessionGet_5Opts struct


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


## RunsForExperimentSraExperimentsAccessionRunsGet

> map[string]interface{} RunsForExperimentSraExperimentsAccessionRunsGet(ctx, accession, optional)

Runs For Experiment

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunsForExperimentSraExperimentsAccessionRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsForExperimentSraExperimentsAccessionRunsGetOpts struct


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


## RunsForExperimentSraExperimentsAccessionRunsGet_0

> map[string]interface{} RunsForExperimentSraExperimentsAccessionRunsGet_0(ctx, accession, optional)

Runs For Experiment

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunsForExperimentSraExperimentsAccessionRunsGet_6Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsForExperimentSraExperimentsAccessionRunsGet_6Opts struct


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


## RunsForSampleSraSamplesAccessionRunsGet

> map[string]interface{} RunsForSampleSraSamplesAccessionRunsGet(ctx, accession, optional)

Runs For Sample

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunsForSampleSraSamplesAccessionRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsForSampleSraSamplesAccessionRunsGetOpts struct


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


## RunsForSampleSraSamplesAccessionRunsGet_0

> map[string]interface{} RunsForSampleSraSamplesAccessionRunsGet_0(ctx, accession, optional)

Runs For Sample

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunsForSampleSraSamplesAccessionRunsGet_7Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsForSampleSraSamplesAccessionRunsGet_7Opts struct


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


## RunsForStudySraStudiesAccessionRunsGet

> map[string]interface{} RunsForStudySraStudiesAccessionRunsGet(ctx, accession, optional)

Runs For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunsForStudySraStudiesAccessionRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsForStudySraStudiesAccessionRunsGetOpts struct


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


## RunsForStudySraStudiesAccessionRunsGet_0

> map[string]interface{} RunsForStudySraStudiesAccessionRunsGet_0(ctx, accession, optional)

Runs For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***RunsForStudySraStudiesAccessionRunsGet_8Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsForStudySraStudiesAccessionRunsGet_8Opts struct


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


## RunsSraRunsGet

> ResponseModel RunsSraRunsGet(ctx, optional)

Runs

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***RunsSraRunsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsSraRunsGetOpts struct


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


## RunsSraRunsGet_0

> ResponseModel RunsSraRunsGet_0(ctx, optional)

Runs

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***RunsSraRunsGet_9Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a RunsSraRunsGet_9Opts struct


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


## SampleByAccessionSraSamplesAccessionGet

> map[string]interface{} SampleByAccessionSraSamplesAccessionGet(ctx, accession, optional)

Sample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SampleByAccessionSraSamplesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SampleByAccessionSraSamplesAccessionGetOpts struct


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


## SampleByAccessionSraSamplesAccessionGet_0

> map[string]interface{} SampleByAccessionSraSamplesAccessionGet_0(ctx, accession, optional)

Sample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SampleByAccessionSraSamplesAccessionGet_10Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SampleByAccessionSraSamplesAccessionGet_10Opts struct


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


## SamplesForStudySraStudiesAccessionSamplesGet

> map[string]interface{} SamplesForStudySraStudiesAccessionSamplesGet(ctx, accession, optional)

Samples For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SamplesForStudySraStudiesAccessionSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesForStudySraStudiesAccessionSamplesGetOpts struct


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


## SamplesForStudySraStudiesAccessionSamplesGet_0

> map[string]interface{} SamplesForStudySraStudiesAccessionSamplesGet_0(ctx, accession, optional)

Samples For Study

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SamplesForStudySraStudiesAccessionSamplesGet_11Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesForStudySraStudiesAccessionSamplesGet_11Opts struct


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


## SamplesSraSamplesGet

> ResponseModel SamplesSraSamplesGet(ctx, optional)

Samples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SamplesSraSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesSraSamplesGetOpts struct


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


## SamplesSraSamplesGet_0

> ResponseModel SamplesSraSamplesGet_0(ctx, optional)

Samples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SamplesSraSamplesGet_12Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesSraSamplesGet_12Opts struct


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


## StudiesSraStudiesGet

> ResponseModel StudiesSraStudiesGet(ctx, optional)

Studies

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***StudiesSraStudiesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a StudiesSraStudiesGetOpts struct


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


## StudiesSraStudiesGet_0

> ResponseModel StudiesSraStudiesGet_0(ctx, optional)

Studies

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***StudiesSraStudiesGet_13Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a StudiesSraStudiesGet_13Opts struct


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


## StudyByAccessionSraStudiesAccessionGet

> map[string]interface{} StudyByAccessionSraStudiesAccessionGet(ctx, accession, optional)

Study By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***StudyByAccessionSraStudiesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a StudyByAccessionSraStudiesAccessionGetOpts struct


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


## StudyByAccessionSraStudiesAccessionGet_0

> map[string]interface{} StudyByAccessionSraStudiesAccessionGet_0(ctx, accession, optional)

Study By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***StudyByAccessionSraStudiesAccessionGet_14Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a StudyByAccessionSraStudiesAccessionGet_14Opts struct


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

