# \BiosampleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BiosampleByAccessionBiosampleSamplesAccessionGet**](BiosampleApi.md#BiosampleByAccessionBiosampleSamplesAccessionGet) | **Get** /biosample/samples/{accession} | Biosample By Accession
[**BiosampleByAccessionBiosampleSamplesAccessionGet_0**](BiosampleApi.md#BiosampleByAccessionBiosampleSamplesAccessionGet_0) | **Get** /biosample/samples/{accession} | Biosample By Accession
[**BiosamplesBiosampleSamplesGet**](BiosampleApi.md#BiosamplesBiosampleSamplesGet) | **Get** /biosample/samples | Biosamples
[**BiosamplesBiosampleSamplesGet_0**](BiosampleApi.md#BiosamplesBiosampleSamplesGet_0) | **Get** /biosample/samples | Biosamples
[**MappingBiosampleFieldsEntityGet**](BiosampleApi.md#MappingBiosampleFieldsEntityGet) | **Get** /biosample/fields/{entity} | Mapping



## BiosampleByAccessionBiosampleSamplesAccessionGet

> map[string]interface{} BiosampleByAccessionBiosampleSamplesAccessionGet(ctx, accession, optional)

Biosample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***BiosampleByAccessionBiosampleSamplesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a BiosampleByAccessionBiosampleSamplesAccessionGetOpts struct


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


## BiosampleByAccessionBiosampleSamplesAccessionGet_0

> map[string]interface{} BiosampleByAccessionBiosampleSamplesAccessionGet_0(ctx, accession, optional)

Biosample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***BiosampleByAccessionBiosampleSamplesAccessionGet_1Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a BiosampleByAccessionBiosampleSamplesAccessionGet_1Opts struct


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


## BiosamplesBiosampleSamplesGet

> ResponseModel BiosamplesBiosampleSamplesGet(ctx, optional)

Biosamples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***BiosamplesBiosampleSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a BiosamplesBiosampleSamplesGetOpts struct


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


## BiosamplesBiosampleSamplesGet_0

> ResponseModel BiosamplesBiosampleSamplesGet_0(ctx, optional)

Biosamples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***BiosamplesBiosampleSamplesGet_2Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a BiosamplesBiosampleSamplesGet_2Opts struct


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


## MappingBiosampleFieldsEntityGet

> map[string]interface{} MappingBiosampleFieldsEntityGet(ctx, entity)

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

