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

class UserEditForm(object):
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
        'alias': 'str',
        'title': 'str',
        'account_number': 'str',
        'color': 'str',
        'email': 'str',
        'language': 'str',
        'timezone': 'str',
        'enabled': 'bool',
        'roles': 'list[str]'
    }

    attribute_map = {
        'alias': 'alias',
        'title': 'title',
        'account_number': 'accountNumber',
        'color': 'color',
        'email': 'email',
        'language': 'language',
        'timezone': 'timezone',
        'enabled': 'enabled',
        'roles': 'roles'
    }

    def __init__(self, alias=None, title=None, account_number=None, color=None, email=None, language=None, timezone=None, enabled=None, roles=None):  # noqa: E501
        """UserEditForm - a model defined in Swagger"""  # noqa: E501
        self._alias = None
        self._title = None
        self._account_number = None
        self._color = None
        self._email = None
        self._language = None
        self._timezone = None
        self._enabled = None
        self._roles = None
        self.discriminator = None
        if alias is not None:
            self.alias = alias
        if title is not None:
            self.title = title
        if account_number is not None:
            self.account_number = account_number
        if color is not None:
            self.color = color
        self.email = email
        self.language = language
        self.timezone = timezone
        if enabled is not None:
            self.enabled = enabled
        if roles is not None:
            self.roles = roles

    @property
    def alias(self):
        """Gets the alias of this UserEditForm.  # noqa: E501


        :return: The alias of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this UserEditForm.


        :param alias: The alias of this UserEditForm.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def title(self):
        """Gets the title of this UserEditForm.  # noqa: E501


        :return: The title of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserEditForm.


        :param title: The title of this UserEditForm.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def account_number(self):
        """Gets the account_number of this UserEditForm.  # noqa: E501


        :return: The account_number of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this UserEditForm.


        :param account_number: The account_number of this UserEditForm.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def color(self):
        """Gets the color of this UserEditForm.  # noqa: E501

        The hexadecimal color code (default: #d2d6de)  # noqa: E501

        :return: The color of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this UserEditForm.

        The hexadecimal color code (default: #d2d6de)  # noqa: E501

        :param color: The color of this UserEditForm.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def email(self):
        """Gets the email of this UserEditForm.  # noqa: E501


        :return: The email of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserEditForm.


        :param email: The email of this UserEditForm.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def language(self):
        """Gets the language of this UserEditForm.  # noqa: E501


        :return: The language of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UserEditForm.


        :param language: The language of this UserEditForm.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        allowed_values = ["ar", "cs", "da", "de", "de_AT", "de_CH", "el", "en", "en_GB", "eo", "es", "eu", "fa", "fi", "fo", "fr", "he", "hr", "hu", "it", "ja", "ko", "nb_NO", "nl", "pl", "pt", "pt_BR", "ro", "ru", "sk", "sv", "tr", "vi", "zh_CN"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this UserEditForm.  # noqa: E501


        :return: The timezone of this UserEditForm.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserEditForm.


        :param timezone: The timezone of this UserEditForm.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def enabled(self):
        """Gets the enabled of this UserEditForm.  # noqa: E501


        :return: The enabled of this UserEditForm.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserEditForm.


        :param enabled: The enabled of this UserEditForm.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def roles(self):
        """Gets the roles of this UserEditForm.  # noqa: E501


        :return: The roles of this UserEditForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserEditForm.


        :param roles: The roles of this UserEditForm.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ROLE_TEAMLEAD", "ROLE_ADMIN", "ROLE_SUPER_ADMIN"]  # noqa: E501
        if not set(roles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

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
        if issubclass(UserEditForm, dict):
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
        if not isinstance(other, UserEditForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
