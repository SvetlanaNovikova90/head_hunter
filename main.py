from head_hunter.data.information_about_vacancies import Vacancy

if __name__ == '__main__':
    name = input('Введите поисковый запрос: ')
    salary = int(input('Введите ожидаемый уровень дохода (например: 50000): '))
    top = int(input('Какое количество вакансий с наибольшим доходом вывести на экран: '))

    user = Vacancy(name, top, salary)
    user.json_file_vacancies()
    user.selecting_attributes()
    # print(user.vacancy_now)
    user.sorted_salary(salary)

    user.get_top_vacancies(top)
    user.info()
    num = int(input('Если вы хотите дополнительную информацию по одной из вакансий, введите ее номер. \n'
                    '(Если хотите выйти, введите "Выйти"): '))
    if num == "Выйти":
        print('Всего доброго')
    else:
        user.additional_info(num)

    # user.name()

    # print(user.all_vacancy)

    # Преобразование набора данных из JSON в список объектов
    # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
