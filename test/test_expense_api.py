# coding: utf-8

"""
    Kimai - API Docs

    JSON API for the Kimai time-tracking software: [API documentation](https://www.kimai.org/documentation/rest-api.html), [Swagger definition file](doc.json)   # noqa: E501

    OpenAPI spec version: 0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import kimai_python
from kimai_python.api.expense_api import ExpenseApi  # noqa: E501
from kimai_python.rest import ApiException


class TestExpenseApi(unittest.TestCase):
    """ExpenseApi unit test stubs"""

    def setUp(self):
        self.api = ExpenseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_expenses_get(self):
        """Test case for api_expenses_get

        Returns a collection of expenses  # noqa: E501
        """
        pass

    def test_api_expenses_id_delete(self):
        """Test case for api_expenses_id_delete

        Delete an existing expense record  # noqa: E501
        """
        pass

    def test_api_expenses_id_duplicate_patch(self):
        """Test case for api_expenses_id_duplicate_patch

        Duplicates an existing expense record  # noqa: E501
        """
        pass

    def test_api_expenses_id_get(self):
        """Test case for api_expenses_id_get

        Returns one expense  # noqa: E501
        """
        pass

    def test_api_expenses_id_meta_patch(self):
        """Test case for api_expenses_id_meta_patch

        Sets the value of a meta-field for an existing expense  # noqa: E501
        """
        pass

    def test_api_expenses_id_patch(self):
        """Test case for api_expenses_id_patch

        Update an existing expense  # noqa: E501
        """
        pass

    def test_api_expenses_post(self):
        """Test case for api_expenses_post

        Creates a new expense  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
