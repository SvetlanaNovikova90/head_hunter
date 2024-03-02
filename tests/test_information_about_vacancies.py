import pytest

from head_hunter.data.information_about_vacancies import Vacancy


@pytest.fixture
def coll():  # имя фикстуры любое

    return [{'id': '92223756', 'name': 'Python',
             'salary': {'from': 60000, 'to': 44000, 'currency': 'RUR', 'gross': True},
             'alternate_url': 'https://hh.ru/vacancy/92223756',
             'area': {'id': '113', 'name': 'Россия', 'url': 'https://api.hh.ru/areas/113'},
             'snippet': {'responsibility': 'Работать с клиентами'}}]


def test_selecting_attributes(coll):
    user = Vacancy('Python', 50000)
    assert user.selecting_attributes(coll) == [
        {'vacancy': 'Python', 'id': '92223756', 'salary': 60000, 'city': 'Россия',
         'url': 'https://hh.ru/vacancy/92223756', 'responsibility': 'Работать с клиентами'}]


def test_class_object(coll):
    user2 = Vacancy('Python', 50000)
    vacancy_new = user2.selecting_attributes(coll)
    for i in user2.class_object(vacancy_new):
        assert i.vacancy == 'Python'
        assert i.id == '92223756'
        assert i.salary == 60000
        assert i.city == 'Россия'
        assert i.url == 'https://hh.ru/vacancy/92223756'
        assert i.responsibility == 'Работать с клиентами'


def test__le__(coll):
    user2 = Vacancy('Python', 50000)
    vacancy_new = user2.selecting_attributes(coll)
    for i in user2.class_object(vacancy_new):
        assert user2.salary <= i.salary


