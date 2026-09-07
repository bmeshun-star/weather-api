from alert_service.app import should_alert

def test_alert():
    result = should_alert(25, 20)
    assert result is False

def test_temp_above_threshold():
    result = should_alert(35, 20)
    assert result is True

def test_wind_above_threshold():
    result = should_alert(16, 43)
    assert result is True

def test_temp_and_wind_exactly_at_thresholds():
    result = should_alert(30, 40)
    assert result is False
