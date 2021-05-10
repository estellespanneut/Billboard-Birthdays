
# def test_example():
#     assert True

# failed the test since we need a user input in the middle of the test

import os
from app.birthday import get_chart

def test_get_chart():
    chart = get_chart("2000-01-01", "hot-100")
    assert chart.title == "The Hot 100"