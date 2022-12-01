from seasons import lived_minutes
from datetime import date
import pytest

def test_lived_minutes():
    today = date.today()
    last_year = today.replace(year = today.year - 1).isoformat()
    assert lived_minutes(last_year) == "Five hundred twenty-five thousand, six hundred minutes"
    two_years_ago = today.replace(year = today.year - 2).isoformat()
    assert lived_minutes(two_years_ago) == "One million, fifty-one thousand, two hundred minutes"

def test_exit():
    with pytest.raises(SystemExit):
        lived_minutes("cat")
    with pytest.raises(SystemExit):
        lived_minutes("1234-1234-1234")
