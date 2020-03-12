# coding: utf-8

"""
    OmicIDX

        The OmicIDX API documentation is available in three forms:  - [RapiDoc](/docs) - [OpenAPI/Swagger Interactive](/swaggerdoc) - [ReDoc (more readable in some ways)](/redoc)    # noqa: E501

    The version of the OpenAPI document: 0.99
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import omicidx_client
from omicidx_client.api.sra_api import SRAApi  # noqa: E501
from omicidx_client.rest import ApiException


class TestSRAApi(unittest.TestCase):
    """SRAApi unit test stubs"""

    def setUp(self):
        self.api = omicidx_client.api.sra_api.SRAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_by_accession_sra_experiments_accession_get(self):
        """Test case for by_accession_sra_experiments_accession_get

        Experiment By Accession  # noqa: E501
        """
        pass

    def test_by_accession_sra_runs_accession_get(self):
        """Test case for by_accession_sra_runs_accession_get

        Run By Accession  # noqa: E501
        """
        pass

    def test_by_accession_sra_samples_accession_get(self):
        """Test case for by_accession_sra_samples_accession_get

        Sample By Accession  # noqa: E501
        """
        pass

    def test_by_accession_sra_studies_accession_get(self):
        """Test case for by_accession_sra_studies_accession_get

        Study By Accession  # noqa: E501
        """
        pass

    def test_for_experiment_sra_experiments_accession_runs_get(self):
        """Test case for for_experiment_sra_experiments_accession_runs_get

        Runs For Experiment  # noqa: E501
        """
        pass

    def test_for_sample_sra_samples_accession_experiments_get(self):
        """Test case for for_sample_sra_samples_accession_experiments_get

        Experiments For Sample  # noqa: E501
        """
        pass

    def test_for_sample_sra_samples_accession_runs_get(self):
        """Test case for for_sample_sra_samples_accession_runs_get

        Runs For Sample  # noqa: E501
        """
        pass

    def test_for_study_sra_studies_accession_experiments_get(self):
        """Test case for for_study_sra_studies_accession_experiments_get

        Experiments For Study  # noqa: E501
        """
        pass

    def test_for_study_sra_studies_accession_runs_get(self):
        """Test case for for_study_sra_studies_accession_runs_get

        Runs For Study  # noqa: E501
        """
        pass

    def test_for_study_sra_studies_accession_samples_get(self):
        """Test case for for_study_sra_studies_accession_samples_get

        Samples For Study  # noqa: E501
        """
        pass

    def test_sra_experiments_get(self):
        """Test case for sra_experiments_get

        Experiments  # noqa: E501
        """
        pass

    def test_sra_fields_entity_get(self):
        """Test case for sra_fields_entity_get

        Mapping  # noqa: E501
        """
        pass

    def test_sra_runs_get(self):
        """Test case for sra_runs_get

        Runs  # noqa: E501
        """
        pass

    def test_sra_samples_get(self):
        """Test case for sra_samples_get

        Samples  # noqa: E501
        """
        pass

    def test_sra_studies_get(self):
        """Test case for sra_studies_get

        Studies  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
