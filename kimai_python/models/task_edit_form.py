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

class TaskEditForm(object):
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
        'title': 'str',
        'todo': 'str',
        'end': 'datetime',
        'project': 'int',
        'activity': 'int',
        'description': 'str',
        'tags': 'str',
        'user': 'int',
        'team': 'int',
        'estimation': 'int'
    }

    attribute_map = {
        'title': 'title',
        'todo': 'todo',
        'end': 'end',
        'project': 'project',
        'activity': 'activity',
        'description': 'description',
        'tags': 'tags',
        'user': 'user',
        'team': 'team',
        'estimation': 'estimation'
    }

    def __init__(self, title=None, todo=None, end=None, project=None, activity=None, description=None, tags=None, user=None, team=None, estimation=None):  # noqa: E501
        """TaskEditForm - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._todo = None
        self._end = None
        self._project = None
        self._activity = None
        self._description = None
        self._tags = None
        self._user = None
        self._team = None
        self._estimation = None
        self.discriminator = None
        self.title = title
        if todo is not None:
            self.todo = todo
        if end is not None:
            self.end = end
        self.project = project
        self.activity = activity
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if user is not None:
            self.user = user
        if team is not None:
            self.team = team
        if estimation is not None:
            self.estimation = estimation

    @property
    def title(self):
        """Gets the title of this TaskEditForm.  # noqa: E501


        :return: The title of this TaskEditForm.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskEditForm.


        :param title: The title of this TaskEditForm.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def todo(self):
        """Gets the todo of this TaskEditForm.  # noqa: E501

        The actual doings, which will be available on the detail and edit page.  # noqa: E501

        :return: The todo of this TaskEditForm.  # noqa: E501
        :rtype: str
        """
        return self._todo

    @todo.setter
    def todo(self, todo):
        """Sets the todo of this TaskEditForm.

        The actual doings, which will be available on the detail and edit page.  # noqa: E501

        :param todo: The todo of this TaskEditForm.  # noqa: E501
        :type: str
        """

        self._todo = todo

    @property
    def end(self):
        """Gets the end of this TaskEditForm.  # noqa: E501


        :return: The end of this TaskEditForm.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TaskEditForm.


        :param end: The end of this TaskEditForm.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def project(self):
        """Gets the project of this TaskEditForm.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project of this TaskEditForm.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TaskEditForm.

        Project ID  # noqa: E501

        :param project: The project of this TaskEditForm.  # noqa: E501
        :type: int
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def activity(self):
        """Gets the activity of this TaskEditForm.  # noqa: E501

        Activity ID  # noqa: E501

        :return: The activity of this TaskEditForm.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this TaskEditForm.

        Activity ID  # noqa: E501

        :param activity: The activity of this TaskEditForm.  # noqa: E501
        :type: int
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501

        self._activity = activity

    @property
    def description(self):
        """Gets the description of this TaskEditForm.  # noqa: E501


        :return: The description of this TaskEditForm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskEditForm.


        :param description: The description of this TaskEditForm.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this TaskEditForm.  # noqa: E501

        Comma separated list of tags  # noqa: E501

        :return: The tags of this TaskEditForm.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaskEditForm.

        Comma separated list of tags  # noqa: E501

        :param tags: The tags of this TaskEditForm.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def user(self):
        """Gets the user of this TaskEditForm.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this TaskEditForm.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TaskEditForm.

        User ID  # noqa: E501

        :param user: The user of this TaskEditForm.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def team(self):
        """Gets the team of this TaskEditForm.  # noqa: E501

        Team ID  # noqa: E501

        :return: The team of this TaskEditForm.  # noqa: E501
        :rtype: int
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TaskEditForm.

        Team ID  # noqa: E501

        :param team: The team of this TaskEditForm.  # noqa: E501
        :type: int
        """

        self._team = team

    @property
    def estimation(self):
        """Gets the estimation of this TaskEditForm.  # noqa: E501

        Estimation in seconds  # noqa: E501

        :return: The estimation of this TaskEditForm.  # noqa: E501
        :rtype: int
        """
        return self._estimation

    @estimation.setter
    def estimation(self, estimation):
        """Sets the estimation of this TaskEditForm.

        Estimation in seconds  # noqa: E501

        :param estimation: The estimation of this TaskEditForm.  # noqa: E501
        :type: int
        """

        self._estimation = estimation

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
        if issubclass(TaskEditForm, dict):
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
        if not isinstance(other, TaskEditForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
