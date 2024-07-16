#!/usr/bin/env python3
"""
A module testing python framework
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    This class tests the Nested Map functions
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
    ) -> None:
        """
        Testing the access nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception
    ) -> None:
        """
        Testing with access_nested_map raises KeyError appropriately
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class tests Json objections
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict
    ) -> None:
        """
        Tests the json output
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Tests the `memoize` function.
    """
    class TestClass:
        """
        Class to test Memoize
        """

        def a_method(self):
            """
            A simple method that returns 42
            """
            return 42

        @memoize
        def a_property(self):
            """
            A memoized property that calls a_method
            """
            return self.a_method()

        def test_memoize(self):
            """
            Test momoized decorator
            """
            test_instance = self.TestClass()

            with patch.object(
                    self.TestClass, 'a_method', return_value=42
            ) as mock_method:
                result1 = test_instance.a_property
                result2 = test_instance.a_property

                self.assertEqual(result1, 42)
                self.assertEqual(result2, 42)

                mock_method.assert_called_once()
