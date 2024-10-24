# Vendor
import requests
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from rest_framework import status

# Local
from apps.contract.models import Contract
from apps.utils.utils import get_arcgis_token, parse_timestamp
from apps.utils.exceptions import CustomException


class Command(BaseCommand):
    help = "fill contracts"

    def handle(self, *args, **options):
        print("Fill contracts ... ")
        token = get_arcgis_token()['token']
        print(f"token: {token}")

        grvrd_url = f"{settings.ARCGIS_CONTRACT_URL}&token={token}"
        print(grvrd_url)
        response = requests.get(grvrd_url, verify=False)
        if response.status_code != 200:
            raise CustomException(translate_code="contracts_list_getting_error", code=status.HTTP_400_BAD_REQUEST)
        else:
            data = response.json()
            features = data.get('features')
            created = 0
            updated = 0

            for contract in features:
                attrs = contract.get('attributes')
                oid = attrs.get('oid')
                contract_obj = Contract.objects.filter(
                    oid=oid,
                ).last()
                if contract_obj is None:
                    Contract.objects.create(
                        oid=oid,
                        location=attrs.get('location'),
                        area=attrs.get('area_1sq'),
                        price_1sq=attrs.get('price_1sq'),
                        montly=attrs.get('montly'),
                        tenant=attrs.get('tenant'),
                        purpose=attrs.get('purpose'),
                        num_date_agg=attrs.get('num_date_agg'),
                        subrent=attrs.get('subrent'),
                        owner_ddu=attrs.get('owner_ddu'),
                        note=attrs.get('note'),
                        region=attrs.get('region'),
                        tech_passport=attrs.get('tech_passport'),
                        contract_date=parse_timestamp(attrs.get('data_dogovora_arendy')),
                        exp_date=parse_timestamp(attrs.get('exp_date')),
                        payment_date=parse_timestamp(attrs.get('date_of_payment')),
                        last_payment_date=parse_timestamp(attrs.get('date_of_actual_payment')),
                        globalid=attrs.get('globalid'),
                        num=attrs.get('num_dogovora_arendy'),
                        phone_num=attrs.get('number_phone'),
                    )
                    created+=1
                    # break
                else:
                    payment_date = parse_timestamp(str(attrs.get('date_of_payment')))
                    last_payment_date = parse_timestamp(str(attrs.get('date_of_actual_payment')))
                    print(f"payment_date: {payment_date}")
                    print(f"last_payment_date: {last_payment_date}")
                    contract_obj.payment_date = payment_date
                    contract_obj.last_payment_date = last_payment_date
                    contract_obj.phone_num = attrs.get('number_phone'),
                    contract_obj.save()
                    updated += 1
            print("created: ", created)
            print("updated: ", updated)

