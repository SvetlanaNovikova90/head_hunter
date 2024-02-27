# Создание экземпляра класса для работы с API сайтов с вакансиями
from head_hunter.User_interaction import user_interaction
from head_hunter.data.get_vacancies_api import HeadHunterAPI
from head_hunter.data.information_about_vacancies import JSONSaver, Vacancy

hh_api = HeadHunterAPI('Python')
# print(hh_api.all_vacancies)

hh_api1 = hh_api.get_list_vacancy()
print(hh_api1)

hh_vac = Vacancy('Pethon', 100, 'Опыт')
hh_vac.sort_vacancy()
# for i in Vacancy.cast_to_object_list():
#     if hh_vac < i:
#         print(i)
# print(hh_vac < Vacancy.cast_to_object_list())
# print(hh_vac.cast_to_object_list())
# print(hh_vac.get_list_vacancy())
# print(hh_vac.sort_vacancy())
# var = hh_vac.name


# nn = hh_api.get_attributes(hh_api1)
# for i in mm:
#     print(mm.name)
# hh_api2 = JSONSaver('Python')
# hh_api2.json_file_vacancies()
# nn = hh_api.get_vacancies()
# print(hh_api)
# nm = Vacancy()
# Vacancy.get_attributes()
# print(Vacancy.get_aVacancy.get_attributes()ttributes().__name__)
# print(Vacancy.name)

# Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies()


# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# if __name__ == "__main__":
#     user_interaction()