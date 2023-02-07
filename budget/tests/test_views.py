from django.test import TestCase, Client
from budget.views import *
from django.urls import reverse
from budget.models import *
import json

class TestView(TestCase):

    def setUp(self): # преднастройки вызывающиеся для  каждого теста
        print("new database is created") # видно что метод вызывается каждый раз перед тестом
        self.client = Client() #класс имитирующий работу фиктивного веб браузера (его можно не задавать django сам все присвоит)
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['pj1'])
        self.add_url = reverse('add')
        self.pj1 = Project.objects.create(name='pj1', budget=10000)


    def tearDown(self):
        print('закрытие после обработки тест метода')

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed((response, 'budget/project-list.html')) # проверяет используемый шаблон по GET запросу

    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed((response, 'budget/project-detail.html'))  # проверяет используемый шаблон по GET запросу

    def test_project_detail_POST_adds_new_expense(self):
        Category.objects.create(project=self.pj1, name='cat1') # создание категории для заполнения expense

        response = self.client.post(self.detail_url, {
            'title': 'expense1',
            'amount': 1000,
            'category': 'cat1'
        }) # заполнение  формы
        print(f'here is: {self.pj1.expenses.values()[0]["title"]}')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.pj1.expenses.first().title, 'expense1') # проверка внесения нового expense в список проекта

    def test_project_detail_POST_no_data(self):
        response = self.client.post(self.detail_url) # форма осталась пустой

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.pj1.expenses.count(), 0)

    def test_project_detail_DELETE_deletes_expense(self):
        Category.objects.create(project=self.pj1, name='cat1')  # создание категории для удаления экземпляра expense
        Expense.objects.create(
            project=self.pj1,
            title='expense2',
            amount=1000,
            category=Category.objects.get(name='cat1')
        )

        response = self.client.delete(self.detail_url, json.dumps({'id': 1})) # json.dumps преобразует словарь(список) в строку
        dumps = json.dumps({'id': 1}) # только для просмотра в terminal
        print(f"dumps: {dumps}", type(dumps))
        self.assertEquals(response.status_code, 204) # 204 -нет ответа (сервер получил запрос, но ему нечего ответить)
        self.assertEquals(self.pj1.expenses.count(), 0)

    def test_project_detail_DELETE_no_id(self):
        Category.objects.create(project=self.pj1, name='cat1')  # создание категории для удаления экземпляра expense
        Expense.objects.create(
            project=self.pj1,
            title='expense2',
            amount=1000,
            category=Category.objects.get(name='cat1')
        )

        response = self.client.delete(self.detail_url)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(self.pj1.expenses.count(), 1)


    def test_project_create_POST(self):
        response = self.client.post(self.add_url, {
            'name': 'pj2',
            'budget': 1100,
            'categoriesString': 'cat2,cat3'
        })
        self.assertEquals(Project.objects.get(name='pj2').name, 'pj2')
        self.assertEquals(Category.objects.get(name='cat2').name, 'cat2') #нектнокорре
        self.assertEquals(Category.objects.get(id=2).name, 'cat3') #корректно