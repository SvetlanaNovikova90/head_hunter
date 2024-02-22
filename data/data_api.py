import io
import json
from abc import abstractmethod, ABC

from pydantic import BaseModel, ValidationError
from config import DATA

import requests


class AbstractHHAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(AbstractHHAPI):

    def __init__(self):
        self.all_vacancies = self.get_vacancies()

    def __repr__(self):
        return self.all_vacancies


    def get_vacancies(self):
        """
        Получение вакансий с hh.ru в формате JSON

        :return:
        """
        url = "https://api.hh.ru/vacancies"
        response = requests.get(url)
        if response.status_code == 200:
            # vacancies = response.json()
            vacancy = json.loads(response.text)['items']
            return vacancy
        return print('Ошибка подключения к сайту')

    def json_file_vacancies(self):
        with open('vacancies.json', 'w') as file:
            json.dump(self.get_vacancies(), file)




class Vacancy(BaseModel):
    id: int

    def __init__(self, name):
        self.name = name

    def cast_to_object_list(vacancies_json):
        pass

    def get_specific_vacancy(self, vacancy):
        pass


vac1 = HeadHunterAPI()
# vac = Vacancy()
vnm = vac1.get_vacancies()
vnn = vac1.list_vacancies()
print(vnn)
# url_get = "https://api.hh.ru/vacancies/"
# response = requests.get(url_get)  # отправка GET-запроса
#
