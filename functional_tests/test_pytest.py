import pytest
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from budget.tests_pytest.conftest import set_reverse_url, new_project


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(executable_path="functional_tests/chromedriver.exe")
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class TestChrome:
    def test_open_url(self, live_server):
        self.driver.get(f'{live_server.url}/add/')
        assert "Budget test" in self.driver.title

    def test_no_projects_alert_is_displayed(self, live_server):
        self.driver.get(live_server.url)
        alert = self.driver.find_element(by=By.CLASS_NAME, value='noproject-wrapper')
        assert alert.find_element(by=By.TAG_NAME, value='h3').text == "Sorry, you don't have any projects, yet."

    def test_no_projects_alert_button_redirects_to_add_page(self, live_server, set_reverse_url):
        self.driver.get(live_server.url)

        add_url = live_server.url + set_reverse_url['add_url']
        self.driver.find_element(By.TAG_NAME, 'a').click()
        assert self.driver.current_url == add_url

    # def test_user_sees_project_list(self, live_server, new_project):
    #     self.driver.get(live_server)
    #     assert self.driver.find_element(By.TAG_NAME, 'h5').text == 'project'
