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

class ProjectCollection(object):
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
        'parent_title': 'str',
        'customer': 'int',
        'id': 'int',
        'name': 'str',
        'start': 'datetime',
        'end': 'datetime',
        'comment': 'str',
        'visible': 'bool',
        'billable': 'bool',
        'meta_fields': 'list[ProjectMeta]',
        'teams': 'list[Team]',
        'global_activities': 'bool',
        'color': 'str'
    }

    attribute_map = {
        'parent_title': 'parentTitle',
        'customer': 'customer',
        'id': 'id',
        'name': 'name',
        'start': 'start',
        'end': 'end',
        'comment': 'comment',
        'visible': 'visible',
        'billable': 'billable',
        'meta_fields': 'metaFields',
        'teams': 'teams',
        'global_activities': 'globalActivities',
        'color': 'color'
    }

    def __init__(self, parent_title=None, customer=None, id=None, name=None, start=None, end=None, comment=None, visible=None, billable=None, meta_fields=None, teams=None, global_activities=None, color=None):  # noqa: E501
        """ProjectCollection - a model defined in Swagger"""  # noqa: E501
        self._parent_title = None
        self._customer = None
        self._id = None
        self._name = None
        self._start = None
        self._end = None
        self._comment = None
        self._visible = None
        self._billable = None
        self._meta_fields = None
        self._teams = None
        self._global_activities = None
        self._color = None
        self.discriminator = None
        if parent_title is not None:
            self.parent_title = parent_title
        if customer is not None:
            self.customer = customer
        if id is not None:
            self.id = id
        self.name = name
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if comment is not None:
            self.comment = comment
        self.visible = visible
        self.billable = billable
        if meta_fields is not None:
            self.meta_fields = meta_fields
        if teams is not None:
            self.teams = teams
        self.global_activities = global_activities
        if color is not None:
            self.color = color

    @property
    def parent_title(self):
        """Gets the parent_title of this ProjectCollection.  # noqa: E501


        :return: The parent_title of this ProjectCollection.  # noqa: E501
        :rtype: str
        """
        return self._parent_title

    @parent_title.setter
    def parent_title(self, parent_title):
        """Sets the parent_title of this ProjectCollection.


        :param parent_title: The parent_title of this ProjectCollection.  # noqa: E501
        :type: str
        """

        self._parent_title = parent_title

    @property
    def customer(self):
        """Gets the customer of this ProjectCollection.  # noqa: E501


        :return: The customer of this ProjectCollection.  # noqa: E501
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ProjectCollection.


        :param customer: The customer of this ProjectCollection.  # noqa: E501
        :type: int
        """

        self._customer = customer

    @property
    def id(self):
        """Gets the id of this ProjectCollection.  # noqa: E501


        :return: The id of this ProjectCollection.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectCollection.


        :param id: The id of this ProjectCollection.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectCollection.  # noqa: E501


        :return: The name of this ProjectCollection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCollection.


        :param name: The name of this ProjectCollection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start(self):
        """Gets the start of this ProjectCollection.  # noqa: E501


        :return: The start of this ProjectCollection.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ProjectCollection.


        :param start: The start of this ProjectCollection.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this ProjectCollection.  # noqa: E501


        :return: The end of this ProjectCollection.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ProjectCollection.


        :param end: The end of this ProjectCollection.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def comment(self):
        """Gets the comment of this ProjectCollection.  # noqa: E501


        :return: The comment of this ProjectCollection.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ProjectCollection.


        :param comment: The comment of this ProjectCollection.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def visible(self):
        """Gets the visible of this ProjectCollection.  # noqa: E501


        :return: The visible of this ProjectCollection.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ProjectCollection.


        :param visible: The visible of this ProjectCollection.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def billable(self):
        """Gets the billable of this ProjectCollection.  # noqa: E501


        :return: The billable of this ProjectCollection.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this ProjectCollection.


        :param billable: The billable of this ProjectCollection.  # noqa: E501
        :type: bool
        """
        if billable is None:
            raise ValueError("Invalid value for `billable`, must not be `None`")  # noqa: E501

        self._billable = billable

    @property
    def meta_fields(self):
        """Gets the meta_fields of this ProjectCollection.  # noqa: E501

        All visible meta (custom) fields registered with this project  # noqa: E501

        :return: The meta_fields of this ProjectCollection.  # noqa: E501
        :rtype: list[ProjectMeta]
        """
        return self._meta_fields

    @meta_fields.setter
    def meta_fields(self, meta_fields):
        """Sets the meta_fields of this ProjectCollection.

        All visible meta (custom) fields registered with this project  # noqa: E501

        :param meta_fields: The meta_fields of this ProjectCollection.  # noqa: E501
        :type: list[ProjectMeta]
        """

        self._meta_fields = meta_fields

    @property
    def teams(self):
        """Gets the teams of this ProjectCollection.  # noqa: E501

        If no team is assigned, everyone can access the project (also depends on the teams of the customer)  # noqa: E501

        :return: The teams of this ProjectCollection.  # noqa: E501
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this ProjectCollection.

        If no team is assigned, everyone can access the project (also depends on the teams of the customer)  # noqa: E501

        :param teams: The teams of this ProjectCollection.  # noqa: E501
        :type: list[Team]
        """

        self._teams = teams

    @property
    def global_activities(self):
        """Gets the global_activities of this ProjectCollection.  # noqa: E501


        :return: The global_activities of this ProjectCollection.  # noqa: E501
        :rtype: bool
        """
        return self._global_activities

    @global_activities.setter
    def global_activities(self, global_activities):
        """Sets the global_activities of this ProjectCollection.


        :param global_activities: The global_activities of this ProjectCollection.  # noqa: E501
        :type: bool
        """
        if global_activities is None:
            raise ValueError("Invalid value for `global_activities`, must not be `None`")  # noqa: E501

        self._global_activities = global_activities

    @property
    def color(self):
        """Gets the color of this ProjectCollection.  # noqa: E501


        :return: The color of this ProjectCollection.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectCollection.


        :param color: The color of this ProjectCollection.  # noqa: E501
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
        if issubclass(ProjectCollection, dict):
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
        if not isinstance(other, ProjectCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
