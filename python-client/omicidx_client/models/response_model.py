# coding: utf-8

"""
    OmicIDX

        The OmicIDX API documentation is available in three forms:  - [RapiDoc](/docs) - [OpenAPI/Swagger Interactive](/swatterdoc) - [ReDoc (more readable in some ways)](/redoc)    # noqa: E501

    The version of the OpenAPI document: 0.99
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from omicidx_client.configuration import Configuration


class ResponseModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'hits': 'list[object]',
        'facets': 'list[object]',
        'stats': 'ResponseStats',
        'success': 'bool',
        'cursor': 'str'
    }

    attribute_map = {
        'hits': 'hits',
        'facets': 'facets',
        'stats': 'stats',
        'success': 'success',
        'cursor': 'cursor'
    }

    def __init__(self, hits=None, facets=None, stats=None, success=None, cursor=None, local_vars_configuration=None):  # noqa: E501
        """ResponseModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hits = None
        self._facets = None
        self._stats = None
        self._success = None
        self._cursor = None
        self.discriminator = None

        self.hits = hits
        self.facets = facets
        self.stats = stats
        self.success = success
        if cursor is not None:
            self.cursor = cursor

    @property
    def hits(self):
        """Gets the hits of this ResponseModel.  # noqa: E501


        :return: The hits of this ResponseModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this ResponseModel.


        :param hits: The hits of this ResponseModel.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and hits is None:  # noqa: E501
            raise ValueError("Invalid value for `hits`, must not be `None`")  # noqa: E501

        self._hits = hits

    @property
    def facets(self):
        """Gets the facets of this ResponseModel.  # noqa: E501


        :return: The facets of this ResponseModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._facets

    @facets.setter
    def facets(self, facets):
        """Sets the facets of this ResponseModel.


        :param facets: The facets of this ResponseModel.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and facets is None:  # noqa: E501
            raise ValueError("Invalid value for `facets`, must not be `None`")  # noqa: E501

        self._facets = facets

    @property
    def stats(self):
        """Gets the stats of this ResponseModel.  # noqa: E501


        :return: The stats of this ResponseModel.  # noqa: E501
        :rtype: ResponseStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this ResponseModel.


        :param stats: The stats of this ResponseModel.  # noqa: E501
        :type: ResponseStats
        """
        if self.local_vars_configuration.client_side_validation and stats is None:  # noqa: E501
            raise ValueError("Invalid value for `stats`, must not be `None`")  # noqa: E501

        self._stats = stats

    @property
    def success(self):
        """Gets the success of this ResponseModel.  # noqa: E501


        :return: The success of this ResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ResponseModel.


        :param success: The success of this ResponseModel.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def cursor(self):
        """Gets the cursor of this ResponseModel.  # noqa: E501


        :return: The cursor of this ResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this ResponseModel.


        :param cursor: The cursor of this ResponseModel.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseModel):
            return True

        return self.to_dict() != other.to_dict()