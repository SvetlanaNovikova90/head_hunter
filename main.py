from head_hunter.data.information_about_vacancies import Vacancy
from head_hunter.user_interaction import UserInteraction



if __name__ == '__main__':
    user = Vacancy('Python')
    user.json_file_vacancies()
    user.sorted_salary(50000)
    # print(user.sort_salary
    for i in user.get_top_vacancies(3):
        print(i)

    # print(user.all_vacancy)

    # Преобразование набора данных из JSON в список объектов
    # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
