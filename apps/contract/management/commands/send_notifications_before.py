# Vendor
import requests
import json
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.conf import settings
from rest_framework import status

# Local
from apps.contract.models import Contract
from apps.utils.utils import get_arcgis_token, parse_timestamp, send_message_custom
from apps.utils.exceptions import CustomException


class Command(BaseCommand):
    help = "fill contracts"

    def handle(self, *args, **options):
        contracts = Contract.objects.filter(
            user__isnull=False,
            num__isnull=False
        ).all()
        now_date = datetime.now().date()
        for contract in contracts:
            payment_date = contract.payment_date
            last_payment_date = contract.last_payment_date
            if payment_date:
                chat_id = contract.user.tg_chat_id
                print("payment date", payment_date)
                print("now_date", now_date)
                time_difference = now_date - payment_date
                last_time_difference = 30
                if last_payment_date:
                    last_time_difference = now_date - last_payment_date
                print(f"last_time_difference.days: {last_time_difference.days}")
                # Если до оплаты осталось 7 дней и при этом последняя оплата была в теч 7 дней назад и вперед
                if time_difference.days == 7:
                    if contract.user.tg_chat_id:
                        contract_number = contract.num
                        payment_date_str = payment_date.strftime('%d.%m.%Y')
                        message_text = (f"Доброго времени.\n"
                                        f"По вашему договору {contract_number} подходит срок оплаты: "
                                        f"{payment_date_str}.\nПожалуйста, не забудьте оплатить")
                        send_message_custom(chat_id=chat_id, message_text=message_text)
                        print(f"notification sended: {contract_number}")
                else:
                    print("more 7")


