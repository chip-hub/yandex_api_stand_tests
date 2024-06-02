# Импортируем модуль configuration, он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests 

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается 
#из базового адреса сервиса и пути к его документации, оба определены в модуле конфигурации.

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_products_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=body,
                         headers=data.headers)

# Вызываем функцию get_docs и сохраняем результат в переменную response
# response = get_docs()

# Вызываем функцию get_logs и сохраняем ответ сервера в переменную response
# response = get_logs()

# Вызываем функцию get_users_table и сохраняем ответ сервера в переменную response
# response = get_users_table()

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
# response = post_new_user(data.user_body)

response = post_products_kits(data.product_ids)

print(response.status_code)

print(response.json())