from unittest.mock import Mock, patch

from django.test import TestCase, override_settings
from django.urls import reverse


class WeatherViewTests(TestCase):
    @patch.dict("os.environ", {"OPENWEATHER_API_KEY": "test-key"})
    @patch("weather.views.requests.get")
    def test_displays_weather_for_a_city(self, mock_get):
        mock_get.return_value = Mock(
            status_code=200,
            json=lambda: {
                "name": "Berlin",
                "main": {"temp": 18.5},
                "weather": [{"description": "clear sky", "main": "Clear"}],
            },
        )

        response = self.client.get("/", {"city": "Berlin"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Berlin")
        self.assertContains(response, "18.5")
        mock_get.assert_called_once()

    @patch.dict("os.environ", {}, clear=True)
    def test_reports_missing_configuration(self):
        response = self.client.get("/", {"city": "Berlin"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Weather service is not configured.")
