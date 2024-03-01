from head_hunter.data.information_about_vacancies import Vacancy

if __name__ == '__main__':

    name = input('Введите поисковый запрос: ')
    salary = int(input('Введите ожидаемый уровень дохода (например: 50000): '))
    top = int(input('Какое количество вакансий с наибольшим доходом вывести на экран: '))

    user = Vacancy(name, salary, 'Россия')
    user.get_vacancies()
    user.add_vacancies()
    # user.delete_vacancy('93919883')
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
