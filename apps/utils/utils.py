# Vendor
import json
import requests

# Local
from django.conf import settings
from apps.user.models import User


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
