from budget.models import Project


def test_project_list_GET(client, new_project, set_reverse_url):
    response = client.get(set_reverse_url['list_url'])
    print(client.__doc__)
    print(dir(client))
    assert response.status_code == 200


def test_project_detail_GET(client, new_project, set_reverse_url):
    response = client.get(set_reverse_url['detail_url'])
    assert response.status_code == 200

    # def test_project_detail_POST_adds_new_expense(client, new_project, new_category, set_reverse_url):
    #     response = client.post(set_reverse_url['detail_url'], data={
    #         'title': 'expense',
    #         'amount': 1000,
    #         'category': 'cat1'
    #     })  # заполнение  формы
    #     # print(new_project.expenses.values()[0]['title'])
    #     assert response.status_code == 302

# def test_project_create_POST(client, new_project, new_category, set_reverse_url):
#     response = client.post(set_reverse_url['add_url'], {
#         'name': 'prj',
#         'budget': 1100,
#         'categoriesString': 'cat1'
#     })
#     prj = Project.objects.get(name='prj')
#     assert prj.name == 'prj'
