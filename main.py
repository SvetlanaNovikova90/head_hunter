# Создание экземпляра класса для работы с API сайтов с вакансиями
from head_hunter.User_interaction import user_interaction
from head_hunter.data.data_api import HeadHunterAPI

hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies()

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