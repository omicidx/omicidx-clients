# \GEOPlatformsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ByAccessionGeoPlatformAccessionGet**](GEOPlatformsApi.md#ByAccessionGeoPlatformAccessionGet) | **Get** /geo/platform/{accession} | Platform By Accession



## ByAccessionGeoPlatformAccessionGet

> map[string]interface{} ByAccessionGeoPlatformAccessionGet(ctx, accession, optional)

Platform By Accession

### Required Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accession** | **string**| An accession for lookup | 
 **optional** | ***ByAccessionGeoPlatformAccessionGetOpts** | optional parameters | nil if no parameters

### Optional Parameters

Optional parameters are passed through a pointer to a ByAccessionGeoPlatformAccessionGetOpts struct


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

