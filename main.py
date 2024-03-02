from head_hunter.data.information_about_vacancies import Vacancy
from head_hunter.data.working_with_files import JSON_file


def user_interaction():
    name = input('Введите поисковый запрос: ')
    salary = int(input('Введите ожидаемый уровень дохода (например: 50000): '))
    top = int(input('Какое количество вакансий с наибольшим доходом вывести на экран: '))

    user = Vacancy(name, salary, 'Россия')
    user.get_vacancies()
    user.selecting_attributes(user.all_vacancy)
    # # Vacancy.class_object(attributes)

    user.sorted_salary()
    user.get_top_vacancies(top)

    user.info(user.top_n)
    num = input('Если вы хотите дополнительную информацию по одной из вакансий, введите ее номер. \n'
                '(Если хотите выйти, введите "Выйти"): ')
    if num.lower() == "выйти":
        print('Всего доброго')
    else:
        user.additional_info(num)


def file_interaction():
    """
    Функция для работы с файлами (пример работы)
    данные сохраняются в файл, удаляется строка по id,
     удаляется все содержимое файла
    :return:
    """
    user = Vacancy('Python', 50000, 'Россия')
    user.get_vacancies()
    file = JSON_file()
    name_file = 'data/vacancy.json'
    file.seving_to_file(user.all_vacancy, name_file)
    file.get_inf_from_file(name_file)
    file.delete_vacancy_id(name_file, '94107682')
    file.del_to_vacancy(name_file)


if __name__ == '__main__':
    user_interaction()
    file_interaction()
