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

class ExpenseEditForm(object):
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
        'customer': 'int',
        'project': 'int',
        'activity': 'int',
        'expense_category': 'str',
        'description': 'str',
        'multiplier': 'float',
        'refundable': 'bool',
        'begin': 'datetime'
    }

    attribute_map = {
        'customer': 'customer',
        'project': 'project',
        'activity': 'activity',
        'expense_category': 'expenseCategory',
        'description': 'description',
        'multiplier': 'multiplier',
        'refundable': 'refundable',
        'begin': 'begin'
    }

    def __init__(self, customer=None, project=None, activity=None, expense_category=None, description=None, multiplier=None, refundable=None, begin=None):  # noqa: E501
        """ExpenseEditForm - a model defined in Swagger"""  # noqa: E501
        self._customer = None
        self._project = None
        self._activity = None
        self._expense_category = None
        self._description = None
        self._multiplier = None
        self._refundable = None
        self._begin = None
        self.discriminator = None
        if customer is not None:
            self.customer = customer
        self.project = project
        if activity is not None:
            self.activity = activity
        self.expense_category = expense_category
        if description is not None:
            self.description = description
        self.multiplier = multiplier
        if refundable is not None:
            self.refundable = refundable
        self.begin = begin

    @property
    def customer(self):
        """Gets the customer of this ExpenseEditForm.  # noqa: E501

        Customer ID  # noqa: E501

        :return: The customer of this ExpenseEditForm.  # noqa: E501
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ExpenseEditForm.

        Customer ID  # noqa: E501

        :param customer: The customer of this ExpenseEditForm.  # noqa: E501
        :type: int
        """

        self._customer = customer

    @property
    def project(self):
        """Gets the project of this ExpenseEditForm.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project of this ExpenseEditForm.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ExpenseEditForm.

        Project ID  # noqa: E501

        :param project: The project of this ExpenseEditForm.  # noqa: E501
        :type: int
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def activity(self):
        """Gets the activity of this ExpenseEditForm.  # noqa: E501

        Activity ID  # noqa: E501

        :return: The activity of this ExpenseEditForm.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ExpenseEditForm.

        Activity ID  # noqa: E501

        :param activity: The activity of this ExpenseEditForm.  # noqa: E501
        :type: int
        """

        self._activity = activity

    @property
    def expense_category(self):
        """Gets the expense_category of this ExpenseEditForm.  # noqa: E501


        :return: The expense_category of this ExpenseEditForm.  # noqa: E501
        :rtype: str
        """
        return self._expense_category

    @expense_category.setter
    def expense_category(self, expense_category):
        """Sets the expense_category of this ExpenseEditForm.


        :param expense_category: The expense_category of this ExpenseEditForm.  # noqa: E501
        :type: str
        """
        if expense_category is None:
            raise ValueError("Invalid value for `expense_category`, must not be `None`")  # noqa: E501

        self._expense_category = expense_category

    @property
    def description(self):
        """Gets the description of this ExpenseEditForm.  # noqa: E501


        :return: The description of this ExpenseEditForm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExpenseEditForm.


        :param description: The description of this ExpenseEditForm.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def multiplier(self):
        """Gets the multiplier of this ExpenseEditForm.  # noqa: E501


        :return: The multiplier of this ExpenseEditForm.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this ExpenseEditForm.


        :param multiplier: The multiplier of this ExpenseEditForm.  # noqa: E501
        :type: float
        """
        if multiplier is None:
            raise ValueError("Invalid value for `multiplier`, must not be `None`")  # noqa: E501

        self._multiplier = multiplier

    @property
    def refundable(self):
        """Gets the refundable of this ExpenseEditForm.  # noqa: E501


        :return: The refundable of this ExpenseEditForm.  # noqa: E501
        :rtype: bool
        """
        return self._refundable

    @refundable.setter
    def refundable(self, refundable):
        """Sets the refundable of this ExpenseEditForm.


        :param refundable: The refundable of this ExpenseEditForm.  # noqa: E501
        :type: bool
        """

        self._refundable = refundable

    @property
    def begin(self):
        """Gets the begin of this ExpenseEditForm.  # noqa: E501


        :return: The begin of this ExpenseEditForm.  # noqa: E501
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this ExpenseEditForm.


        :param begin: The begin of this ExpenseEditForm.  # noqa: E501
        :type: datetime
        """
        if begin is None:
            raise ValueError("Invalid value for `begin`, must not be `None`")  # noqa: E501

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
        if issubclass(ExpenseEditForm, dict):
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
        if not isinstance(other, ExpenseEditForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
