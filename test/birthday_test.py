import billboard
import os
from app.birthday import set_birth_date

def test_set_birth_date():
    assert set_birth_date() == "2000-01-01"