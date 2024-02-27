from collections import defaultdict

from head_hunter.data.get_vacancies_api import HeadHunterAPI


class Vacancy(HeadHunterAPI):
    def __init__(self, vacancy: str):
        super().__init__(vacancy)
        self.sort_salary: dict = defaultdict(list)
        self.top: dict = defaultdict(list)

    def sorted_salary(self, all_vacancy: list, salary: int, city: str) -> dict:
        """
        Сортировка спска вакансий по
        :param all_vacancy:
        :param salary:
        :param city:
        :return:
        """

        for vacancies in all_vacancy:
            if vacancies['salary'] is not None and vacancies['salary']['from'] is not None:
                if vacancies['area']['name'] == city:
                    if vacancies["salary"]['from'] >= salary:
                        self.sort_salary[vacancies["salary"]['from']].append(vacancies)
        return self.sort_salary

