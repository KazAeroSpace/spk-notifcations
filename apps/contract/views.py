# Vendor
import telebot
import requests
from rest_framework.response import Response
from rest_framework import status, permissions as permissions, viewsets
from django.db.transaction import atomic

# Local
from django.conf import settings
from .serializers import *
from .models import Contract
from apps.user.models import User, TgMessageHistory, MessageType
from apps.utils.utils import send_message_for_get_contact, send_message_custom, send_message_remove_markup

bot = telebot.TeleBot(settings.TOKEN)


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("1")
    chat_id = message.chat.id
    tg_username = ''
    if message.from_user.username:
        tg_username = message.from_user.username
    print("2")
    check_user = User.objects.filter(tg_chat_id=chat_id).last()

    from_user = message.from_user
    last_name = ""
    first_name = ""
    language = ""
    if from_user.last_name:
        last_name = from_user.last_name
    if from_user.first_name:
        first_name = from_user.first_name

    if check_user is None:
        username = f'tg_{chat_id}'
        check_user = User.objects.create(
            tg_chat_id=chat_id,
            username=username,
            tg_username=tg_username,
            last_name=last_name,
            first_name=first_name,
        )

    print("3")
    # check_user = 1
    if check_user:
        if check_user.phone is not None:
            message_text = (f"Здравствуйте, {tg_username}.\n"
                            f"Перед тем, как начать пользоваться ботом, необходимо зарегистрироваться\n"
                            f"Для этого пожалуйста вначале поделитесь своим телефоном, нажав кнопку ниже:\n")

            send_message_for_get_contact(chat_id=chat_id, message_text=message_text)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    print("----handle_contact---")
    chat_id = message.chat.id
    print(f"chat_id: {chat_id}")
    if message.contact is not None:
        print("has contact")
        user_obj = User.objects.filter(tg_chat_id=chat_id).last()
        if user_obj:
            user_obj.phone = message.contact.phone_number
            user_obj.save()

            print(f"user_obj 2: {user_obj}")
            contract = Contract.objects.filter(user_id=user_obj.id).last()
            if contract is None:
                message_text = "Теперь введите ваш номер договора чтобы получать уведомления"
                message_id = send_message_remove_markup(chat_id=chat_id, message_text=message_text)
                if message_id:
                    TgMessageHistory.objects.create(
                        message_type=MessageType.ASK_CONTRACT_NUMBER,
                        user=user_obj,
                        message_id=message_id,
                    )
            else:
                exp_date = contract.exp_date
                message_text = f"К вам уже привязан номер договора. Он заканчивается: {exp_date}"
                message_id = send_message_remove_markup(chat_id=chat_id, message_text=message_text)
                if message_id:
                    TgMessageHistory.objects.create(
                        message_type=MessageType.ASK_CONTRACT_NUMBER,
                        user=user_obj,
                        message_id=message_id,
                    )

    else:
        print("else handle contact")
        message_text = "Не удалось получить ваш контакт. Пожалуйста, попробуйте снова: /start"
        send_message_custom(chat_id=chat_id, message_text=message_text)


if settings.IS_LOCAL:
    print("Есть контакт!")
    # bot.polling(none_stop=bool(settings.BOT_POLLING))
