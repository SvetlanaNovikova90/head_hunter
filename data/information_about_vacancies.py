from operator import itemgetter
from typing import Any, List

from head_hunter.data.get_vacancies_api import HeadHunterAPI


class Vacancy(HeadHunterAPI):
    all = []

    def __init__(self, vacancy, salary, city=None, id=None, url=None, responsibility=None):
        super().__init__(vacancy)
        self.salary = salary
        self.city = city
        self.id = id
        self.url = url
        self.responsibility = responsibility
        self.sort_salary = []  # Вакансии с выбранной зарплатой
        self.top_n = []  # N вакансий отсортированных по зарплате
        self.vacancy_now = []  # Все вакансии по аттрибутам

    def selecting_attributes(self, all_vacancy):
        """
        Выборка нужных атрибутов из общего списка
        :return: Список с нужными атрибутами
        """
        for vacancies in all_vacancy:
            # print(vacancies['name'], vacancies['area']['name'])
            try:
                if vacancies['salary']['from'] is not None:
                    all_inf = {'vacancy': vacancies['name'], 'id': vacancies['id'],
                               'salary': vacancies['salary']['from'],
                               'city': vacancies["area"]['name'],
                               'url': vacancies['alternate_url'],
                               'responsibility': vacancies['snippet']['responsibility']}
                    self.vacancy_now.append(all_inf)
                self.vacancy_now = sorted(self.vacancy_now, key=itemgetter('salary'), reverse=True)
            except TypeError:
                continue
        return self.vacancy_now

    @classmethod
    def class_object(cls, vacancy_new):
        """
        Создание экземпляров класса с вакансиями
        :param vacancy: список вакансий
        :return: список экземпляров
        """
        for i in vacancy_new:
            vacancy = i['vacancy']
            id = i['id']
            salary = i['salary']
            city = i['city']
            url = i['url']
            responsibility = i['responsibility']
            vacancy_all = Vacancy(vacancy, salary, city, id, url, responsibility)
            Vacancy.all.append(vacancy_all)
        return Vacancy.all

    def __le__(self, other):
        """
        Метод для сравнения экземпляров класса по зарплате
        :param other: экземпляр класса
        :return: Bool
        """
        return self.salary <= other.salary

    def sorted_salary(self) -> str | list[Any]:
        """
        Выборка вакансий по зарплате
        :return: Список вакансий с нужной зарплатой
        """
        Vacancy.class_object(self.vacancy_now)
        for i in Vacancy.all:
            if self <= i:
                self.sort_salary.append(i)
            else:
                return f'Вакансий с данной зарплатой не найдено'

    def get_top_vacancies(self, n) -> list[Any]:
        """
        Выборка необходимого количества вакансий, отсортированных по зарплате
        :return: Список вакансий
        """
        self.top_n = self.sort_salary[:n]

    def info(self, top_n):
        """
        Вывод инфомации по запросу
        :return:
        """
        counter = 1
        for i in top_n:
            print(f"{counter}) {i.vacancy}, зарплата: {i.salary}")
            counter += 1

    def additional_info(self, num):
        """
        Вывод дополнительной информации по выбранной вакансии
        :param num:
        :return:
        """
        counter = 0
        for i in self.top_n:
            counter += 1
            if counter == num:
                print(f'Описание: {i.responsibility}')
