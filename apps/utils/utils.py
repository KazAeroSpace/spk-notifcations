# Vendor
import json
import requests
from rest_framework import status
from datetime import datetime

# Local
from django.conf import settings
from apps.user.models import User
from .exceptions import CustomException


def send_message_for_get_contact(chat_id, message_text):
    # Кастомная отправка сообщений с помощью requests
    check_tg_user = User.objects.filter(tg_chat_id=chat_id).last()

    if check_tg_user:
        url = f'https://api.telegram.org/bot{settings.TOKEN}/sendMessage'
        markup = {
            "keyboard": [[
                {
                    "text": "Поделиться",
                    "request_contact": True
                }
            ]],
            "one_time_keyboard": True,
            "resize_keyboard": True
        }

        # Параметры запроса
        params = {
            'chat_id': chat_id,
            'text': message_text,
            'reply_markup': json.dumps(markup)  # Преобразуем клавиатуру в JSON-строку
        }

        # Отправка POST-запроса
        try:
            response = requests.post(url, data=params, verify=False)

            # Проверка ответа
            if response.status_code == 200:
                response_data = response.json()
                if response_data['ok']:
                    message_id = response_data['result']['message_id']
                    print('Запрос поделиться контактом отправлен')
                    return message_id
                else:
                    print(f'Ошибка при отправке сообщения: {response_data["description"]}')

            else:
                print(f'Ошибка {response.status_code}: {response.text} 2')
        except:
            print(f'Ошибка 2')
    else:
        return None


def send_message_custom(chat_id, message_text, parse_mode='Markdown', web_url=None, button_label=""):
    # Кастомная отправка сообщений с помощью requests
    check_tg_user = User.objects.filter(tg_chat_id=chat_id,).last()
    if check_tg_user:
        url = f'https://api.telegram.org/bot{settings.TOKEN}/sendMessage'

        keyboard = None
        if web_url:
            # Создаем инлайн-клавиатуру
            keyboard = {"inline_keyboard": [[{
                "text": button_label,
                "web_app": {"url": web_url}
            }]]}

        params = {
            'chat_id': chat_id,
            'text': message_text,
            'parse_mode': parse_mode
        }
        if keyboard:
            # Параметры запроса
            params = {
                'chat_id': chat_id,
                'text': message_text,
                'parse_mode': parse_mode,
                'reply_markup': json.dumps(keyboard)  # Преобразуем клавиатуру в JSON-строку
            }

        try:
            # Отправка POST-запроса
            response = requests.post(url, data=params, verify=False)

            # Проверка ответа
            if response.status_code == 200:
                response_data = response.json()
                if response_data['ok']:
                    message_id = response_data['result']['message_id']
                    print(f'Сообщение успешно отправлено. ID сообщения: {message_id}')
                    return message_id
                else:
                    print(f'Ошибка при отправке сообщения: {response_data["description"]}')
            else:
                print(f'Ошибка {response.status_code}: {response.text} 1')
        except:
            print(f'Ошибка 1')
    return None


def send_message_remove_markup(chat_id, message_text):
    check_tg_user = User.objects.filter(tg_chat_id=chat_id,).last()
    if check_tg_user:
        url = f'https://api.telegram.org/bot{settings.TOKEN}/sendMessage'
        markup = json.dumps({"remove_keyboard": True})
        # Параметры запроса
        params = {
            'chat_id': chat_id,
            'text': message_text,
            'reply_markup': markup
        }
        # Отправка POST-запроса
        try:
            response = requests.post(url, data=params, verify=False)

            # Проверка ответа
            if response.status_code == 200:
                response_data = response.json()
                if response_data['ok']:
                    message_id = response_data['result']['message_id']
                    print('Сообщение отправлено 3')
                    return message_id
                else:
                    print(f'Ошибка при удалении кнопки Поделиться : {response_data["description"]} 1')
            else:
                print(f'Ошибка при удалении кнопки Поделиться: {response.status_code} - {response.text} 1')
        except:
            print(f'Ошибка при удалении кнопки Поделиться 1')
    else:
        return None


def get_arcgis_token():
    username: str = settings.ARCGIS_USERNAME
    password: str = settings.ARCGIS_PASSWORD
    get_token_url = settings.ARCGIS_URL_FOR_TOKEN
    arcgis_token_expiration:int = 3600

    data_for_token = {
        "f": "pjson",
        "username": username,
        "password": password,
        "client": "referer",
        "referer": get_token_url,
        "expiration": arcgis_token_expiration
    }

    # print("token_url: {}".format(get_token_url))
    try:
        response = requests.post(get_token_url, data=data_for_token, verify=False)
        # print(f"response.status_code: {response.status_code}")
        if response.status_code != 200:
            raise CustomException(translate_code="arcgis_token_get_error", code=status.HTTP_400_BAD_REQUEST)
        else:
            data = response.json()
            if data.get('error'):
                error_data = data.get('error')
                msg = 'Ошибка получения токена ARCGIS 1: {} - {}'.format(
                        error_data.get('message'),
                        error_data.get('details'))
                raise CustomException(
                    detail_ru=msg,
                    detail_en=msg,
                    detail_kk=msg,
                    code=status.HTTP_400_BAD_REQUEST
                )
        return response.json()
    except:
        raise CustomException(translate_code="arcgis_get_error", code=status.HTTP_400_BAD_REQUEST)

def parse_timestamp(timestamp):
    if timestamp is not None:
        timestamp = int(timestamp) / 1000
        return datetime.fromtimestamp(timestamp)
    return None