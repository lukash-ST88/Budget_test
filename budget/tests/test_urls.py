from django.test import SimpleTestCase
from django.urls import resolve, reverse
from budget.views import *


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolves(self): #проверка функции адресата url
        url = reverse('list') #reverse ищет path с похожим именем и выводит его url
        print(resolve(url)) # resolve раскрывает данные о функции(классе) и их аргументах по введенному url
        self.assertEquals(resolve(url).func, project_list)

    def test_add_url_is_resolves(self): # проверка класса адресата url
        url = reverse('add')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_resolves(self): # проверка функции с параметрами адресата url
        url = reverse('detail', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_detail)
