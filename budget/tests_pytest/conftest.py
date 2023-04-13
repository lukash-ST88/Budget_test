import pytest
from pytest_factoryboy import register
from .model_factories import UserFactory, ProjectFactory, CategoryFactory, CategoryFactory2, ExpenseFactory, \
    ExpenseFactory2
from django.urls import reverse
from budget.models import Project

register(UserFactory)
register(ProjectFactory)
register(CategoryFactory)
register(CategoryFactory2)
register(ExpenseFactory)


# предсоздание проекта для каждой функции
# db - ссылка на базу данных
@pytest.fixture(scope='function')
def new_project(db, project_factory):
    project = project_factory.create()
    return project


@pytest.fixture(scope='function')
def new_category(db, category_factory):
    category = category_factory.create()
    print('new project is created')
    return category


@pytest.fixture(scope='function')
def new_expense(db, expense_factory):
    expense = expense_factory.create()
    print('new expense is created')
    return expense


@pytest.fixture(scope='module')
def set_reverse_url():
    print('call fixture set reverse url')
    list_url = reverse('list')
    detail_url = reverse('detail', args=['project'])
    add_url = reverse('add')
    return {'list_url': list_url, 'detail_url': detail_url, 'add_url': add_url}
