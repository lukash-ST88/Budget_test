import pytest
from budget.models import Project
from budget.forms import ExpenseForm
from .conftest import new_category


@pytest.mark.parametrize(
    "title, amount, validity",
    [
        ("exp3", 10, True),
        ('', 10, False),
    ],
)
def test_add_expense_form(title, amount, validity):
    form = ExpenseForm(data={
        'title': title,
        'amount': amount,
        'category': new_category

    })
    print(dir(form))
    assert form.is_valid() == validity
