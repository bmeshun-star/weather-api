from fastapi.testclient import TestClient
from alert_service.app import app
from unittest.mock import patch
from unittest.mock import Mock, patch

client = TestClient(app)

def test_alert_integration():
    with patch("alert_service.app.requests.get") as mock_get:
        mock_response = Mock()
        mock_get.return_value = mock_response
        mock_response.json.return_value = {"city": "London", "current": {"temperature_2m": 35, "wind_speed_10m": 20}}
        mock_response.raise_for_status.return_value = None
        response = client.get("/alert", params={"city":"London"})
        assert response.status_code == 200
        assert response.json()["alert"] is True 
