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

class ActivityExpanded(object):
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
        'project': 'Project',
        'name': 'str',
        'comment': 'str',
        'visible': 'bool',
        'billable': 'bool',
        'color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project': 'project',
        'name': 'name',
        'comment': 'comment',
        'visible': 'visible',
        'billable': 'billable',
        'color': 'color'
    }

    def __init__(self, id=None, project=None, name=None, comment=None, visible=None, billable=None, color=None):  # noqa: E501
        """ActivityExpanded - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project = None
        self._name = None
        self._comment = None
        self._visible = None
        self._billable = None
        self._color = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        self.name = name
        if comment is not None:
            self.comment = comment
        self.visible = visible
        self.billable = billable
        if color is not None:
            self.color = color

    @property
    def id(self):
        """Gets the id of this ActivityExpanded.  # noqa: E501


        :return: The id of this ActivityExpanded.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActivityExpanded.


        :param id: The id of this ActivityExpanded.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this ActivityExpanded.  # noqa: E501


        :return: The project of this ActivityExpanded.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ActivityExpanded.


        :param project: The project of this ActivityExpanded.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def name(self):
        """Gets the name of this ActivityExpanded.  # noqa: E501


        :return: The name of this ActivityExpanded.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityExpanded.


        :param name: The name of this ActivityExpanded.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this ActivityExpanded.  # noqa: E501


        :return: The comment of this ActivityExpanded.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ActivityExpanded.


        :param comment: The comment of this ActivityExpanded.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def visible(self):
        """Gets the visible of this ActivityExpanded.  # noqa: E501


        :return: The visible of this ActivityExpanded.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ActivityExpanded.


        :param visible: The visible of this ActivityExpanded.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def billable(self):
        """Gets the billable of this ActivityExpanded.  # noqa: E501


        :return: The billable of this ActivityExpanded.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this ActivityExpanded.


        :param billable: The billable of this ActivityExpanded.  # noqa: E501
        :type: bool
        """
        if billable is None:
            raise ValueError("Invalid value for `billable`, must not be `None`")  # noqa: E501

        self._billable = billable

    @property
    def color(self):
        """Gets the color of this ActivityExpanded.  # noqa: E501


        :return: The color of this ActivityExpanded.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ActivityExpanded.


        :param color: The color of this ActivityExpanded.  # noqa: E501
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
        if issubclass(ActivityExpanded, dict):
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
        if not isinstance(other, ActivityExpanded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
