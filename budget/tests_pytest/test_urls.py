from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView


def test_url_project_list():
    url = reverse('list')
    assert resolve(url).func == project_list


def test_url_add_project():
    url = reverse('add')
    print(dir(resolve(url).func))
    assert resolve(url).func.view_class == ProjectCreateView


def test_url_project_detail():
    url = reverse('detail', args=['some-slug'])
    assert resolve(url).func == project_detail
