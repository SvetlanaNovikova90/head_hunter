from head_hunter.data.information_about_vacancies import Vacancy
from head_hunter.data.working_with_files import JSON_file


def user_interaction():
    name = input('Введите поисковый запрос: ')
    salary = int(input('Введите ожидаемый уровень дохода (например: 50000): '))
    top = int(input('Какое количество вакансий с наибольшим доходом вывести на экран: '))

    user = Vacancy(name, salary, 'Россия')
    user.get_vacancies()
    user.add_vacancies()
    user.selecting_attributes()

    user.sorted_salary()

    user.get_top_vacancies(top)
    user.info()
    num = int(input('Если вы хотите дополнительную информацию по одной из вакансий, введите ее номер. \n'
                    '(Если хотите выйти, введите "Выйти"): '))
    if num == "Выйти":
        print('Всего доброго')
    else:
        user.additional_info(num)


if __name__ == '__main__':
    user = Vacancy('Python', 50000, 'Россия')
    user.get_vacancies()
    file = JSON_file()
    name_file = 'data/vacancy.json'
    file.seving_to_file(user.all_vacancy, name_file)
    file.get_inf_from_file(name_file)
    print(file.vacancy)
    file.delete_vacancy_id(name_file, '94107682')
    file.del_to_vacancy(name_file)
    # user_interaction()


