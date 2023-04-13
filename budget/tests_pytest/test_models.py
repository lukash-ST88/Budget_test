import pytest
from budget.models import Project


def test_new_user(db, user_factory):
    user = user_factory.create()
    print(user)
    print(db.__doc__)
    assert True


def test_new_project(db, new_project):
    print(new_project)
    assert True


def test_project_str(new_project):
    print(new_project)
    assert new_project.__str__() == 'project'


@pytest.mark.parametrize(
    "name, slug, budget, validity",
    [
        ("Project2", "project2", 1000, True),
        # ("Project3", "project3", 1400, False),
    ],
)
def test_project_instance(
        db, project_factory, name, slug, budget, validity
):
    test = project_factory(
        name=name,
        slug=slug,
        budget=budget
    )

    item = Project.objects.filter(name=name).count()
    print(item)
    assert item == validity
