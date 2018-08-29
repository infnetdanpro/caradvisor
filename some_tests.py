import unittest

from get_weather import get_weather_data, get_weather_message, URL_CURRENT_WEATHER, URL_WEATHER_PREDICTION_SIX_HOURS
from holidays import get_holiday
from roads_closed import get_road_restrictions
from get_html import get_html


class GetWeatherTestCase(unittest.TestCase):
    """Tests for get_weather.py"""

    def test_get_weather_data_connection(self):
        result = get_weather_data(URL_CURRENT_WEATHER)
        self.assertEqual(type(result), dict)

    def test_get_weather_message(self):
        result = get_weather_message()
        self.assertEqual(type(result), str)


class GetHolidaysTestCase(unittest.TestCase):
    """Tests for holidays.py"""

    def test_get_holidays(self):
        result_true = get_holiday(day='09-05')
        result_false = get_holiday(day='10-07')
        self.assertTrue(result_true)
        self.assertFalse(result_false)


class RoadsClosedTestCase(unittest.TestCase):
    """Tests for roads_closed.py"""

    def test_get_road_restrictions(self):
        closed_roads = get_road_restrictions()
        self.assertEqual(type(closed_roads), str)


class GetHtmlTestCase(object):
    """docstring for GetHtmlTestCase"""
    def test_get_html(self):
        html = get_html()
        self.assertEqual(type(html), str)


if __name__ == '__main__':
    unittest.main()
