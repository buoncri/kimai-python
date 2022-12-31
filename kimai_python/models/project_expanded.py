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

class ProjectExpanded(object):
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
        'customer': 'Customer',
        'name': 'str',
        'comment': 'str',
        'visible': 'bool',
        'billable': 'bool',
        'global_activities': 'bool',
        'color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'customer': 'customer',
        'name': 'name',
        'comment': 'comment',
        'visible': 'visible',
        'billable': 'billable',
        'global_activities': 'globalActivities',
        'color': 'color'
    }

    def __init__(self, id=None, customer=None, name=None, comment=None, visible=None, billable=None, global_activities=None, color=None):  # noqa: E501
        """ProjectExpanded - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer = None
        self._name = None
        self._comment = None
        self._visible = None
        self._billable = None
        self._global_activities = None
        self._color = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.customer = customer
        self.name = name
        if comment is not None:
            self.comment = comment
        self.visible = visible
        self.billable = billable
        self.global_activities = global_activities
        if color is not None:
            self.color = color

    @property
    def id(self):
        """Gets the id of this ProjectExpanded.  # noqa: E501


        :return: The id of this ProjectExpanded.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectExpanded.


        :param id: The id of this ProjectExpanded.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def customer(self):
        """Gets the customer of this ProjectExpanded.  # noqa: E501


        :return: The customer of this ProjectExpanded.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ProjectExpanded.


        :param customer: The customer of this ProjectExpanded.  # noqa: E501
        :type: Customer
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def name(self):
        """Gets the name of this ProjectExpanded.  # noqa: E501


        :return: The name of this ProjectExpanded.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectExpanded.


        :param name: The name of this ProjectExpanded.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this ProjectExpanded.  # noqa: E501


        :return: The comment of this ProjectExpanded.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ProjectExpanded.


        :param comment: The comment of this ProjectExpanded.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def visible(self):
        """Gets the visible of this ProjectExpanded.  # noqa: E501


        :return: The visible of this ProjectExpanded.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ProjectExpanded.


        :param visible: The visible of this ProjectExpanded.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def billable(self):
        """Gets the billable of this ProjectExpanded.  # noqa: E501


        :return: The billable of this ProjectExpanded.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this ProjectExpanded.


        :param billable: The billable of this ProjectExpanded.  # noqa: E501
        :type: bool
        """
        if billable is None:
            raise ValueError("Invalid value for `billable`, must not be `None`")  # noqa: E501

        self._billable = billable

    @property
    def global_activities(self):
        """Gets the global_activities of this ProjectExpanded.  # noqa: E501


        :return: The global_activities of this ProjectExpanded.  # noqa: E501
        :rtype: bool
        """
        return self._global_activities

    @global_activities.setter
    def global_activities(self, global_activities):
        """Sets the global_activities of this ProjectExpanded.


        :param global_activities: The global_activities of this ProjectExpanded.  # noqa: E501
        :type: bool
        """
        if global_activities is None:
            raise ValueError("Invalid value for `global_activities`, must not be `None`")  # noqa: E501

        self._global_activities = global_activities

    @property
    def color(self):
        """Gets the color of this ProjectExpanded.  # noqa: E501


        :return: The color of this ProjectExpanded.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectExpanded.


        :param color: The color of this ProjectExpanded.  # noqa: E501
        :type: str
        """

        self._color = color

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
        if issubclass(ProjectExpanded, dict):
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
        if not isinstance(other, ProjectExpanded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
