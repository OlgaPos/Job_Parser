import os
from abc import ABC, abstractmethod
from connector import Connector

import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self, keyword):
        """Запрашивает вакансии, в том числе через API"""
        pass

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        """Возвращает экземпляр класса Connector"""
        pass


class SuperJob(Engine):
    HEADERS = {"X-Api-App-Id": os.environ["SuperJob_API_KEY"]}
    URL = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, name=None):  # ne uverena chto tut inizializirovat
        self.name = name

    def get_request(self, keyword):
        """Возвращает список из 500 вакансий, найденных по ключевому слову через API"""
        sj_vacancies = []
        for page_number in range(5):
            response = requests.get(url=self.URL, headers=self.HEADERS,
                                    params={"keywords": keyword, "count": 100,
                                            "page": page_number})
            print(response.status_code)  # mozhno ubrat' ili peredelat' test
            data = response.json()
            if response.status_code == 200:
                for vacancy in data['objects']:
                    sj_vacancies.append(vacancy)
            else:
                print("Что-то пошло не так")  # mozhno ubrat' ili peredelat' test
        return sj_vacancies


class HeadHunter(Engine):
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self, name=None):  # ne uverena chto tut inizializirovat
        self.name = name

    def get_request(self, keyword) -> list:
        hh_vacancies = []
        try:
            response = requests.get(self.URL, params={'text': f'{keyword}', 'page': 0, 'per_page': 100})
            if response.status_code == 200:
                return response.json()

        except requests.RequestException:
            print('Не удается получить данные')

        for page_number in range(5):
            response = requests.get(url=self.URL, params={"text": f"{keyword}", "per_page": 100, "page": 0})
            print(response.status_code)  # mozhno ubrat' ili peredelat' test
            data = response.json()
            if response.status_code == 200:
                for vacancy in data['objects']:
                    hh_vacancies.append(vacancy)
            else:
                print("Что-то пошло не так")  # mozhno ubrat' ili peredelat' test
        return hh_vacancies
