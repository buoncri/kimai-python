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

class CustomerEntity(object):
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
        'number': 'str',
        'comment': 'str',
        'visible': 'bool',
        'billable': 'bool',
        'company': 'str',
        'vat_id': 'str',
        'contact': 'str',
        'address': 'str',
        'country': 'str',
        'currency': 'str',
        'phone': 'str',
        'fax': 'str',
        'mobile': 'str',
        'email': 'str',
        'homepage': 'str',
        'timezone': 'str',
        'meta_fields': 'list[CustomerMeta]',
        'teams': 'list[Team]',
        'budget': 'float',
        'time_budget': 'int',
        'budget_type': 'str',
        'color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'number': 'number',
        'comment': 'comment',
        'visible': 'visible',
        'billable': 'billable',
        'company': 'company',
        'vat_id': 'vatId',
        'contact': 'contact',
        'address': 'address',
        'country': 'country',
        'currency': 'currency',
        'phone': 'phone',
        'fax': 'fax',
        'mobile': 'mobile',
        'email': 'email',
        'homepage': 'homepage',
        'timezone': 'timezone',
        'meta_fields': 'metaFields',
        'teams': 'teams',
        'budget': 'budget',
        'time_budget': 'timeBudget',
        'budget_type': 'budgetType',
        'color': 'color'
    }

    def __init__(self, id=None, name=None, number=None, comment=None, visible=None, billable=None, company=None, vat_id=None, contact=None, address=None, country=None, currency=None, phone=None, fax=None, mobile=None, email=None, homepage=None, timezone=None, meta_fields=None, teams=None, budget=None, time_budget=None, budget_type=None, color=None):  # noqa: E501
        """CustomerEntity - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._number = None
        self._comment = None
        self._visible = None
        self._billable = None
        self._company = None
        self._vat_id = None
        self._contact = None
        self._address = None
        self._country = None
        self._currency = None
        self._phone = None
        self._fax = None
        self._mobile = None
        self._email = None
        self._homepage = None
        self._timezone = None
        self._meta_fields = None
        self._teams = None
        self._budget = None
        self._time_budget = None
        self._budget_type = None
        self._color = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if number is not None:
            self.number = number
        if comment is not None:
            self.comment = comment
        self.visible = visible
        self.billable = billable
        if company is not None:
            self.company = company
        if vat_id is not None:
            self.vat_id = vat_id
        if contact is not None:
            self.contact = contact
        if address is not None:
            self.address = address
        self.country = country
        self.currency = currency
        if phone is not None:
            self.phone = phone
        if fax is not None:
            self.fax = fax
        if mobile is not None:
            self.mobile = mobile
        if email is not None:
            self.email = email
        if homepage is not None:
            self.homepage = homepage
        self.timezone = timezone
        if meta_fields is not None:
            self.meta_fields = meta_fields
        if teams is not None:
            self.teams = teams
        self.budget = budget
        self.time_budget = time_budget
        if budget_type is not None:
            self.budget_type = budget_type
        if color is not None:
            self.color = color

    @property
    def id(self):
        """Gets the id of this CustomerEntity.  # noqa: E501


        :return: The id of this CustomerEntity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerEntity.


        :param id: The id of this CustomerEntity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CustomerEntity.  # noqa: E501


        :return: The name of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerEntity.


        :param name: The name of this CustomerEntity.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def number(self):
        """Gets the number of this CustomerEntity.  # noqa: E501


        :return: The number of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CustomerEntity.


        :param number: The number of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def comment(self):
        """Gets the comment of this CustomerEntity.  # noqa: E501


        :return: The comment of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CustomerEntity.


        :param comment: The comment of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def visible(self):
        """Gets the visible of this CustomerEntity.  # noqa: E501


        :return: The visible of this CustomerEntity.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this CustomerEntity.


        :param visible: The visible of this CustomerEntity.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def billable(self):
        """Gets the billable of this CustomerEntity.  # noqa: E501


        :return: The billable of this CustomerEntity.  # noqa: E501
        :rtype: bool
        """
        return self._billable

    @billable.setter
    def billable(self, billable):
        """Sets the billable of this CustomerEntity.


        :param billable: The billable of this CustomerEntity.  # noqa: E501
        :type: bool
        """
        if billable is None:
            raise ValueError("Invalid value for `billable`, must not be `None`")  # noqa: E501

        self._billable = billable

    @property
    def company(self):
        """Gets the company of this CustomerEntity.  # noqa: E501


        :return: The company of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CustomerEntity.


        :param company: The company of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def vat_id(self):
        """Gets the vat_id of this CustomerEntity.  # noqa: E501


        :return: The vat_id of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """Sets the vat_id of this CustomerEntity.


        :param vat_id: The vat_id of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._vat_id = vat_id

    @property
    def contact(self):
        """Gets the contact of this CustomerEntity.  # noqa: E501


        :return: The contact of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CustomerEntity.


        :param contact: The contact of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def address(self):
        """Gets the address of this CustomerEntity.  # noqa: E501


        :return: The address of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerEntity.


        :param address: The address of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def country(self):
        """Gets the country of this CustomerEntity.  # noqa: E501


        :return: The country of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerEntity.


        :param country: The country of this CustomerEntity.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def currency(self):
        """Gets the currency of this CustomerEntity.  # noqa: E501


        :return: The currency of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CustomerEntity.


        :param currency: The currency of this CustomerEntity.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def phone(self):
        """Gets the phone of this CustomerEntity.  # noqa: E501


        :return: The phone of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CustomerEntity.


        :param phone: The phone of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """Gets the fax of this CustomerEntity.  # noqa: E501


        :return: The fax of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this CustomerEntity.


        :param fax: The fax of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def mobile(self):
        """Gets the mobile of this CustomerEntity.  # noqa: E501


        :return: The mobile of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this CustomerEntity.


        :param mobile: The mobile of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def email(self):
        """Gets the email of this CustomerEntity.  # noqa: E501

        Limited via RFC to 254 chars  # noqa: E501

        :return: The email of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerEntity.

        Limited via RFC to 254 chars  # noqa: E501

        :param email: The email of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def homepage(self):
        """Gets the homepage of this CustomerEntity.  # noqa: E501


        :return: The homepage of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this CustomerEntity.


        :param homepage: The homepage of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

    @property
    def timezone(self):
        """Gets the timezone of this CustomerEntity.  # noqa: E501

        Length was determined by a MySQL column via \"use mysql;describe time_zone_name;\"  # noqa: E501

        :return: The timezone of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CustomerEntity.

        Length was determined by a MySQL column via \"use mysql;describe time_zone_name;\"  # noqa: E501

        :param timezone: The timezone of this CustomerEntity.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def meta_fields(self):
        """Gets the meta_fields of this CustomerEntity.  # noqa: E501

        All visible meta (custom) fields registered with this customer  # noqa: E501

        :return: The meta_fields of this CustomerEntity.  # noqa: E501
        :rtype: list[CustomerMeta]
        """
        return self._meta_fields

    @meta_fields.setter
    def meta_fields(self, meta_fields):
        """Sets the meta_fields of this CustomerEntity.

        All visible meta (custom) fields registered with this customer  # noqa: E501

        :param meta_fields: The meta_fields of this CustomerEntity.  # noqa: E501
        :type: list[CustomerMeta]
        """

        self._meta_fields = meta_fields

    @property
    def teams(self):
        """Gets the teams of this CustomerEntity.  # noqa: E501

        If no team is assigned, everyone can access the customer  # noqa: E501

        :return: The teams of this CustomerEntity.  # noqa: E501
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this CustomerEntity.

        If no team is assigned, everyone can access the customer  # noqa: E501

        :param teams: The teams of this CustomerEntity.  # noqa: E501
        :type: list[Team]
        """

        self._teams = teams

    @property
    def budget(self):
        """Gets the budget of this CustomerEntity.  # noqa: E501


        :return: The budget of this CustomerEntity.  # noqa: E501
        :rtype: float
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this CustomerEntity.


        :param budget: The budget of this CustomerEntity.  # noqa: E501
        :type: float
        """
        if budget is None:
            raise ValueError("Invalid value for `budget`, must not be `None`")  # noqa: E501

        self._budget = budget

    @property
    def time_budget(self):
        """Gets the time_budget of this CustomerEntity.  # noqa: E501


        :return: The time_budget of this CustomerEntity.  # noqa: E501
        :rtype: int
        """
        return self._time_budget

    @time_budget.setter
    def time_budget(self, time_budget):
        """Sets the time_budget of this CustomerEntity.


        :param time_budget: The time_budget of this CustomerEntity.  # noqa: E501
        :type: int
        """
        if time_budget is None:
            raise ValueError("Invalid value for `time_budget`, must not be `None`")  # noqa: E501

        self._time_budget = time_budget

    @property
    def budget_type(self):
        """Gets the budget_type of this CustomerEntity.  # noqa: E501


        :return: The budget_type of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._budget_type

    @budget_type.setter
    def budget_type(self, budget_type):
        """Sets the budget_type of this CustomerEntity.


        :param budget_type: The budget_type of this CustomerEntity.  # noqa: E501
        :type: str
        """

        self._budget_type = budget_type

    @property
    def color(self):
        """Gets the color of this CustomerEntity.  # noqa: E501


        :return: The color of this CustomerEntity.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CustomerEntity.


        :param color: The color of this CustomerEntity.  # noqa: E501
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
        if issubclass(CustomerEntity, dict):
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
        if not isinstance(other, CustomerEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
