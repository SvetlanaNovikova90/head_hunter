
from operator import itemgetter
from typing import Any

from head_hunter.data.get_vacancies_api import HeadHunterAPI


class Vacancy(HeadHunterAPI):
    def __init__(self, vacancy: str):
        super().__init__(vacancy)
        self.sort_salary = []
        self.top = []
        self.top_n = []

    def sorted_salary(self, salary: int) -> list[Any]:
        """
        Сортировка спска вакансий по
        :param all_vacancy:
        :param salary:
        :param city:
        :return:
        """
        for vacancies in self.all_vacancy:
            # print(vacancies['name'], vacancies['area']['name'])
            try:
                if vacancies['salary']['from'] is not None:
                    if vacancies['salary']['from'] >= salary:
                        self.sort_salary.append(vacancies)
            except TypeError:
                continue
        return self.sort_salary

    def get_top_vacancies(self, n) -> list[Any]:
        """
        Get top vacancies.
        :return: list with vacancies.
        """
        for i in self.sort_salary:
            all_inf = {'name': i['name'], 'id': i['id'], 'salary': i['salary']['from'], 'city': i["area"]['name'],
                       'url': i['alternate_url'],
                       'responsibility': i['snippet']['responsibility']}
            self.top.append(all_inf)

        self.top = sorted(self.top, key=itemgetter('salary'), reverse=True)
        self.top_n = self.top[0:n]

        return self.top_n

