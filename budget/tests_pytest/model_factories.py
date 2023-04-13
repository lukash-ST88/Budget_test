import factory
from faker import Faker

from django.contrib.auth.models import User

from budget.models import Project, Category, Expense

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    password = 'pass'
    email = 'email'
    is_staff = 'True'


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = 'project'
    budget = 1488


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'cat1'
    project = factory.SubFactory(ProjectFactory)


class CategoryFactory2(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'cat2'
    project = factory.SubFactory(ProjectFactory)


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    title = 'expense1'
    amount = 20
    project = factory.SubFactory(ProjectFactory)
    category = factory.SubFactory(CategoryFactory)


class ExpenseFactory2(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    title = 'expense2'
    amount = 10
    project = factory.SubFactory(ProjectFactory)
    category = factory.SubFactory(CategoryFactory2)
