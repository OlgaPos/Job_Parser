from engine_classes import *
from vacancy_classes import *

# Запрашивает у пользователя ключевое слова, по которому будет производиться поиск.
keyword = input('Введите ключевое слово для поиска: \n')



sj = SuperJob()
sj.get_request(keyword)
sj_vacancies = SJVacancy()
print(sj_vacancies)



# hh = HeadHunter()
# print(hh.get_request(keyword))
