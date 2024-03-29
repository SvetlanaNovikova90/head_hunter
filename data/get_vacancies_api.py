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




