from selenium import webdriver
from budget.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

from selenium.webdriver.common.by import By


class TestProjectListPage(StaticLiveServerTestCase):  # liveserverTestCse задействует действующий HTTP server
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')  # определение webdriver'a

    def tearDown(self):
        self.browser.close()  # браузер закрывается перед каждым тестом

    def test_no_projects_alert_is_displayed(self): #тестируем правильность текста в сплывающем предупреждении
        self.browser.get(self.live_server_url)  # запускаем браузер на базовой странице его live HTTPs//...
        # time.sleep(20)  # браузер спит открытым 20 сек

        # пользователь впервые попадает на страницу
        alert = self.browser.find_element(by=By.CLASS_NAME,
                                          value='noproject-wrapper')  # находим div в html с подходящим классом(см. html код страницы)
        self.assertEquals(alert.find_element(by=By.TAG_NAME, value='h3').text,
                          "Sorry, you don't have any projects, yet.") # находим внутри div тег h3 и сравниваем его текст


    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url) # запускаем браузер на базовой странице

        # пользователь жмет add_project
        add_url = self.live_server_url + reverse('add')
        self.browser.find_element(By.TAG_NAME, 'a').click() # нажатие на ссылку
        self.assertEquals(
            self.browser.current_url, add_url # проверяем правильность перехода на новый url
        )

    def test_user_sees_project_list(self):
        pj1 = Project.objects.create( # создаем проект для отображения на home странице
            name="pj1",
            budget=1002
        )
        self.browser.get(self.live_server_url)

        # Пользователь видит один проект
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h5').text, 'pj1'
        )

    def test_user_is_redirected_to_project_detail(self):
        pj2 = Project.objects.create(  # создаем проект для отображения на home странице
            name="pj2",
            budget=1000
        )

        self.browser.get(self.live_server_url)

        # Пользователь нажимает VISIT и перенаправляется на detail page
        detail_url = self.live_server_url + reverse('detail', args=[pj2.slug])
        self.browser.find_element(By.LINK_TEXT, 'VISIT').click()
        self.assertEquals(
            self.browser.current_url, detail_url
        )
