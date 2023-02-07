from budget.models import *
from django.test import TestCase


class TestModels(TestCase): # класс использующий модели

    @classmethod
    def setUpTestData(cls): # преднастройки тестов для каждого класса
        print('database is created in model test file') # создатся только один раз
        cls.pj1 = Project.objects.create(name='pj1', budget=100)
        cls.cat1 = Category.objects.create(
            project=cls.pj1,
            name='cat1'
        )
        Expense.objects.create(
            project=cls.pj1,
            title='exp1',
            amount=54,
            category=cls.cat1
        )
        Expense.objects.create(
            project=cls.pj1,
            title='exp2',
            amount=12,
            category=cls.cat1
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEquals(self.pj1.slug, 'pj1')

    def test_budget_left(self):
        self.assertEquals(self.pj1.budget_left, 34)

    def test_total_transactions(self):
        self.assertEquals(self.pj1.total_transactions, 2)

    def test_project_get_absolute_url(self):
        self.assertEqual(self.pj1.get_absolute_url(), '/pj1')
