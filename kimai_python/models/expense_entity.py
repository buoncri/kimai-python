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

class ExpenseEntity(object):
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
        'category': 'ExpenseCategory',
        'description': 'str',
        'cost': 'float',
        'multiplier': 'float',
        'exported': 'bool',
        'refundable': 'bool',
        'total': 'float',
        'begin': 'datetime',
        'activity': 'int',
        'project': 'int',
        'user': 'int',
        'meta_fields': 'list[ExpenseMeta]'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'description': 'description',
        'cost': 'cost',
        'multiplier': 'multiplier',
        'exported': 'exported',
        'refundable': 'refundable',
        'total': 'total',
        'begin': 'begin',
        'activity': 'activity',
        'project': 'project',
        'user': 'user',
        'meta_fields': 'metaFields'
    }

    def __init__(self, id=None, category=None, description=None, cost=None, multiplier=None, exported=None, refundable=None, total=None, begin=None, activity=None, project=None, user=None, meta_fields=None):  # noqa: E501
        """ExpenseEntity - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._category = None
        self._description = None
        self._cost = None
        self._multiplier = None
        self._exported = None
        self._refundable = None
        self._total = None
        self._begin = None
        self._activity = None
        self._project = None
        self._user = None
        self._meta_fields = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.category = category
        if description is not None:
            self.description = description
        self.cost = cost
        if multiplier is not None:
            self.multiplier = multiplier
        self.exported = exported
        self.refundable = refundable
        if total is not None:
            self.total = total
        if begin is not None:
            self.begin = begin
        if activity is not None:
            self.activity = activity
        if project is not None:
            self.project = project
        if user is not None:
            self.user = user
        if meta_fields is not None:
            self.meta_fields = meta_fields

    @property
    def id(self):
        """Gets the id of this ExpenseEntity.  # noqa: E501


        :return: The id of this ExpenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpenseEntity.


        :param id: The id of this ExpenseEntity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this ExpenseEntity.  # noqa: E501


        :return: The category of this ExpenseEntity.  # noqa: E501
        :rtype: ExpenseCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ExpenseEntity.


        :param category: The category of this ExpenseEntity.  # noqa: E501
        :type: ExpenseCategory
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def description(self):
        """Gets the description of this ExpenseEntity.  # noqa: E501


        :return: The description of this ExpenseEntity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExpenseEntity.


        :param description: The description of this ExpenseEntity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def cost(self):
        """Gets the cost of this ExpenseEntity.  # noqa: E501


        :return: The cost of this ExpenseEntity.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ExpenseEntity.


        :param cost: The cost of this ExpenseEntity.  # noqa: E501
        :type: float
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")  # noqa: E501

        self._cost = cost

    @property
    def multiplier(self):
        """Gets the multiplier of this ExpenseEntity.  # noqa: E501


        :return: The multiplier of this ExpenseEntity.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this ExpenseEntity.


        :param multiplier: The multiplier of this ExpenseEntity.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def exported(self):
        """Gets the exported of this ExpenseEntity.  # noqa: E501


        :return: The exported of this ExpenseEntity.  # noqa: E501
        :rtype: bool
        """
        return self._exported

    @exported.setter
    def exported(self, exported):
        """Sets the exported of this ExpenseEntity.


        :param exported: The exported of this ExpenseEntity.  # noqa: E501
        :type: bool
        """
        if exported is None:
            raise ValueError("Invalid value for `exported`, must not be `None`")  # noqa: E501

        self._exported = exported

    @property
    def refundable(self):
        """Gets the refundable of this ExpenseEntity.  # noqa: E501


        :return: The refundable of this ExpenseEntity.  # noqa: E501
        :rtype: bool
        """
        return self._refundable

    @refundable.setter
    def refundable(self, refundable):
        """Sets the refundable of this ExpenseEntity.


        :param refundable: The refundable of this ExpenseEntity.  # noqa: E501
        :type: bool
        """
        if refundable is None:
            raise ValueError("Invalid value for `refundable`, must not be `None`")  # noqa: E501

        self._refundable = refundable

    @property
    def total(self):
        """Gets the total of this ExpenseEntity.  # noqa: E501


        :return: The total of this ExpenseEntity.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ExpenseEntity.


        :param total: The total of this ExpenseEntity.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def begin(self):
        """Gets the begin of this ExpenseEntity.  # noqa: E501


        :return: The begin of this ExpenseEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this ExpenseEntity.


        :param begin: The begin of this ExpenseEntity.  # noqa: E501
        :type: datetime
        """

        self._begin = begin

    @property
    def activity(self):
        """Gets the activity of this ExpenseEntity.  # noqa: E501


        :return: The activity of this ExpenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ExpenseEntity.


        :param activity: The activity of this ExpenseEntity.  # noqa: E501
        :type: int
        """

        self._activity = activity

    @property
    def project(self):
        """Gets the project of this ExpenseEntity.  # noqa: E501


        :return: The project of this ExpenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ExpenseEntity.


        :param project: The project of this ExpenseEntity.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def user(self):
        """Gets the user of this ExpenseEntity.  # noqa: E501


        :return: The user of this ExpenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ExpenseEntity.


        :param user: The user of this ExpenseEntity.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def meta_fields(self):
        """Gets the meta_fields of this ExpenseEntity.  # noqa: E501


        :return: The meta_fields of this ExpenseEntity.  # noqa: E501
        :rtype: list[ExpenseMeta]
        """
        return self._meta_fields

    @meta_fields.setter
    def meta_fields(self, meta_fields):
        """Sets the meta_fields of this ExpenseEntity.


        :param meta_fields: The meta_fields of this ExpenseEntity.  # noqa: E501
        :type: list[ExpenseMeta]
        """

        self._meta_fields = meta_fields

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
        if issubclass(ExpenseEntity, dict):
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
        if not isinstance(other, ExpenseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
