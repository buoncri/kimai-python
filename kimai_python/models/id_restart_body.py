# coding: utf-8

"""
    Kimai - API Docs

    JSON API for the Kimai time-tracking software: [API documentation](https://www.kimai.org/documentation/rest-api.html), [Swagger definition file](doc.json)   # noqa: E501

    OpenAPI spec version: 0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IdRestartBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'copy': 'str',
        'begin': 'str'
    }

    attribute_map = {
        'copy': 'copy',
        'begin': 'begin'
    }

    def __init__(self, copy=None, begin=None):  # noqa: E501
        """IdRestartBody - a model defined in Swagger"""  # noqa: E501
        self._copy = None
        self._begin = None
        self.discriminator = None
        if copy is not None:
            self.copy = copy
        if begin is not None:
            self.begin = begin

    @property
    def copy(self):
        """Gets the copy of this IdRestartBody.  # noqa: E501

        Whether data should be copied to the new entry. Allowed values: all, tags (deprecated), rates (deprecated), description (deprecated), meta (deprecated) (default: nothing is copied)  # noqa: E501

        :return: The copy of this IdRestartBody.  # noqa: E501
        :rtype: str
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """Sets the copy of this IdRestartBody.

        Whether data should be copied to the new entry. Allowed values: all, tags (deprecated), rates (deprecated), description (deprecated), meta (deprecated) (default: nothing is copied)  # noqa: E501

        :param copy: The copy of this IdRestartBody.  # noqa: E501
        :type: str
        """

        self._copy = copy

    @property
    def begin(self):
        """Gets the begin of this IdRestartBody.  # noqa: E501

        Changes the restart date to the given one (default: now)  # noqa: E501

        :return: The begin of this IdRestartBody.  # noqa: E501
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this IdRestartBody.

        Changes the restart date to the given one (default: now)  # noqa: E501

        :param begin: The begin of this IdRestartBody.  # noqa: E501
        :type: str
        """

        self._begin = begin

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(IdRestartBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IdRestartBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
