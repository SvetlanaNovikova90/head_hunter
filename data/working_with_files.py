import json
import pathlib
from abc import ABC, abstractmethod


class AbConvectorClass(ABC):

    @abstractmethod
    def seving_to_file(self, list_vacancy, file_name):
        pass

    @abstractmethod
    def del_to_vacancy(self,file_name):
        pass

    @abstractmethod
    def get_inf_from_file(self, file_name):
        pass

    @abstractmethod
    def delete_vacancy_id(self, file_name, id_):
        pass


class JSON_file(AbConvectorClass):
    """
    Класс для работы с файлам json
    """

    def __init__(self):
        self.vacancy = []

    def seving_to_file(self, list_vacancy, file_name):
        """
        Сохрнние информации в файл json
        :param list_vacancy: Список вакансий, который будет сохраняться в Фал
        :param file_name: название файла
        :return:
        """
        if len(list_vacancy) == 0:
            return f'Выбранная вакансия не найдена'
        else:
            with open(file_name, 'w+', encoding='utf-8') as file:
                file.write(json.dumps(list_vacancy, ensure_ascii=False, indent=4))

    def del_to_vacancy(self, file_name):
        """
        Удаляет всю информацию из файла
        :param file_name: название файла
        :return:
        """
        confirm = input('Вы уверены, что хотите удалить информацию из файла? [y/n]  ')
        if confirm.lower() == 'y':
            with open(file_name, 'w'):
                pass
            print('Инфомация о вакасии из файла удалена')
        else:
            print('Инфомация о вакасии из файла НЕ удалена')

    def get_inf_from_file(self, file_name):
        """
        Сохранение необходимой информации из файла в список
        :param file_name: название файла
        :return:
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.read()
        obj = json.loads(data)
        for i in obj:
            try:
                if i['salary']['from'] is not None:
                    all_inf = {'vacancy': i['name'], 'id': i['id'],
                               'salary': i['salary']['from'],
                               'city': i["area"]['name'],
                               'url': i['alternate_url'],
                               'responsibility': i['snippet']['responsibility']}
                    self.vacancy.append(all_inf)
            except TypeError:
                continue

    def delete_vacancy_id(self, file_name, id_):
        """
        Удаление вакансии из файла по id
        :param id_: id вакансии
        :return:
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data_new = []
        for i in data:
            if i['id'] != id_:
                data_new.append(i)
        with open(file_name, 'w+', encoding='utf-8') as file:
            file.write(json.dumps(data_new, ensure_ascii=False, indent=4))


