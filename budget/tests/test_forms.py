from django.test import SimpleTestCase
from budget.forms import *

class TestForms(SimpleTestCase): # класс не использующий модели

    def test_expense_form_valid_data(self):
        form = ExpenseForm(data={
            'title': 'expense1',
            'amount': 1000,
            'category': 'anyCat'
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self): # проверка валидации пустой формы
        form = ExpenseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

