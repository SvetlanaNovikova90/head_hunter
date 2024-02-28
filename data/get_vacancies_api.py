import json
from abc import abstractmethod, ABC
import requests
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA = pathlib.Path(ROOT, '../data/vacancies.json')


class AbstractHHAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(AbstractHHAPI):
    all = []

    def __init__(self, vacancy):
        self.vacancy = vacancy
        self.all_vacancy = self.get_vacancies()

    def __repr__(self):
        return f'{self.all_vacancy}'

    def get_vacancies(self):
        """
        Получение вакансий с hh.ru в формате JSON

        :return:
        """
        response = requests.get(f'https://api.hh.ru/vacancies', {'text': self.vacancy})
        if response.status_code == 200:
            return json.loads(response.text)['items']
        return print('Ошибка подключения к сайту')

    def json_file_vacancies(self) -> str or list:
        """
        Сохранение вакансий в файл json
        :return:
        """

        if len(self.all_vacancy) == 0:
            return f'Выбранная вакансия не найдена'
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False, indent=4))
            return self.all_vacancy

    # def json_file_vacancies(self):
    #     with open('data/vacancies.json', 'w') as file:
    #         json.dump(self.all_vacancies, file, indent=4)

    # def get_list_vacancy(self):
    #     for i in self.all_vacancies:
    #         if i['salary'] is not None:
    #             salary = i['salary']['from']
    #         else:
    #             salary = 0
    #
    #         all_inf = {'name': i['name'], 'id': i['id'], 'salary': salary, 'url': i['alternate_url'],
    #                    'responsibility': i['snippet']['responsibility']}
    #         self.all.append(all_inf)
    #
    #     return self.all
