from engine_classes import *


class Vacancy:
    """Организация информации, полученной из вакансии в удобный вывод для пользователя"""
    __slots__ = ('name', 'company_name', 'client_description', 'staff_count', 'url', 'description', 'experience',
                 'town_title', 'remote_work', 'salary_from', 'salary_to', 'type_of_work', 'place_of_work', 'languages')

    def __init__(self, name, url, company_name, description, remote_work, salary_from, salary_to, *args, **kwargs):
        self.name = name
        self.company_name = company_name
        self.url = url
        self.description = description
        self.remote_work = remote_work
        self.salary_from = salary_from
        self.salary_to = salary_to


    def __str__(self):
        return f'Вакансия - {self.name}, зарплата от- {self.salary_from} и до {self.salary_to} руб/мес'


class CountMixin:
    """Возвращает количество вакансий из файла с вакансиями"""

    @property
    def get_count_of_vacancy(self, x):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        return len(x)


class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """

    def __init__(self, name, company_name, salary_from, salary_to):
        super().__init__(name, company_name, salary_from, salary_to)

    def __str__(self):
        return f'SJ: Работодатель: {self.company_name}, зарплата от: {self.salary_from} и до: {self.salary_to} руб/мес'


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: Работодатель: {self.company_name}, зарплата от: {self.salary_from} и до: {self.salary_to} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass
