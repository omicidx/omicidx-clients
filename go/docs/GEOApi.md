# \GEOApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**MappingGeoFieldsEntityGet**](GEOApi.md#MappingGeoFieldsEntityGet) | **Get** /geo/fields/{entity} | Mapping
[**PlatformByAccessionGeoPlatformAccessionGet**](GEOApi.md#PlatformByAccessionGeoPlatformAccessionGet) | **Get** /geo/platform/{accession} | Platform By Accession
[**PlatformByAccessionGeoPlatformAccessionGet_0**](GEOApi.md#PlatformByAccessionGeoPlatformAccessionGet_0) | **Get** /geo/platform/{accession} | Platform By Accession
[**PlatformGeoPlatformsGet**](GEOApi.md#PlatformGeoPlatformsGet) | **Get** /geo/platforms | Platform
[**PlatformGeoPlatformsGet_0**](GEOApi.md#PlatformGeoPlatformsGet_0) | **Get** /geo/platforms | Platform
[**SampleByAccessionGeoSamplesAccessionGet**](GEOApi.md#SampleByAccessionGeoSamplesAccessionGet) | **Get** /geo/samples/{accession} | Sample By Accession
[**SampleByAccessionGeoSamplesAccessionGet_0**](GEOApi.md#SampleByAccessionGeoSamplesAccessionGet_0) | **Get** /geo/samples/{accession} | Sample By Accession
[**SamplesForPlatformGeoPlatformsAccessionSamplesGet**](GEOApi.md#SamplesForPlatformGeoPlatformsAccessionSamplesGet) | **Get** /geo/platforms/{accession}/samples | Samples For Platform
[**SamplesForPlatformGeoPlatformsAccessionSamplesGet_0**](GEOApi.md#SamplesForPlatformGeoPlatformsAccessionSamplesGet_0) | **Get** /geo/platforms/{accession}/samples | Samples For Platform
[**SamplesGeoSamplesGet**](GEOApi.md#SamplesGeoSamplesGet) | **Get** /geo/samples | Samples
[**SamplesGeoSamplesGet_0**](GEOApi.md#SamplesGeoSamplesGet_0) | **Get** /geo/samples | Samples
[**SeriesByAccessionGeoSeriesAccessionGet**](GEOApi.md#SeriesByAccessionGeoSeriesAccessionGet) | **Get** /geo/series/{accession} | Series By Accession
[**SeriesByAccessionGeoSeriesAccessionGet_0**](GEOApi.md#SeriesByAccessionGeoSeriesAccessionGet_0) | **Get** /geo/series/{accession} | Series By Accession
[**SeriesGeoSeriesGet**](GEOApi.md#SeriesGeoSeriesGet) | **Get** /geo/series | Series
[**SeriesGeoSeriesGet_0**](GEOApi.md#SeriesGeoSeriesGet_0) | **Get** /geo/series | Series



## MappingGeoFieldsEntityGet

> map[string]interface{} MappingGeoFieldsEntityGet(ctx, entity)

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


## PlatformByAccessionGeoPlatformAccessionGet

> map[string]interface{} PlatformByAccessionGeoPlatformAccessionGet(ctx, accession, optional)

Platform By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***PlatformByAccessionGeoPlatformAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a PlatformByAccessionGeoPlatformAccessionGetOpts struct


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


## PlatformByAccessionGeoPlatformAccessionGet_0

> map[string]interface{} PlatformByAccessionGeoPlatformAccessionGet_0(ctx, accession, optional)

Platform By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***PlatformByAccessionGeoPlatformAccessionGet_1Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a PlatformByAccessionGeoPlatformAccessionGet_1Opts struct


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


## PlatformGeoPlatformsGet

> ResponseModel PlatformGeoPlatformsGet(ctx, optional)

Platform

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***PlatformGeoPlatformsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a PlatformGeoPlatformsGetOpts struct


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


## PlatformGeoPlatformsGet_0

> ResponseModel PlatformGeoPlatformsGet_0(ctx, optional)

Platform

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***PlatformGeoPlatformsGet_2Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a PlatformGeoPlatformsGet_2Opts struct


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


## SampleByAccessionGeoSamplesAccessionGet

> map[string]interface{} SampleByAccessionGeoSamplesAccessionGet(ctx, accession, optional)

Sample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SampleByAccessionGeoSamplesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SampleByAccessionGeoSamplesAccessionGetOpts struct


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


## SampleByAccessionGeoSamplesAccessionGet_0

> map[string]interface{} SampleByAccessionGeoSamplesAccessionGet_0(ctx, accession, optional)

Sample By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SampleByAccessionGeoSamplesAccessionGet_3Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SampleByAccessionGeoSamplesAccessionGet_3Opts struct


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


## SamplesForPlatformGeoPlatformsAccessionSamplesGet

> map[string]interface{} SamplesForPlatformGeoPlatformsAccessionSamplesGet(ctx, accession, optional)

Samples For Platform

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SamplesForPlatformGeoPlatformsAccessionSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesForPlatformGeoPlatformsAccessionSamplesGetOpts struct


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


## SamplesForPlatformGeoPlatformsAccessionSamplesGet_0

> map[string]interface{} SamplesForPlatformGeoPlatformsAccessionSamplesGet_0(ctx, accession, optional)

Samples For Platform

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SamplesForPlatformGeoPlatformsAccessionSamplesGet_4Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesForPlatformGeoPlatformsAccessionSamplesGet_4Opts struct


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


## SamplesGeoSamplesGet

> ResponseModel SamplesGeoSamplesGet(ctx, optional)

Samples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SamplesGeoSamplesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesGeoSamplesGetOpts struct


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


## SamplesGeoSamplesGet_0

> ResponseModel SamplesGeoSamplesGet_0(ctx, optional)

Samples

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SamplesGeoSamplesGet_5Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SamplesGeoSamplesGet_5Opts struct


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


## SeriesByAccessionGeoSeriesAccessionGet

> map[string]interface{} SeriesByAccessionGeoSeriesAccessionGet(ctx, accession, optional)

Series By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SeriesByAccessionGeoSeriesAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SeriesByAccessionGeoSeriesAccessionGetOpts struct


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


## SeriesByAccessionGeoSeriesAccessionGet_0

> map[string]interface{} SeriesByAccessionGeoSeriesAccessionGet_0(ctx, accession, optional)

Series By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***SeriesByAccessionGeoSeriesAccessionGet_6Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SeriesByAccessionGeoSeriesAccessionGet_6Opts struct


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


## SeriesGeoSeriesGet

> ResponseModel SeriesGeoSeriesGet(ctx, optional)

Series

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SeriesGeoSeriesGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SeriesGeoSeriesGetOpts struct


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


## SeriesGeoSeriesGet_0

> ResponseModel SeriesGeoSeriesGet_0(ctx, optional)

Series

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SeriesGeoSeriesGet_7Opts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a SeriesGeoSeriesGet_7Opts struct


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

