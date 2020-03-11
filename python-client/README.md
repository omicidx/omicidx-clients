# omicidx-client




The OmicIDX API documentation is available in three forms:

- [RapiDoc](/docs)
- [OpenAPI/Swagger Interactive](/swatterdoc)
- [ReDoc (more readable in some ways)](/redoc)



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.99
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import omicidx_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import omicidx_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import omicidx_client
from omicidx_client.rest import ApiException
from pprint import pprint


# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with omicidx_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omicidx_client.BiosampleApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Mapping
        api_response = api_instance.biosample_fields_entity_get(entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiosampleApi->biosample_fields_entity_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BiosampleApi* | [**biosample_fields_entity_get**](docs/BiosampleApi.md#biosample_fields_entity_get) | **GET** /biosample/fields/{entity} | Mapping
*BiosampleApi* | [**biosample_samples_get**](docs/BiosampleApi.md#biosample_samples_get) | **GET** /biosample/samples | Biosamples
*BiosampleApi* | [**biosample_samples_get_0**](docs/BiosampleApi.md#biosample_samples_get_0) | **GET** /biosample/samples | Biosamples
*BiosampleApi* | [**by_accession_biosample_samples_accession_get**](docs/BiosampleApi.md#by_accession_biosample_samples_accession_get) | **GET** /biosample/samples/{accession} | Biosample By Accession
*BiosampleApi* | [**by_accession_biosample_samples_accession_get_0**](docs/BiosampleApi.md#by_accession_biosample_samples_accession_get_0) | **GET** /biosample/samples/{accession} | Biosample By Accession
*GEOApi* | [**by_accession_geo_platform_accession_get**](docs/GEOApi.md#by_accession_geo_platform_accession_get) | **GET** /geo/platform/{accession} | Platform By Accession
*GEOApi* | [**by_accession_geo_platform_accession_get_0**](docs/GEOApi.md#by_accession_geo_platform_accession_get_0) | **GET** /geo/platform/{accession} | Platform By Accession
*GEOApi* | [**by_accession_geo_samples_accession_get**](docs/GEOApi.md#by_accession_geo_samples_accession_get) | **GET** /geo/samples/{accession} | Sample By Accession
*GEOApi* | [**by_accession_geo_samples_accession_get_0**](docs/GEOApi.md#by_accession_geo_samples_accession_get_0) | **GET** /geo/samples/{accession} | Sample By Accession
*GEOApi* | [**by_accession_geo_series_accession_get**](docs/GEOApi.md#by_accession_geo_series_accession_get) | **GET** /geo/series/{accession} | Series By Accession
*GEOApi* | [**by_accession_geo_series_accession_get_0**](docs/GEOApi.md#by_accession_geo_series_accession_get_0) | **GET** /geo/series/{accession} | Series By Accession
*GEOApi* | [**for_platform_geo_platforms_accession_samples_get**](docs/GEOApi.md#for_platform_geo_platforms_accession_samples_get) | **GET** /geo/platforms/{accession}/samples | Samples For Platform
*GEOApi* | [**for_platform_geo_platforms_accession_samples_get_0**](docs/GEOApi.md#for_platform_geo_platforms_accession_samples_get_0) | **GET** /geo/platforms/{accession}/samples | Samples For Platform
*GEOApi* | [**geo_fields_entity_get**](docs/GEOApi.md#geo_fields_entity_get) | **GET** /geo/fields/{entity} | Mapping
*GEOApi* | [**geo_platforms_get**](docs/GEOApi.md#geo_platforms_get) | **GET** /geo/platforms | Platform
*GEOApi* | [**geo_platforms_get_0**](docs/GEOApi.md#geo_platforms_get_0) | **GET** /geo/platforms | Platform
*GEOApi* | [**geo_samples_get**](docs/GEOApi.md#geo_samples_get) | **GET** /geo/samples | Samples
*GEOApi* | [**geo_samples_get_0**](docs/GEOApi.md#geo_samples_get_0) | **GET** /geo/samples | Samples
*GEOApi* | [**geo_series_get**](docs/GEOApi.md#geo_series_get) | **GET** /geo/series | Series
*GEOApi* | [**geo_series_get_0**](docs/GEOApi.md#geo_series_get_0) | **GET** /geo/series | Series
*SRAApi* | [**by_accession_sra_experiments_accession_get**](docs/SRAApi.md#by_accession_sra_experiments_accession_get) | **GET** /sra/experiments/{accession} | Experiment By Accession
*SRAApi* | [**by_accession_sra_experiments_accession_get_0**](docs/SRAApi.md#by_accession_sra_experiments_accession_get_0) | **GET** /sra/experiments/{accession} | Experiment By Accession
*SRAApi* | [**by_accession_sra_runs_accession_get**](docs/SRAApi.md#by_accession_sra_runs_accession_get) | **GET** /sra/runs/{accession} | Run By Accession
*SRAApi* | [**by_accession_sra_runs_accession_get_0**](docs/SRAApi.md#by_accession_sra_runs_accession_get_0) | **GET** /sra/runs/{accession} | Run By Accession
*SRAApi* | [**by_accession_sra_samples_accession_get**](docs/SRAApi.md#by_accession_sra_samples_accession_get) | **GET** /sra/samples/{accession} | Sample By Accession
*SRAApi* | [**by_accession_sra_samples_accession_get_0**](docs/SRAApi.md#by_accession_sra_samples_accession_get_0) | **GET** /sra/samples/{accession} | Sample By Accession
*SRAApi* | [**by_accession_sra_studies_accession_get**](docs/SRAApi.md#by_accession_sra_studies_accession_get) | **GET** /sra/studies/{accession} | Study By Accession
*SRAApi* | [**by_accession_sra_studies_accession_get_0**](docs/SRAApi.md#by_accession_sra_studies_accession_get_0) | **GET** /sra/studies/{accession} | Study By Accession
*SRAApi* | [**for_experiment_sra_experiments_accession_runs_get**](docs/SRAApi.md#for_experiment_sra_experiments_accession_runs_get) | **GET** /sra/experiments/{accession}/runs | Runs For Experiment
*SRAApi* | [**for_experiment_sra_experiments_accession_runs_get_0**](docs/SRAApi.md#for_experiment_sra_experiments_accession_runs_get_0) | **GET** /sra/experiments/{accession}/runs | Runs For Experiment
*SRAApi* | [**for_sample_sra_samples_accession_experiments_get**](docs/SRAApi.md#for_sample_sra_samples_accession_experiments_get) | **GET** /sra/samples/{accession}/experiments | Experiments For Sample
*SRAApi* | [**for_sample_sra_samples_accession_experiments_get_0**](docs/SRAApi.md#for_sample_sra_samples_accession_experiments_get_0) | **GET** /sra/samples/{accession}/experiments | Experiments For Sample
*SRAApi* | [**for_sample_sra_samples_accession_runs_get**](docs/SRAApi.md#for_sample_sra_samples_accession_runs_get) | **GET** /sra/samples/{accession}/runs | Runs For Sample
*SRAApi* | [**for_sample_sra_samples_accession_runs_get_0**](docs/SRAApi.md#for_sample_sra_samples_accession_runs_get_0) | **GET** /sra/samples/{accession}/runs | Runs For Sample
*SRAApi* | [**for_study_sra_studies_accession_experiments_get**](docs/SRAApi.md#for_study_sra_studies_accession_experiments_get) | **GET** /sra/studies/{accession}/experiments | Experiments For Study
*SRAApi* | [**for_study_sra_studies_accession_experiments_get_0**](docs/SRAApi.md#for_study_sra_studies_accession_experiments_get_0) | **GET** /sra/studies/{accession}/experiments | Experiments For Study
*SRAApi* | [**for_study_sra_studies_accession_runs_get**](docs/SRAApi.md#for_study_sra_studies_accession_runs_get) | **GET** /sra/studies/{accession}/runs | Runs For Study
*SRAApi* | [**for_study_sra_studies_accession_runs_get_0**](docs/SRAApi.md#for_study_sra_studies_accession_runs_get_0) | **GET** /sra/studies/{accession}/runs | Runs For Study
*SRAApi* | [**for_study_sra_studies_accession_samples_get**](docs/SRAApi.md#for_study_sra_studies_accession_samples_get) | **GET** /sra/studies/{accession}/samples | Samples For Study
*SRAApi* | [**for_study_sra_studies_accession_samples_get_0**](docs/SRAApi.md#for_study_sra_studies_accession_samples_get_0) | **GET** /sra/studies/{accession}/samples | Samples For Study
*SRAApi* | [**sra_experiments_get**](docs/SRAApi.md#sra_experiments_get) | **GET** /sra/experiments | Experiments
*SRAApi* | [**sra_experiments_get_0**](docs/SRAApi.md#sra_experiments_get_0) | **GET** /sra/experiments | Experiments
*SRAApi* | [**sra_fields_entity_get**](docs/SRAApi.md#sra_fields_entity_get) | **GET** /sra/fields/{entity} | Mapping
*SRAApi* | [**sra_runs_get**](docs/SRAApi.md#sra_runs_get) | **GET** /sra/runs | Runs
*SRAApi* | [**sra_runs_get_0**](docs/SRAApi.md#sra_runs_get_0) | **GET** /sra/runs | Runs
*SRAApi* | [**sra_samples_get**](docs/SRAApi.md#sra_samples_get) | **GET** /sra/samples | Samples
*SRAApi* | [**sra_samples_get_0**](docs/SRAApi.md#sra_samples_get_0) | **GET** /sra/samples | Samples
*SRAApi* | [**sra_studies_get**](docs/SRAApi.md#sra_studies_get) | **GET** /sra/studies | Studies
*SRAApi* | [**sra_studies_get_0**](docs/SRAApi.md#sra_studies_get_0) | **GET** /sra/studies | Studies
*DefaultApi* | [**by_index_facets_entity_get**](docs/DefaultApi.md#by_index_facets_entity_get) | **GET** /facets/{entity} | Facets By Index


## Documentation For Models

 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [ResponseModel](docs/ResponseModel.md)
 - [ResponseStats](docs/ResponseStats.md)
 - [ValidationError](docs/ValidationError.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author



