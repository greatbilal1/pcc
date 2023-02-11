import pytest
from employee import Employee


@pytest.fixture
def default_raise():
    default_raise = Employee("Alzy", "Welzy")
    # default_raise.give_raise()
    return default_raise


def test_give_default_raise(default_raise):
    assert default_raise.salary == 0


def test_give_custom_raise(default_raise):
    salary_raise = 5000000
    default_raise.give_raise(salary_raise)
    assert default_raise.salary == salary_raise
