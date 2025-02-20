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

class ActivityEditForm(object):
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
        'name': 'str',
        'comment': 'str',
        'invoice_text': 'str',
        'project': 'int',
        'color': 'str',
        'visible': 'bool',
        'billable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'comment': 'comment',
        'invoice_text': 'invoiceText',
        'project': 'project',
        'color': 'color',
        'visible': 'visible',
        'billable': 'billable'
    }

    def __init__(self, name=None, comment=None, invoice_text=None, project=None, color=None, visible=None, billable=None):  # noqa: E501
        """ActivityEditForm - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._comment = None
        self._invoice_text = None
        self._project = None
        self._color = None
        self._visible = None
        self._billable = None
        self.discriminator = None
        self.name = name
        if comment is not None:
            self.comment = comment
        if invoice_text is not None:
            self.invoice_text = invoice_text
        if project is not None:
            self.project = project
        if color is not None:
            self.color = color
        if visible is not None:
            self.visible = visible
        if billable is not None:
            self.billable = billable

    @property
    def name(self):
        """Gets the name of this ActivityEditForm.  # noqa: E501


        :return: The name of this ActivityEditForm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityEditForm.


        :param name: The name of this ActivityEditForm.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this ActivityEditForm.  # noqa: E501


        :return: The comment of this ActivityEditForm.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ActivityEditForm.


        :param comment: The comment of this ActivityEditForm.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def invoice_text(self):
        """Gets the invoice_text of this ActivityEditForm.  # noqa: E501


        :return: The invoice_text of this ActivityEditForm.  # noqa: E501
        :rtype: str
        """
        return self._invoice_text

    @invoice_text.setter
    def invoice_text(self, invoice_text):
        """Sets the invoice_text of this ActivityEditForm.


        :param invoice_text: The invoice_text of this ActivityEditForm.  # noqa: E501
        :type: str
        """

        self._invoice_text = invoice_text

    @property
    def project(self):
        """Gets the project of this ActivityEditForm.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project of this ActivityEditForm.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ActivityEditForm.

        Project ID  # noqa: E501

        :param project: The project of this ActivityEditForm.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def color(self):
        """Gets the color of this ActivityEditForm.  # noqa: E501

        The hexadecimal color code (default: #d2d6de)  # noqa: E501

        :return: The color of this ActivityEditForm.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ActivityEditForm.

        The hexadecimal color code (default: #d2d6de)  # noqa: E501

        :param color: The color of this ActivityEditForm.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def visible(self):
        """Gets the visible of this ActivityEditForm.  # noqa: E501


        :return: The visible of this ActivityEditForm.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ActivityEditForm.


        :param visible: The visible of this ActivityEditForm.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def billable(self):
        """Gets the billable of this ActivityEditForm.  # noqa: E501


        :return: The billable of this ActivityEditForm.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this ActivityEditForm.


        :param billable: The billable of this ActivityEditForm.  # noqa: E501
        :type: bool
        """

        self._billable = billable

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
        if issubclass(ActivityEditForm, dict):
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
        if not isinstance(other, ActivityEditForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
