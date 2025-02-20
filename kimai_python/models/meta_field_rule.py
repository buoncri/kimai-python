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

class MetaFieldRule(object):
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
        'id': 'int',
        'name': 'str',
        'label': 'str',
        'help': 'str',
        'value': 'str',
        'type': 'str',
        'visible': 'bool',
        'required': 'bool',
        'entity_type': 'str',
        'customer': 'int',
        'project': 'int',
        'activity': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'label': 'label',
        'help': 'help',
        'value': 'value',
        'type': 'type',
        'visible': 'visible',
        'required': 'required',
        'entity_type': 'entityType',
        'customer': 'customer',
        'project': 'project',
        'activity': 'activity'
    }

    def __init__(self, id=None, name=None, label=None, help=None, value=None, type=None, visible=None, required=None, entity_type=None, customer=None, project=None, activity=None):  # noqa: E501
        """MetaFieldRule - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._label = None
        self._help = None
        self._value = None
        self._type = None
        self._visible = None
        self._required = None
        self._entity_type = None
        self._customer = None
        self._project = None
        self._activity = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if label is not None:
            self.label = label
        if help is not None:
            self.help = help
        if value is not None:
            self.value = value
        self.type = type
        self.visible = visible
        self.required = required
        if entity_type is not None:
            self.entity_type = entity_type
        if customer is not None:
            self.customer = customer
        if project is not None:
            self.project = project
        if activity is not None:
            self.activity = activity

    @property
    def id(self):
        """Gets the id of this MetaFieldRule.  # noqa: E501


        :return: The id of this MetaFieldRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetaFieldRule.


        :param id: The id of this MetaFieldRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MetaFieldRule.  # noqa: E501


        :return: The name of this MetaFieldRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetaFieldRule.


        :param name: The name of this MetaFieldRule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this MetaFieldRule.  # noqa: E501


        :return: The label of this MetaFieldRule.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MetaFieldRule.


        :param label: The label of this MetaFieldRule.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def help(self):
        """Gets the help of this MetaFieldRule.  # noqa: E501


        :return: The help of this MetaFieldRule.  # noqa: E501
        :rtype: str
        """
        return self._help

    @help.setter
    def help(self, help):
        """Sets the help of this MetaFieldRule.


        :param help: The help of this MetaFieldRule.  # noqa: E501
        :type: str
        """

        self._help = help

    @property
    def value(self):
        """Gets the value of this MetaFieldRule.  # noqa: E501


        :return: The value of this MetaFieldRule.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetaFieldRule.


        :param value: The value of this MetaFieldRule.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this MetaFieldRule.  # noqa: E501


        :return: The type of this MetaFieldRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetaFieldRule.


        :param type: The type of this MetaFieldRule.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def visible(self):
        """Gets the visible of this MetaFieldRule.  # noqa: E501


        :return: The visible of this MetaFieldRule.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this MetaFieldRule.


        :param visible: The visible of this MetaFieldRule.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def required(self):
        """Gets the required of this MetaFieldRule.  # noqa: E501


        :return: The required of this MetaFieldRule.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this MetaFieldRule.


        :param required: The required of this MetaFieldRule.  # noqa: E501
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def entity_type(self):
        """Gets the entity_type of this MetaFieldRule.  # noqa: E501


        :return: The entity_type of this MetaFieldRule.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this MetaFieldRule.


        :param entity_type: The entity_type of this MetaFieldRule.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def customer(self):
        """Gets the customer of this MetaFieldRule.  # noqa: E501


        :return: The customer of this MetaFieldRule.  # noqa: E501
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this MetaFieldRule.


        :param customer: The customer of this MetaFieldRule.  # noqa: E501
        :type: int
        """

        self._customer = customer

    @property
    def project(self):
        """Gets the project of this MetaFieldRule.  # noqa: E501


        :return: The project of this MetaFieldRule.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this MetaFieldRule.


        :param project: The project of this MetaFieldRule.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def activity(self):
        """Gets the activity of this MetaFieldRule.  # noqa: E501


        :return: The activity of this MetaFieldRule.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this MetaFieldRule.


        :param activity: The activity of this MetaFieldRule.  # noqa: E501
        :type: int
        """

        self._activity = activity

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
        if issubclass(MetaFieldRule, dict):
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
        if not isinstance(other, MetaFieldRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
