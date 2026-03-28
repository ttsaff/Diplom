# 🎬 UI и API автотесты для Кинопоиска

## 📌 Описание проекта
Проект содержит автоматизированные UI и API тесты для сайта Кинопоиска.

Реализованы:
- UI тесты с использованием Selenium
- API тесты с использованием requests
- Отчеты Allure

## 📁 Структура проекта
api/            # API методы
pages/          # PageObject
config/         # настройки и .env
test/           # тесты
conftest.py     # фикстуры
requirements.txt
pytest.ini

## ⚙️ Установка
pip install -r requirements.txt

## 🔐 Настройка окружения
Создать файл .env:
API_KEY=your_api_key
BASE_URL=https://api.poiskkino.dev/v1.4/
UI_URL=https://www.kinopoisk.ru/

## Запуск тестов
# Все тесты 
pytest
# Только API
pytest -m api
# Только UI
pytest -m ui

## Allure отчет
pytest --alluredir=allure-results
allure serve allure-results

## 📌 ССылка на отчет по ручному тестированию
https://serovas.yonote.ru/share/05f7fd35-8476-4870-ad13-e3947150bdb5