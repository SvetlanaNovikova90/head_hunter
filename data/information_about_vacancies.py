from operator import itemgetter
from typing import Any

from head_hunter.data.get_vacancies_api import HeadHunterAPI


class Vacancy(HeadHunterAPI):
    def __init__(self, vacancy: str, salary, top, responsibility = None):
        super().__init__(vacancy)
        self.salary = salary
        self.top = top
        self.responsibility = responsibility
        self.sort_salary = []  # Вакансии с выбранной зарплатой
        self.top_n = []  # N вакансий отсортированных по зарплате
        self.vacancy_now = []  # Все вакансии по аттрибутам

    # @property
    # def name(self):
    #     for i in self.top_n:
    #         return print(f"{i['name']} - {i['salary']}")

    def selecting_attributes(self) -> list[Any]:
        """
        Выборка нужных атрибутов из общего списка
        :return: Список с нужными атрибутами
        """
        for vacancies in self.all_vacancy:
            # print(vacancies['name'], vacancies['area']['name'])
            try:
                if vacancies['salary']['from'] is not None:
                    all_inf = {'name': vacancies['name'], 'id': vacancies['id'], 'salary': vacancies['salary']['from'],
                               'city': vacancies["area"]['name'],
                               'url': vacancies['alternate_url'],
                               'responsibility': vacancies['snippet']['responsibility']}
                    self.vacancy_now.append(all_inf)

            except TypeError:
                continue

    def sorted_salary(self, salary) -> list[Any]:
        """
        Выборка вакансий по зарплате
        :param salary:
        :return: Список вакасий с нужной зарплатой
        """
        for i in self.vacancy_now:
            if i['salary'] >= salary:
                self.sort_salary.append(i)
                print(i['salary'])
        return self.sort_salary

    def get_top_vacancies(self, n) -> list[Any]:
        """
        Выборка необходимого количества вакансий, отсортированных по зарплате
        :return: Список вакансий
        """
        self.sort_salary = sorted(self.sort_salary, key=itemgetter('salary'), reverse=True)
        self.top_n = self.sort_salary[:n]
    def info(self):
        counter = 1
        for i in self.top_n:
            print(f"{counter}) {i['name']}, зарплата: {i['salary']}")
            counter +=1

    def additional_info(self, num):
        counter = 0
        for i in self.top_n:
            counter +=1
            if counter == num:
                print(f'{i["responsibility"]}')

